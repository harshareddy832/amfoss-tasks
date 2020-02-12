require 'nokogiri'
require 'open-uri'
puts 'search here'
request = gets
link = open('https://www.google.com/search?q=' + request)
data = Nokogiri::HTML(link)
data.xpath('(//div/a/div[text()])').each do |give|
	puts give.data
end
