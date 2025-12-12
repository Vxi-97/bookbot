def num_words(path_to_file):
	with open(path_to_file) as f:
		text = f.read()
	words = text.split()
	return len(words)

def num_characters(path_to_file):
	with open(path_to_file) as f:
		text = f.read()
	chars = list(text.lower())
	characters = dict.fromkeys(chars)
	for key in characters:
		characters[key] = chars.count(key)
	return characters

def sort_on(items):
	return items["num"]


def sorted_characters(path_to_file):
	sorted_chars = []
	characters = num_characters(path_to_file)
	for key in characters:
		character = {"char": key, "num": characters[key]}
		sorted_chars.append(character)
	sorted_chars.sort(reverse=True, key=sort_on)
	return sorted_chars
