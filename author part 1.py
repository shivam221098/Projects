class Author:
    def __init__(self, name):
        # Initializing Author class with name and an empty list of books
        self.name = name
        self.books = []

    # Adding new books to author's book list
    def publish(self, title):
        self.books.append(title)
        print("Your book: ({}) is successfully added.".format(title))

    # returning name of author with their book published
    def __str__(self):
        return "Name of author: {} \nPublished books: {}".format(self.name, "".join(self.books))


if __name__ == '__main__':
    author1 = Author("Micheal")  # name added
    author1.publish("Python tips and tricks")  # book added
    print(author1)
