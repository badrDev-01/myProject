import random


def load_flashcards():
    with open("flashcards_data.txt", "r") as f:
        cards = [line.strip().split(" - ") for line in f.readlines()]
    return cards


def quiz():
    cards = load_flashcards()
    random.shuffle(cards)

    for term, definition in cards:
        answer = input(f"What is '{term}'? ")
        print(f"Correct Answer: {definition}\n")


if __name__ == "__main__":
    quiz()