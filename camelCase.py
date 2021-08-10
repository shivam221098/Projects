import string as special_symbol


def camelCase(string):
    splitted_string = string.split()       # splitting string from spaces @splitted_string is a list
    if len(splitted_string) == 0:          # if there is no word simply return empty string
        return ''
    elif len(splitted_string) == 1:        # if there is only single letter then return first letter
        return splitted_string[0].lower()
    else:
        splitted_string[0] = splitted_string[0].lower()
        # removing escape sequences
        for i in range(len(splitted_string)):
            if "\\n" in splitted_string[i]:
                splitted_string[i] = splitted_string[i].replace("\\n", "")
            if "\\t" in splitted_string[i]:
                splitted_string[i] = splitted_string[i].replace("\\t", "")

        camelcase = splitted_string[0]
        for i in range(1, len(splitted_string)):
            camelcase += splitted_string[i].title()

        # removing special symbols
        for letter in camelcase:
            if letter in special_symbol.punctuation:
                camelcase = camelcase.replace(letter, "")

        return camelcase


if __name__ == '__main__':
    sentence = input("Enter your sentence: ")
    print(camelCase(sentence))