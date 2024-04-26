def main():
    filepath = "books/frankenstein.txt"
    text = get_text(filepath)
    word_count = count_words(text)
    characters = count_characters(text)
    sorted_characters = make_sorted_chars_list(characters)

    print("--- Begin report ---")
    print(f"The word count is {word_count}.")
    for char in sorted_characters:
        print(f"{char["character"]} was found {char["count"]} times.")
    print("--- End report ---")


def get_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict:
    characters = {}
    for c in text.lower():
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters


def make_sorted_chars_list(d: dict) -> list:
    list_of_dicts = []
    for i in d:
        if i.isalpha():
            list_of_dicts.append({"character" : i, "count": int(d[i])})

    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts


def sort_on(d):
    return d["count"]


if __name__ == "__main__":
    main()
