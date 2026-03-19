#!/usr/bin/env ruby
# frozen_string_literal: true

require 'cgi'
require 'date'
require 'fileutils'
require 'nokogiri'
require 'rss'
require 'uri'

TARGET_OFFSET = '-03:00'

def usage!
  warn "Usage: #{$PROGRAM_NAME} FEED_XML_URL_OR_PATH MEDIUM_URL [MEDIUM_URL ...]"
  exit 1
end

def read_feed(source)
  if source =~ %r{\Ahttps?://}
    require 'open-uri'
    URI.open(source, &:read)
  else
    File.read(source)
  end
end

def normalize_medium_url(url)
  uri = URI.parse(url)
  uri.query = nil
  uri.fragment = nil
  uri.to_s
end

def extract_slug(url)
  raw = URI.decode_www_form_component(File.basename(URI.parse(url).path).sub(/-[0-9a-f]+\z/i, ''))
  ascii = raw.unicode_normalize(:nfkd).encode('ASCII', replace: '').downcase
  ascii.gsub(/[^a-z0-9]+/, '-').gsub(/\A-+|-+\z/, '')
end

def clean_text(text)
  CGI.unescapeHTML(text.to_s)
     .gsub(/\u00A0/, ' ')
     .gsub(/[ \t]+/, ' ')
     .gsub(/\n{3,}/, "\n\n")
     .strip
end

def markdown_escape(text)
  text.gsub(/([\\`*_{}\[\]()#+\-.!|>])/, '\\\\\1')
end

def inline_markdown(node)
  case node
  when Nokogiri::XML::Text
    CGI.unescapeHTML(node.text)
  when Nokogiri::XML::Element
    content = node.children.map { |child| inline_markdown(child) }.join
    case node.name
    when 'strong', 'b'
      content.empty? ? '' : "**#{content.strip}**"
    when 'em', 'i'
      content.empty? ? '' : "*#{content.strip}*"
    when 'code'
      "`#{content.gsub('`', '\\`')}`"
    when 'a'
      href = node['href'].to_s.strip
      label = clean_text(content)
      return label if href.empty?

      "[#{label}](#{href})"
    when 'br'
      "\n"
    else
      content
    end
  else
    ''
  end
end

def block_markdown(node, ordered_index = nil)
  case node.name
  when 'p'
    clean_text(inline_markdown(node))
  when 'h1'
    "# #{clean_text(inline_markdown(node))}"
  when 'h2'
    "## #{clean_text(inline_markdown(node))}"
  when 'h3'
    "### #{clean_text(inline_markdown(node))}"
  when 'h4'
    "#### #{clean_text(inline_markdown(node))}"
  when 'blockquote'
    lines = node.element_children.map { |child| block_markdown(child) }.join("\n\n")
    lines.lines.map { |line| line.strip.empty? ? '>' : "> #{line.rstrip}" }.join
  when 'pre'
    code = node.children.map do |child|
      if child.element? && child.name == 'br'
        "\n"
      else
        CGI.unescapeHTML(child.text.to_s)
      end
    end.join
    code = code.gsub(/\u00A0/, ' ').gsub(/\r\n?/, "\n").strip
    "```text\n#{code}\n```"
  when 'ul'
    node.xpath('./li').map { |li| "- #{clean_text(inline_markdown(li))}" }.join("\n")
  when 'ol'
    node.xpath('./li').each_with_index.map { |li, idx| "#{idx + 1}. #{clean_text(inline_markdown(li))}" }.join("\n")
  when 'figure'
    img = node.at_css('img')
    caption = node.at_css('figcaption')
    parts = []
    if img && img['src'] && !img['src'].include?('/_/stat?')
      alt = clean_text(img['alt'])
      parts << "![#{markdown_escape(alt)}](#{img['src']})"
    end
    if caption
      cap = clean_text(caption.text)
      parts << "_#{cap}_" unless cap.empty?
    end
    parts.join("\n\n")
  when 'img'
    src = node['src'].to_s
    return '' if src.empty? || src.include?('/_/stat?')

    alt = clean_text(node['alt'])
    "![#{markdown_escape(alt)}](#{src})"
  when 'hr'
    '---'
  else
    clean_text(inline_markdown(node))
  end
end

def html_to_markdown(html)
  fragment = Nokogiri::HTML::DocumentFragment.parse(html)
  blocks = fragment.children.each_with_object([]) do |node, acc|
    next if node.text? && clean_text(node.text).empty?

    value =
      if node.element?
        block_markdown(node)
      else
        clean_text(node.text)
      end

    acc << value unless value.nil? || value.empty?
  end

  blocks.join("\n\n").gsub(/\n{3,}/, "\n\n").strip + "\n"
end

def description_from_markdown(markdown)
  text = markdown.gsub(/```.*?```/m, '')
                 .gsub(/!\[.*?\]\(.*?\)/, '')
                 .gsub(/\[([^\]]+)\]\((.*?)\)/, '\1')
                 .gsub(/^#+\s+/, '')
                 .gsub(/^[>-]\s+/,'')
                 .gsub(/\*+/, '')
                 .gsub(/`/, '')
                 .gsub(/\s+/, ' ')
  clean = clean_text(text)
  clean.length > 160 ? "#{clean[0, 157].rstrip}..." : clean
end

usage! if ARGV.length < 2

feed_source = ARGV.shift
target_urls = ARGV.map { |url| normalize_medium_url(url) }
feed = RSS::Parser.parse(read_feed(feed_source), false)
items_by_url = feed.items.to_h { |item| [normalize_medium_url(item.link), item] }

target_urls.each do |url|
  item = items_by_url[url]
  unless item
    warn "Article not found in feed: #{url}"
    next
  end

  slug = extract_slug(url)
  dt = item.pubDate.to_datetime.new_offset(TARGET_OFFSET)
  dir = File.join('content', dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'), slug)
  FileUtils.mkdir_p(dir)

  markdown = html_to_markdown(item.content_encoded.to_s)
  description = description_from_markdown(markdown)
  tags = item.categories.map(&:content).map { |tag| clean_text(tag).downcase }.reject(&:empty?).uniq

  frontmatter = []
  frontmatter << '---'
  frontmatter << %(title: "#{item.title.gsub('"', '\"')}")
  frontmatter << %(date: '#{dt.strftime('%Y-%m-%dT%H:%M:%S%:z')}')
  frontmatter << %(slug: #{slug})
  unless tags.empty?
    frontmatter << 'tags:'
    tags.each { |tag| frontmatter << "- #{tag}" }
  end
  frontmatter << 'draft: false'
  frontmatter << %(description: "#{description.gsub('"', '\"')}")
  frontmatter << '---'
  frontmatter << ''

  File.write(File.join(dir, 'index.md'), (frontmatter + [markdown]).join("\n"))
  puts "Imported #{item.title} -> #{dir}/index.md"
end
