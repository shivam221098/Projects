import string


def camelCase():
    sentence = input("Enter you sentence: ")  # take input from the user (example: Hello how are you)
    invalid_characters = list(string.punctuation) + list(string.digits)
    # invalid_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'] + ALL DIGITS
    # if these invalid characters are present in my sentence then i have to print a warning message
    warning = False
    for i in sentence:
        if i in invalid_characters:
            warning = True

    sentence = sentence.split()  # Splitting sentence from spaces (example: ['Hello', 'how', 'are', 'you'])
    camelcase = sentence[0].lower()  # making first word of sentence in lowercase
    for word in range(1, len(sentence)):  # making all word's first letter capital and then joining it
        camelcase += sentence[word].title()

    if warning:
        print(camelcase)
        print("Warning: Input is not valid. It contains either special characters or digits.")
    else:
        print(camelcase)


camelCase()