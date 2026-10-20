def sort_on(vehicle: tuple[str, int]) -> int:
    return vehicle[1]

def chars_dict_to_sorted_list(freq: dict[str, int]) -> list[tuple[str, int]]:
	char_count = []
	for key, value in freq.items():
		tup = (key, value)
		char_count.append(tup)
	sorted_char_counts = sorted(char_count, reverse=True, key=sort_on)
	return sorted_char_counts

def get_book_text(FILE_PATH: str) -> str:
        with open(FILE_PATH) as f:
                file_contents = f.read()
        return file_contents

def count_words(contents: str) -> int:
        words = contents.split()
        return len(words)

def word_frequency(contents: str):
	freq = {}
	for i in contents:
		if i.lower() not in freq:
			freq[i.lower()] = 1
		else:
			freq[i.lower()] +=1
	return freq

def main():
        #print(get_book_text("books/frankenstein.txt"))
        contents = get_book_text("books/frankenstein.txt")
        num_words = count_words(contents)
        #print(f"Found {num_words} total words")

main()
