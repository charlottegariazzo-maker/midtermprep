import requests

def download_book(url):
    """
    :param url: the url to download
    :return: none
    """
    response = requests.get(url)
    print(response.status_code)
    with open("book.txt", "w") as file:
        file.write(response.text)

download_book("https://www.gutenberg.org/cache/epub/43/pg43.txt")

def find_words(book_filename):
    """
    find 3 letter words starting with b inside the book
    :param book_filename: the name of the file containing the book
    :return: none
    """
    found_words = []
    special_characters = ",.;?!”"
    with open("book.txt", "r") as f:
        for line in f:
            line = line.lower()
            # SANITIZE THE LINE BY REMOVING PUNCTUATION
            for c in special_characters:
                line = line.replace(c, "")
            words = line.split()
            for word in words:
                if len(word) == 9 and word[0]=="c" and word not in found_words:
                    found_words.append(word)

    print(len(found_words))
    print(found_words)

find_words("book.txt")