def get_cards_texts(filename: str) -> tuple[int, list[str]]:
    with open(filename, "r") as file:
        cards_texts: list[str] = file.read().split("\n")
        texts_count: int = len(cards_texts)
        return texts_count, cards_texts
