import string
from sys import argv

scriptname, filename = argv[0], argv[1]

def create_dictionary(filename):

    input_file = open(filename)
    dictionary = {}
    exclude = string.punctuation

    for line in input_file:
        line = line.rstrip().split(' ')

        for word in line:
            word = word.lower()
#            word = ''.join(char for char in word if char not in exclude)
            word_no_punc = ''

            for char in word:
                if char not in exclude:
                    word_no_punc+=char

            if word_no_punc in dictionary.keys():
                dictionary[word_no_punc] += 1
            else:
                dictionary[word_no_punc] = 1

    return dictionary

def print_dictionary(dictionary):
    for k, v in dictionary.iteritems():
        print k, v

def sort_frequency(dictionary):
    new_dictionary = {}

    words = dictionary.keys()

    for word in words:
        frequency = dictionary[word]

        if frequency in new_dictionary.keys():
            new_dictionary[frequency] += [word]
        else:
            new_dictionary[frequency] = [word]

    return new_dictionary

def sort_alphabetically(new_dictionary):
    for frequency in new_dictionary.keys():
        new_dictionary[frequency].sort()

    return new_dictionary

def print_sort_dictionary(new_dictionary):

    frequencies = new_dictionary.keys()
    sorted_freq = sorted(frequencies, reverse = True)

    for key in sorted_freq:
        for word in new_dictionary[key]:
            print word, key

def main():
    dictionary = create_dictionary(filename)
    #print_dictionary(dictionary)
    new_dictionary = sort_alphabetically(sort_frequency(dictionary))
    print_sort_dictionary(new_dictionary)


if __name__ == '__main__':
    main()


