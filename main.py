# ---------------- OPEN AND PARSE HTML FILE ------------------ #
from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# ---------------- PRINT WEBPAGE ------------------ #
# print(soup.prettify())  # Print out indented version of entire webpage

# ---------------- FIND ALL TAGS OF TYPE ------------------ #
# all_anchor_tags = soup.find_all(name="a")  # Store all anchor tags in a list
# for tag in all_anchor_tags:
#     print(tag.getText())  # Print text of tag
#     print(tag.get("href"))  # Print link of tag

# ---------------- SEARCH FOR SPECIFIC TAG USING find()/find_all() ------------------ #
# heading = soup.find(name="h1", id="name")  # name: name of element | id: that element's ID
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")  # "class" is a Python keyword. Must have _ after
# print(section_heading)

# ---------------- SEARCH FOR SPECIFIC TAG USING select_one()/select() ------------------ #
company_url = soup.select_one(selector="p a")  # Searches for an "a" element inside a "p" element
print(company_url)

name = soup.select_one(selector="#name")  # Searches for an id called "name"
print(name)

headings = soup.select(selector=".heading")  # Searches for a class called "heading"
print(headings)
