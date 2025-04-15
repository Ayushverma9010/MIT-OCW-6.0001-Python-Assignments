# Problem Set 4C
# Name:ayush
# Collaborators:

import json
import ps4b  # Importing your work from Part B


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    best_pad = None
    best_decryption = None
    max_valid_words = 0
    
    for pad in pads:
        decrypted_message = ciphertext.decrypt_message(pad)
        decrypted_text = decrypted_message.get_text().split()
        
        valid_words = sum(1 for word in decrypted_text if is_word(word_list, word))
        
        if valid_words >= max_valid_words:
            max_valid_words = valid_words
            best_pad = pad
            best_decryption = decrypted_message

    return best_decryption


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story
    '''
    encrypted_text = get_story_string()
    pads = get_story_pads()
    encrypted_message = ps4b.EncryptedMessage(encrypted_text)
    
    decrypted_message = decrypt_message_try_pads(encrypted_message, pads)
    
    return decrypted_message.get_text()


if __name__ == '__main__':
    # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
