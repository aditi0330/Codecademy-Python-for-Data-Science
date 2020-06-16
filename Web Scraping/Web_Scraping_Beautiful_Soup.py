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
  
#FindAll
#find all of the occurrences of a tag, instead of just the first one, we can use .find_all().
print(soup.find_all("h1"))

#Using Regex
#every <ol> and every <ul> that the page contains
import re
soup.find_all(re.compile("[ou]l"))

#we want all of the h1 - h9 tags that the page contains
import re
soup.find_all(re.compile("h[1-9]"))

#Using lists
#We can also just specify all of the elements we want to find by supplying the function with a list of the tag names we are looking for
soup.find_all(['h1', 'a', 'p'])

#Using 
#We can pass a dictionary to the attrs parameter of find_all with the desired attributes of the elements we’re looking for. If we want to find all of the elements with the "banner" class, for example, we could use the command
soup.find_all(attrs={'class':'banner'})
soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

#Using a function
def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"

soup.find_all(has_banner_class_and_hello_world)
#This command would find an element that looks like this:
<div class="banner">Hello world</div>

#To find all the a elements
turtle_links = soup.find_all("a")
print(turtle_links)

#To select all of the elements that have the class 'recipeLink'
soup.select(".recipeLink")

#we wanted to select the element that has the id 'selected'
soup.select("#selected")
            
for link in soup.select(".recipeLink > a"):
  webpage = requests.get(link)
  new_soup = BeautifulSoup(webpage)
  
#This loop will go through each link in each .recipeLink div and create a soup object out of the webpage it links to.
# So, it would first make soup out of <a href="spaghetti.html">Funfetti Spaghetti</a>, then <a href="lasagna.html">Lasagna de Funfetti</a>, and so on.
turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  #Add your code here:
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name] = []
  
print(turtle_data)