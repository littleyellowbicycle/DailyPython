import io

file = open("words.txt", "r", encoding="utf-8")
wordlist = file.readlines()

while (True):
    stdin = input()
    if (stdin in wordlist):
        print("freedom")
    elif (stdin == "exit"):
        break
    else:
        print("manrights")