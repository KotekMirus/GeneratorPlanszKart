from PIL import Image


def get_cards_texts(filename: str) -> tuple[int, list[str]]:
    with open(filename, "r", encoding="utf-8") as file:
        cards_texts: list[str] = file.read().split("\n")
        texts_count: int = len(cards_texts)
        return texts_count, cards_texts


def convert_pngs_to_pdf(png_files_list: list[str]) -> None:
    image_list: list[any] = []
    for png_file in png_files_list:
        img: Image = Image.open(png_file).convert("RGB")
        image_list.append(img)
    image_list[0].save("cards.pdf", save_all=True, append_images=image_list[1:])
