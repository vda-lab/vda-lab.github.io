source 'https://rubygems.org'

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', group: :jekyll_plugins
gem 'kramdown', ">= 2.3.1"
gem 'jekyll-seo-tag'

group :jekyll_plugins do
  gem 'jekyll-asciidoc'
end