from stats import get_word_count
from stats import get_char_count, sort_char_count
import sys



#def get_book_text():
   # bookpath = sys.argv[1]
    #with open(bookpath) as f:
        #file_contents = f.read()
        #print(file_contents)



def main():
    if len(sys.argv) > 1:
        bookpath = sys.argv[1]

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}...")
        print("----------- Word Count ----------")
        get_word_count(bookpath)
        print("--------- Character Count -------")

        counts = get_char_count(bookpath)
        sorted_counts = sort_char_count(counts, letters_only=True)
        for ch, n in sorted_counts[:31]:
            if ch == " ":
                label = "SPACE"
            elif ch == "\n":
                label = "NEWLINE"
            else:
                label = ch  # <-- just use the raw character
            print(f"{label}: {n}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()

