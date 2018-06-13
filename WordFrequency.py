import os

def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ");
    text = text.replace("\r", " ");
    text = text.replace(",","").replace(".", " ").replace("?"," ").replace("!"," ").replace("  "," ")
    text = text.replace("\"", "").replace("(", "").replace(")","").replace("  "," ")
    text = text.replace(" '"," ").replace("' "," ").replace("  "," ")
    text = text.replace(" \'"," ").replace("\' "," ").replace("  "," ")
    text = text.replace("\t\'", " ").replace("  "," ")
    text = text.replace("\t'", " ").replace("  "," ")
    #text = text.replace(",","").replace(".", " ").replace("?"," ").replace("!"," ").replace("\"", "").replace("(", "").replace(")","").replace(" '"," ").replace("' "," ").replace(" \'"," ").replace("\' "," ").replace("  "," ")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

def main():
    #text = "'Death!' I shouted. 'Death is coming! Death!' and leaving him to think about that, I hurried on to Weybridge."
    #text = text.replace(",","").replace(".", " ").replace("?"," ").replace("!"," ").replace("  "," ")
    #text = text.replace("\"", "").replace("(", "").replace(")","").replace("  "," ")
    #text = text.replace(" '"," ").replace("' "," ").replace("  "," ")
    #text = text.replace(" \'"," ").replace("\' "," ").replace("  "," ")
    #text = text.replace("\t\'", " ").replace("  "," ")
    #text = text.replace("\t'", " ").replace("  "," ")

    filename = input("input path to file: ")
    while os.path.exists(filename):
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("count of words: %d" % len(words))
        print("Count of unique words: %d" % len(words_dict))
        with open("frequency.txt", "w") as file:
            for word in words_dict:
                file.write(word)
                file.write("\t")
                file.write(str(words_dict[word]))
                file.write("\n")
        filename = input("input path to file: ")


if __name__ == "__main__":
    main()
