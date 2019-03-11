import random
import datetime

# The title
print('TrustIndex')
print("___________________________________________________________________________________")

# function for finding duplicates. Otherwise it would return the same first index for
# all duplicates, like: 2,2,2,2, for "PT J"


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


# Opening the designated file; currently, it needs to be a txt output file from web of science.
# A sample of this output is pictured in the readme file.

filepath = "data\JAP.txt"
with open(filepath, encoding="UTF8") as f:
    articles = f.read().strip().split("\n")

# Print a timestamp
print("\n")
print(datetime.datetime.now())

# Scanning for the name of the journal and available years:
while True:
    journal_name = [i for i in articles if i.startswith('SO ')]
    journal_name_clean = journal_name[0].replace("SO ", "")
    journal_year = [i for i in articles if i.startswith('PY ')]
    journal_year_dup = list(set(journal_year))
    journal_year_clean = ', '.join(journal_year_dup)

    # The empty list:
    articles_list = []

    # Defining the range of one article from start to finish:
    start = list_duplicates_of(articles, "PT J")
    end = list_duplicates_of(articles, "ER")

    for i, j in list(zip(start, end)):
        i = i + 1
        articles_list.append(articles[i:j])

    # The dialogue with the user
    timeprint = str(datetime.datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "-")
    # Getting the number of articles and all scanned years.
    dialogue_raw = ("Welcome, you are about to get a random draw out of " + str(len(articles_list)) + " articles of the \""
                    + str(journal_name_clean) + "\" from the year(s) " + str(journal_year_clean) + ". You are welcome.")
    # Cleaning the dialogue
    dialogue1 = dialogue_raw.replace("PY ", "")

    print("\n")
    print(dialogue1)
    print("\n")
    print("Now, how many random articles do you like to get on this sunny day?")
    amount = input()
    # Check if entered number is a number and lower or equal to the total amount of articles
    if amount.isdigit():
        # Drawing random articles from the population file:
        random_articles = random.sample(articles_list, k = int(amount))

        # Creating an output file with timestamp as title (in txt format)
        f = open("output/" + timeprint + ".txt","w+", encoding="UTF8")
        for i in random_articles:
            i = str(i)
            i = i.replace("AU ", "Author(s): ").replace("AF ", "Author(s): ").replace("TI ", "Title: ")\
                .replace("DI ", "DOI: https://doi.org/").replace("SO ", "Journal: ").replace("PY ", "Year: ").replace("'", "").replace("[", "").replace("]", "")
            i = ''.join(i)
            # print(i, sep = "\n")
            f.write(str(i).replace(",    ", " ") + '\n')

        f.close()
        print("You will find the chosen articles here:\n>>> output/" + str(timeprint) + ".txt <<<")

        # Setting up a new round
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
    else:
        print("No, " + amount + " is not a number! Again.")
        continue
