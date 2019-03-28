import os


def GetWords(filepath):
    words = []
    if (os.path.exists(filepath)):
        with open(filepath, "r", encoding="utf-8") as file:
            print("log--->open file successfully")
            while (True):
                line = file.readline()
                if (line != ""):
                    words.append(line.strip())
                else:
                    break
            print(words)
            return words
    pass


def filter(words, stdin):
    if (words == []):
        print("words list is null")
    if stdin:
        for word in words:
            if (stdin.find(word) > -1):
                print("find word in input")
                stdin = stdin.replace(word, "**")
        print(stdin)
    else:
        print("no chars input")
    pass


def main():
    stdin = input("enter your sentence: ")
    filter(GetWords("words.txt"), stdin)
    pass


if __name__ == '__main__':
    main()
