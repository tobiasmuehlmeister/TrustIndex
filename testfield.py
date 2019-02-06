import random
import sys
from fpdf import FPDF
import datetime
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# Some pretty stuff
cprint(figlet_format('TrustIndex', font='big'),
       'yellow', 'on_red')
print("___________________________________________________________________________________")

# function for finding duplicates. Otherwise it would return the same index for duplicates, like: 2,2,2,2, for "PT J" (don't know why)
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

# Opening the designated file of joy:
filepath = "data\jap_2000.txt"
with open(filepath) as f:
    articles = f.read().strip().split("\n")

# Print a timestamp
print("\n")
print(datetime.datetime.now())

while True:
# Scanning for the name of the journal and available years:
    journal_name = [i for i in articles if i.startswith('SO ')]
    journal_name_clean = journal_name[0].replace("SO ", "")
    journal_year = [i for i in articles if i.startswith('PY ')]
    journal_year_dup = list(set(journal_year))
    journal_year_clean = ', '.join(journal_year_dup)

    # The majestic empty list:
    articles_list = []

    # Defining the range of one article from start to finish:
    start = list_duplicates_of(articles, "PT J")
    end = list_duplicates_of(articles, "ER")

    for i, j in list(zip(start, end)):
        i = i + 1
        articles_list.append(articles[i:j])

    # The dialogue
    timeprint = str(datetime.datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "-")

    dialogue_raw = ("Welcome sir, you are about to get a random draw out of the \""
                    + str(journal_name_clean) + "\" from the year(s) " + str(journal_year_clean) + ". You are welcome.")
    dialogue1 = dialogue_raw.replace("PY ", "")

    print("\n")
    print(dialogue1)
    print("\n")
    print("Now, how many random articles do you like to get on this sunny day?")
    amount = input('Choose a number:')

    # Gotta love the random stuff:
    random_articles = random.sample(articles_list, k = int(amount))

    # Merge and replace + PDF stuff:
    pdflist = []
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=9)

    f = open("output/" + timeprint + ".txt","w+")
    for i in random_articles:
        i = str(i)
        i = i.replace("AU ", "Author(s): ").replace("AF ", "Author(s): ").replace("TI ", "Title: ")\
            .replace("DI ", "DOI: https://doi.org/").replace("SO ", "Journal: ").replace("PY ", "Year: ").replace("'", "").replace("[", "").replace("]", "")
        i = ''.join(i)
        # print(i, sep = "\n")
        f.write(str(i).replace(",    ", " ") + '\n')
        pdflist.append(i)

    f.close()
    print("You will find the chosen articles under:\n>>> output/" + str(timeprint) + ".txt <<<")

    while True:
        answer = input("What about another run? (y/n): ")
        if answer in ("y", "n"):
            break
        print("Invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye sir!")
        break
