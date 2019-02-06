import random
import sys

filepath = "data\jap_2000-2001-plain.txt"

thesplit = ()

with open(filepath) as f:
    articles = f.read().strip().split("\n")
print(articles)

articles_list = []

author = []
title = []
year = []
doi = []

for article in articles:
    if article.startswith("AF"):
        author.append(article[:2])
    if article.startswith("TI"):
        title = article[3:]
    if article.startswith("PY"):
        year = article[3:]
    if article.startswith("DI"):
        doi = article[3:]
    if article == "ER#":
        articles_list.append("{}. {}, {}, https://doi.org/{}".format(author, title, year, doi))
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
