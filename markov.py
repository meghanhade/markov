#!/usr/bin/env python

import sys
from sys import argv

script, corpus = argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    open_file = open(corpus)

    all_text = open_file.read()

    words = all_text.split()

    stripped_list = []
    

    for word in words:
        stripped_list.append(word)

    markov_chains = {}

    for i in range(len(stripped_list) - 2):
        x = i + 1
        y = i + 2
        tuple_key = stripped_list[i], stripped_list[x]
        value = [stripped_list[y]]

        markov_chains[tuple_key] = markov_chains.get(tuple_key, []) + value

    return markov_chains


# make_chains(corpus)


def make_text(input_dictionary):
    import random
   
    key_list = input_dictionary.keys()
    random_key = random.randrange(len(key_list))
    random_tuple = key_list[random_key]
    letter_list = []
    
    for char in random_tuple[0]:
        letter_list += char
    
    random_key_check = ord(letter_list[0])
    
    while random_key_check > 96:
        key_list = input_dictionary.keys()
        random_key = random.randrange(len(key_list))
        random_tuple = key_list[random_key]
        letter_list = []
        for char in random_tuple[0]:
            letter_list += char
        random_key_check = ord(letter_list[0])

    random_string = random_tuple[0] + " " + random_tuple[1]

    value_list = input_dictionary[random_tuple] #looks up key in dict, returns value

    random_value = random.randrange(len(value_list))

    third_word = value_list[random_value]

    random_string = random_string + " " + third_word


    for i in range(0, 30):

        split_random_string = random_string.split()

        loop_tuple = (split_random_string[-2], split_random_string[-1])

        next_value_list = input_dictionary[loop_tuple]

        new_random_value = random.randrange(len(next_value_list))

        next_word = next_value_list[new_random_value]

        random_string = random_string + " " + next_word

    random_string = random_string.strip(',";:')

    punctuation_list = ["!", ".", "..."]
    random_punctuation = random.randrange(len(punctuation_list))
    punctuation = punctuation_list[random_punctuation]
    
    random_string += punctuation

    return random_string


def main():
    # args = sys.argv
    # import random
    chain_dictionary = make_chains(corpus)

    random_text = make_text(chain_dictionary)

    print random_text

if __name__ == "__main__":
    main()