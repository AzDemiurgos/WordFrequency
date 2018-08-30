import os
import sys
#import module1

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
    text = text.replace("-", " ").replace("  "," ")
    text = text.replace(":", " ").replace("  "," ")
    text = text.replace(";", " ").replace("  "," ")

    #text = text.replace(",","").replace(".", " ").replace("?"," ").replace("!"," ").replace("\"", "").replace("(", "").replace(")","").replace(" '"," ").replace("' "," ").replace(" \'"," ").replace("\' "," ").replace("  "," ")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word[0] < 'a':
            continue
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
    #from Accelerate_Py import Accelerate_Py_Func
   
    filename = input("input path to file: ")
    filename = "E:\Azat\Python\WebParser\GoT\GoT_s__e_.text"
    while os.path.exists(filename):
        words = get_words(filename)
        words_dict = get_words_dict(words)
        from collections import OrderedDict
        from operator import itemgetter
        words_dict = OrderedDict(sorted(words_dict.items(), key=itemgetter(1), reverse=True))
        #words_dict = sorted(words_dict, key=lambda x:x[1], reverse=True)
        print("count of words: %d" % len(words))
        print("Count of unique words: %d" % len(words_dict))
        with open("E:\\Azat\\Python\\WebParser\\GoT\\frequency.txt", "w") as file:
            for word in words_dict:
                file.write(word)
                file.write("\t")
                file.write(str(words_dict[word]))
                file.write("\n")
        filename = input("input path to file: ")


if __name__ == "__main__":
    main()
