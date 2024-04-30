from bs4 import BeautifulSoup

with open ("../html/main.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

result = doc.find_all("option")
print(result)