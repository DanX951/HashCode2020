import csv

allBooks = [] # All books in system
libraries = [] # All libraries that exist
signed = [] # All libraries that are signed up

class Library:
    def __init__(self, processing, bookNum, speed, books, score):
        self.procDays = processing # How long it takes to sign up
        self.bookNum = bookNum # Books that exist in the library
        self.perDay = speed # Processing speed of the books
        self.books = books
        self.score = score

# Open file and load data
f = open('Data/a_example.txt', 'r')
data = f.readlines()
f.close()

header = data[0].rstrip().split(" ")

totalBook = header[0]
totalLib = header[1]
totalDays = header[2]
scores = data[1].rstrip().split(" ")

count = 2
books = []
bookScore = 0

for line in data[2:]:
    if (count % 2) == 0: # Library data
        libData = line.rstrip().split(" ")
        libScore = bookScore * int(libData[2])
        libraries.append(Library(libData[1], libData[0], libData[2], books, libScore))
    else: # Book data
        books = line.rstrip().split(" ")
        for book in books:
            bookScore += int(scores[int(book)])
    count+=1

for library in libraries:
    print(library.score)