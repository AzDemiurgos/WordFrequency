import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import Accelerate_Py
import module1

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
    #from Accelerate_Py import Accelerate_Py_Func
    l_value = [1,2,3,4]
    l_lambda = [1,2,3,4, 5, 6]
   # dummy = Accelerate_Py_Func(np.asarray(l_lambda), np.asarray(l_value), 5);

    from module1 import example
    dummy = example(l_value, l_lambda)
    dummy = "fsdfds"

    filename = input("input path to file: ")
    dummy = example(l_lambda, l_value)
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
