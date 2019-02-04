import random
import sys

filepath = "data\jap_2000-2001-plain.txt"

thesplit = ()

with open(filepath) as f:
    articles = f.read().strip().split("\n")
print(articles)

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

random_articles = random.sample(articles_list, k = int(amount))


for i in random_articles:
    print(i)
    print("\n")

exit = input('Please enter exit to exit: \n')
if exit in ['exit','Exit']:
    print("Goodbye sir!")
    sys.exit()
