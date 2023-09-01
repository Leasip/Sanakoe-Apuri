import pyperclip
import re
import time
import os
from difflib import SequenceMatcher
# Get the directory of the executed script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the script's directory
file_path = os.path.join(script_dir, 'sanat.txt')

# Open the file for reading with utf-8 encoding
with open(file_path, encoding='utf-8') as input_file:
    sanat = input_file.read()
    lines = input_file.readlines()

#pharse sanat to list
spellingremove = re.sub('/.*?/', "00", sanat)

#replace \n0\n with \n
testi = re.sub(r'\n00\n', ':', spellingremove)

#replace \n: with :
testi2 = re.sub(r'\n:', ':', testi)

#make two way dict pair devided by :
testi33 = re.sub(r':\n', ':', testi2)
testi3 = testi33.replace(", ", ",")

#remove all empty lines from testi3
lines = testi3.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]
word_translations = "\n".join(non_empty_lines).replace(", ", "")
#print(word_translations)

while True:
    pyperclip.waitForNewPaste()
    clipboard = pyperclip.paste()
    search_string = clipboard

    best_match = None
    best_similarity = 0

    for line in word_translations.splitlines():
        word, translation = line.split(':')
        similarity_word = SequenceMatcher(None, search_string, word).ratio()
        similarity_translation = SequenceMatcher(None, search_string, translation).ratio()
        if similarity_word > best_similarity:
            best_similarity = similarity_word
            best_match = translation
        if similarity_translation > best_similarity:
            best_similarity = similarity_translation
            best_match = word

    if best_match is not None:
        print(best_match)
        pyperclip.copy(best_match)

    #wait for next copy
    time.sleep(1)
