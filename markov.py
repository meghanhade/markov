#!/usr/bin/env python

#all imports go at the top
from sys import argv

script, corpus = argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    open_file = open(corpus)
    all_text = open_file.read()
    words = all_text.split()
    markov_chains = {}
    
    # this creates a key that is a tuple of the first two words in the word list.
    # it then creates a value for that key that is the third word in the word list.
    for first_word in range(len(words) - 2):
        second_word = first_word + 1
        first_value = first_word + 2
        tuple_key = words[first_word], words[second_word]
        value = [words[first_value]]
        # the line below adds the new key value pair to the markov-chains dictionary
        markov_chains[tuple_key] = markov_chains.get(tuple_key, []) + value

    return markov_chains


# make_chains(corpus)


def make_text(input_dictionary):
    import random
   

    # key_list establishes a list of the keys in the markov_chains dictionary.
    # random_key chooses a random number from the list of numbers that
    # is the length of the key_list.
    # random_tuple finds the value associated with the key in the key_list at the 
    # index of the random number.
    # letter_list establishes an empty list for later use.

    key_list = input_dictionary.keys()
    random_key = random.randrange(len(key_list))
    random_tuple = key_list[random_key]
    letter_list = []
    
    
    # random_key_check makes sure the first word of the random_string is capitalized.
    # anther approach would have been to capitalize the first character of
    # the first word of the random_string
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

    # this range sets the length of the sentence by number of words.
    # this loop takes the random string and creates a list of the words it contains.
    # it then takes the last two words of that string to use as the next tuple key.
    # from the values available for this new tuple, a random value is
    # selected and added as the next word in the random_string.
    for i in range(0, 30):
        split_random_string = random_string.split()
        loop_tuple = (split_random_string[-2], split_random_string[-1])
        next_value_list = input_dictionary[loop_tuple]
        new_random_value = random.randrange(len(next_value_list))
        next_word = next_value_list[new_random_value]
        random_string = random_string + " " + next_word

    # strips unwanted punctuation and chooses a random punctuation to 
    # end the sentence.
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