class Author:
    # Initializing Author class with name and an empty list of books
    def __init__(self, name):
        self.name = name
        self.books = []

    # Adding new books to author's book list and checking if the book given has the same name as a book currently in the books list
    def publish(self, title):
        if title in self.books:
            print("Error book already added")
        else:
            self.books.append(title)
            print("Your book: ({}) is successfully added.".format(title))

    # returning name of author with their book published
    def __str__(self):
        return "Name of author: {} \nPublished books: {}".format(self.name, "".join(self.books))


if __name__ == '__main__':
    author1 = Author("Micheal")  # name added
    author1.publish("Python tips and tricks")  # book added
    # if I add this book again, I will get an error message and book can't be added again.
    author1.publish("Python tips and tricks")
    print(author1)
