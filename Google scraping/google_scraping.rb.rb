require 'nokogiri'
require 'open-uri'
#Nokogiri is a Ruby gem providing HTML, XML, and Reader parsers. ... Among Nokogiri's many features is the ability to search documents via XPath or CSS3 selectors.
#open uri is a gem which allows to interact with web pages 
puts 'enter your query'
#here we enter the keyword for which we want the top 10 search results of google
question = gets
url = open('https://www.google.com/search?q=' + question)
#opens the given word in google
content = Nokogiri::HTML(url)
#parses the html content from google
#XPath is a query language for selecting nodes from an XML document.
content.xpath('(//div/a/div[text()])').each do |give|
	puts give.content
#gives the top 10 search results of google
end