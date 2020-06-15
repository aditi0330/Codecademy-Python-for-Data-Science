import requests

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html/http-requests')
webpage = webpage_response.content
print(webpage)

#Using Beautiful Soup
from bs4 import BeautifulSoup

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

print(soup)
#to print the first p tag
print(soup.p)
#to print string associated with the first p tag
print(soup.p.string)

for child in soup.ul.children:
    print(child)
    
for parent in soup.li.parents:
    print(parent)
#Above two loos print out the same thing.

#Loop through all of the children of the first div and print out each one.
for child in soup.div.children:
  print(child)