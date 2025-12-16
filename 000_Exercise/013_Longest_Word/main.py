def longest_word(string):
    words = string.split()
    cleaned_words = [''.join(char for char in word if char.isalnum()) for word in words]
    longest = max(cleaned_words, key=len)
    return longest


string = "fun&!! time"
print(longest_word(string))
