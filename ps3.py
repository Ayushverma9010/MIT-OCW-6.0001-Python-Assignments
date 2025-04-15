# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: ayush
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.
import string
import math

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split()

### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    """
    freq_dict = {}
    for item in input_iterable:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    freq_dict = {}
    for letter in word:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    return freq_dict

### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other
    """
    diff = 0
    all_freq = 0

    # Collect all unique keys (letters or words)
    all_keys = set(freq_dict1.keys()).union(set(freq_dict2.keys()))

    # Calculate the difference and total frequencies
    for key in all_keys:
        freq1 = freq_dict1.get(key, 0)
        freq2 = freq_dict2.get(key, 0)
        diff += abs(freq1 - freq2)
        all_freq += max(freq1, freq2)

    similarity = 1 - (diff / all_freq)
    return round(similarity, 2)

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries
    """
    combined_freq = {}

    # Combine frequencies from both dictionaries
    for word, freq in freq_dict1.items():
        combined_freq[word] = combined_freq.get(word, 0) + freq
    for word, freq in freq_dict2.items():
        combined_freq[word] = combined_freq.get(word, 0) + freq

    # Find the maximum frequency
    max_freq = max(combined_freq.values())

    # Get all words that have the maximum frequency
    most_frequent_words = [word for word, freq in combined_freq.items() if freq == max_freq]

    return sorted(most_frequent_words)

### Problem 5: Find TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF
    """
    text = load_file(file_path)
    words = text_to_list(text)
    word_freq = get_frequencies(words)
    total_words = len(words)
    
    tf_dict = {word: freq / total_words for word, freq in word_freq.items()}
    return tf_dict

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF
    """
    total_documents = len(file_paths)
    word_document_count = {}

    for file_path in file_paths:
        text = load_file(file_path)
        words = set(text_to_list(text))
        for word in words:
            word_document_count[word] = word_document_count.get(word, 0) + 1

    idf_dict = {word: math.log10(total_documents / count) for word, count in word_document_count.items()}
    return idf_dict

def get_tfidf(tf_file_path, idf_file_paths):
    """
    Args:
        tf_file_path: name of file in the form of a string (used to calculate TF)
        idf_file_paths: list of names of files, where each file name is a string
                        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.
    """
    tf_dict = get_tf(tf_file_path)
    idf_dict = get_idf(idf_file_paths)
    
    tfidf_scores = []
    for word, tf in tf_dict.items():
        idf = idf_dict.get(word, 0)  # Default to 0 if word not in IDF
        tfidf = tf * idf
        tfidf_scores.append((word, tfidf))

    # Sort by TF-IDF and then alphabetically if tied
    return sorted(tfidf_scores, key=lambda x: (x[1], x[0]))

if __name__ == "__main__":
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
