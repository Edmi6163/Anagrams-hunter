import nltk
from collections import defaultdict

def compute_letter_distribution(word):
    return nltk.FreqDist(word.lower())

def angram_search(dictionary):
    anagram_dict = defaultdict(list)

    for word in dictionary:
        letter_distribution = compute_letter_distribution(word)
        anagram_dict[str(letter_distribution)].append(word)

    return anagram_dict

if __name__ == "__main__":
    # Type your dictionary path
    file_path = " "

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)

    print("Total words loaded:", len(words))

    word = input("Enter the first word: ").lower()

    letter_distribution_input = compute_letter_distribution(word)
    anagram_dict = angram_search(words)

    anagrams = anagram_dict.get(str(letter_distribution_input), [])

    if anagrams:
        print("Anagrams found:")
        for anagram in anagrams:
            print(anagram)
    else:
        print("No anagrams found.")
