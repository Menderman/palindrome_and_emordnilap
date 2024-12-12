import sys
def isPalindrome(word):
    word=word.lower()
    word2 = word[::-1]
    if(word == word2):
        return True
    else:
        return False

# if(isPalindrome("radar")):
#     print("true")
if len(sys.argv) < 2:
        print("Usage: python palindrome.py <words_name>")
        sys.exit(1)

file_name = sys.argv[1]

print("Palindrome words:")
with open(file_name, 'r') as file:
    for word in file:
        word=word.strip().lower()
        #print(word)
        if(isPalindrome(word)):
            print(word)