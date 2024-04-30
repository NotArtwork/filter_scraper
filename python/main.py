from bs4 import BeautifulSoup

with open ("../html/main.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
print(tag)