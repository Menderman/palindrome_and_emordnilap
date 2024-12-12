import sys

def isEmordnilap(word, all_words):
    word=word.lower()
    word2 = word[::-1]
    if word != word2 and word2 in all_words:
        return True
    else:
        return False


if len(sys.argv) < 3:
        print("Usage: python emordnilap.py <words_name> <dictionary_name>")
        sys.exit(1)

words = sys.argv[1]
dictionary = sys.argv[2]


all_words = set()
with open(dictionary, 'r') as file:
    for word in file:
        all_words.add(word.strip().lower())

print("Emordnilap words:")
with open(words, 'r') as file:
    for word in file:
        word=word.strip().lower()
        word2=word[::-1]
        #print(word)
        if(isEmordnilap(word,all_words)):
            print(word)