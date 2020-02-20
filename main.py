import csv
import pprint

allBooks = [] # All books in system
libraries = [] # All libraries that exist
signed = [] # All libraries that are signed up

class Library:
    def __init__(self, id, bookNum, processing, speed, books, score, pref):
        self.id = id
        self.procDays = int(processing) # How long it takes to sign up
        self.bookNum = bookNum # Books that exist in the library
        self.perDay = speed # Processing speed of the books
        self.books = books
        self.score = score
        self.pref = pref
        self.collection = []

# Open file and load data
f = open('Data/b_read_on.txt', 'r')
dirty = f.readlines()
data = [line[:-1] for line in dirty]
f.close()

header = data[0].split(" ")

totalBook = header[0]
totalLib = header[1]
deadline = int(header[2])
scores = data[1].split(" ")

for line in data[3::2]: # Books
    allBooks.append(line.split(" "))

count = 0
for line in data[2::2]: # Libraries
    score = 0
    l = line.split(" ")
    for book in allBooks[count]:
        score += int(scores[int(book)])
    pref = score * int(l[2])
    library = Library(count, l[0], l[1], l[2], allBooks[count], score, pref)
    libraries.append(library)
    count+=1

ranked = sorted(libraries, key=lambda x: x.pref, reverse=True)

inprog = False
daysleft = 0
for day in range(0,deadline):
    print("Day",day)
    # Add books from registered libraries
    for library in signed:
        # add books from library
        for x in range(0,int(library.perDay)):
            book = None
            try:
                book = library.books.pop(0)
                library.collection.append(book)
            except:
                print("No more books available")
        print(library.collection)

    # Add unregisterred libraries
    if not inprog:
        try:
            popped = ranked.pop(0)
            daysleft = popped.procDays - 1
            inprog = True
        except:
            print("No more libraries")
    else:
        daysleft -= 1
        if daysleft <= 0:
            signed.append(popped)
            print("Library added:",popped.id)
            inprog = False
   
print("---------------------------------------------")
output = []
output.append(len(signed))

for library in signed:
    bookl = ""
    output.append(library.id)
    for item in library.collection:
        bookl += item + " "
    output.append(bookl)

pprint.pprint(output)

with open('output.txt', 'w') as f:
    for item in output:
        f.write("%s\n" % item)