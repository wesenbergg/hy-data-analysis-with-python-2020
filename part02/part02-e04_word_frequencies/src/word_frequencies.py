#!/usr/bin/env python3

#cwd: hy/hy-data-analysis-with-python-2020/part02-e02_file_listing/
def word_frequencies(filename):
    with open(filename, 'r') as f:
        dictionary = {}
        words = f.read().split()
        for word in words:
            word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
            if word not in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1
    
    return dictionary

def main():
    print(word_frequencies("hy/hy-data-analysis-with-python-2020/part02-e04_word_frequencies/src/alice.txt"))

if __name__ == "__main__":
    main()
