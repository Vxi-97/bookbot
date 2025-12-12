import sys
from stats import num_words
from stats import num_characters
from stats import sorted_characters

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()



def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	print("Found " + str(num_words(sys.argv[1])) + " total words")
	#print(num_characters("books/frankenstein.txt"))
	#print(sorted_characters("books/frankenstein.txt"))
	for i in sorted_characters(sys.argv[1]):
		print(f"{i['char']}: {i['num']}")

	
	
main()


