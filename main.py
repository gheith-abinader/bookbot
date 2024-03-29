import re
import os

path_to_file = "./books/frankenstein.txt"
file_contents = None
with open(path_to_file) as f:
	file_contents = f.read()

def cnt_words(book):
	words = book.split()
	return len(words)


def cnt_character_occurence(string):
	chars = re.sub(r"[^a-zA-Z]", "", string)
	chars = chars.lower()
	counter = {}
	for char in chars:
		if char in counter:
			counter[char] = counter[char] + 1
		else:
			counter[char] = 1
	return counter

def sort_print_chars_report(counter):
	def sort_on(dict, key):
		return dict[key]
	
	listed_dicts = [{"letter":key, "count":v} for key, v in counter.items()]
	listed_dicts.sort(key=lambda listed_dict: listed_dict["letter"])
	printout = ["--- Begin report of books/frankenstein.txt ---"]
	printout.append(f"{cnt_words(file_contents)} words found in the document")
	printout.append('')	
	for letterDict in listed_dicts:
		printout.append(f"The '{letterDict['letter']}' character was found {letterDict['count']} times")
	printout.append('--- End report ---')
	return os.linesep.join(printout)

charList = cnt_character_occurence(file_contents)
print(sort_print_chars_report(charList))