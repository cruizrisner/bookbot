




def get_word_count(filepath):
    with open(filepath) as f:
        text = f.read()
        word_count = len(text.split())
        print(f"Found {word_count} total words")


def get_char_count(filepath):
    with open(filepath) as f:
        text = f.read().lower()

    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def sort_char_count(char_count, letters_only=False):
    if letters_only:
        # Filter dictionary to only include alphabetic keys
        char_count = {ch: n for ch, n in char_count.items() if ch.isalpha()}
    
    # Sort descending by count
    return sorted(char_count.items(), key=lambda kv: kv[1], reverse=True)




