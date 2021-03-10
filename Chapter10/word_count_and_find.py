def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents.lower
        word.lower
        words=contents.count(word)
        print("The word", word, "appears", words, "times in the", filename, "file.")
        
filenames = ['Chapter10/happy.txt','Chapter10/masks.txt','Chapter10/the_voice.txt']
for filename in filenames:
    count_words(filename)
word=input("Enter a word you would like to count in each file: ")
for filename in filenames:
    find_words(filename, word)