from bs4 import BeautifulSoup

#read in html file and use beautifulsoup to read it
#with open index.html in read mode call it f standing for file
with open("index.html", "r") as f:
    #there is other parsers you can use but since its a html doc this accepted type for bsoup moduel
    doc = BeautifulSoup(f, "html.parser")

#this prints out the local html doc 
#.prettify implements indents making it easier to read
#print(doc.prettify())

#find specific tag names in the doc
#this will give you access to the first tag name in the doc
#tag = doc.title
#this will allow you to get all tags to find the first letter p
tags = doc.find_all("d")

#this will modify the string and then print hello instead of the actual string
#tag.string = "hello"

#tag will show you the line you are asking for 
#.string will only show the string
#print(tag.string)

print(tags.find_all())