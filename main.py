import sys
from stats import get_book_text, count_words, word_frequency, chars_dict_to_sorted_list

def print_report(FILE_PATH: str, sorted_char_counts: list[tuple[str, int]]):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {FILE_PATH}...")
	print("----------- Word Count ----------")
	contents = get_book_text(FILE_PATH)
	count = count_words(contents)
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for char_counts in sorted_char_counts:
		if char_counts[0].isalpha():
			print(f"'{char_counts[0]}: {char_counts[1]}'")
		else:
			continue
	print("============= END ===============")

def main():
	#FILE_PATH = "books/frankenstein.txt"
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	FILE_PATH = sys.argv[1]
	contents = get_book_text(FILE_PATH)
	freq = word_frequency(contents)
	sorted_char_counts = chars_dict_to_sorted_list(freq)
	print_report(FILE_PATH, sorted_char_counts)

main()
