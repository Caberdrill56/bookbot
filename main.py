def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = 0
        for word in file_contents.split():
            words += 1
        print(words)
        print(countCharacter(file_contents))
        report(words, sorted_list(countCharacter(file_contents)))

def countCharacter(text):
    lowertext = text.lower()
    CharDict = {}
    for char in lowertext:
        if char in CharDict:
            CharDict[char] += 1
        else:
            CharDict[char] = 1
    return CharDict

def sort_on(d):
    return d["num"]

def sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(count_word, chars_sorted_list):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_word} words found in the document")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    



if __name__ == "__main__":
    main()