def main():
    path = "books/frankenstein.txt"

    with open(path) as f:
        file_contents = f.read()

    wordCount = countWords(file_contents)
    letterCount = countLetters(file_contents)
    sortedList = dictToList(letterCount)
    printReport(path, wordCount, sortedList)

def countWords(file):
    words = file.split()
    return(len(words))

def countLetters(file):
    letterCount = {}
    list1 = list(file)
    for l in list1:
        lLetter = l.lower()
        if lLetter in letterCount:
            letterCount[lLetter] += 1
        else:
            letterCount[lLetter] = 1
    return (letterCount)

def dictToList(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return(sorted_list)

def sort_on(d):
    return d["num"]

def printReport(path, wordCount, letterCount):
    print(f"--- Report for {path} ---")
    print(f"{wordCount} words found in document")
    for i in letterCount:
        if not i["char"].isalpha():
            continue
        print(f"Letter '{i["char"]}' was used {i["num"]} times")
    


main()