from sys import argv

scriptname, filename = argv[0], argv[1]

def create_dictionary(filename):

    input_file = open(filename)

    dictionary = {}

    for line in input_file:
        line = line.rstrip().split(' ')

        for word in line:
            if word in dictionary.keys():
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return dictionary

def print_dictionary(dictionary):
    for k, v in dictionary.iteritems():
        print k, v

def main():
    dictionary = create_dictionary(filename)
    print_dictionary(dictionary)


if __name__ == '__main__':
    main()


