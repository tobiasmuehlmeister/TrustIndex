import random
filepath = "data\jap_2000-2001-plain.txt"

with open(filepath) as f:
    articles = f.read().strip().split("\n")

articles_list = []

author = ""
title = ""
year = ""
doi = ""

for article in articles:
    if "AU" in article:
        author = article.split("#")[-1]
    if "TI" in article:
        title = article.split("#")[-1]
    if "PY" in article:
        year = article.split("#")[-1]
    if "DI" in article:
        doi = article.split("#")[-1]
    if article == "ER#":
        articles_list.append("{}, {}, {}, https://doi.org/{}".format(author, title, year, doi))

print("Oh hello sir, how many articles do you like to get?")
amount = input()
print(random.sample(articles_list, k = int(amount)))