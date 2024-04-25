def main():
    filepath = "books/frankenstein.txt"
    text = get_text(filepath)
    word_count = count_words(text)
    print(f"The word count is {word_count}.")


def get_text(filepath):
    with open(filepath) as f:
        return f.read()


def count_words(text):
    return len(text.split())






if __name__ == "__main__":
    main()
