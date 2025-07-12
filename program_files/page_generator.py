from PIL import Image, ImageDraw, ImageFont
import files_handling as fh
import math


class Page:
    def __init__(self) -> None:
        self.page_width: int = 2480
        self.page_height: int = 3508
        self.font = ImageFont.truetype("arial.ttf", 47)
        self.image: Image = Image.new(
            "RGB", (self.page_width, self.page_height), color="white"
        )
        self.draw: ImageDraw = ImageDraw.Draw(self.image)

    def create_cards(
        self, columns: int, ratio: str, color: str, border_color: str, text_color: str
    ) -> bool:
        margin: int = 90
        space: int = 10
        width_multiplier: float = 1
        height_multiplier: float = 1
        new_height_multiplier: float = 1
        card_width: int = int(
            (self.page_width - 2 * margin - (columns - 1) * space) / columns
        )
        width_multiplier = float(ratio[: ratio.find(":")])
        height_multiplier = float(ratio[ratio.find(":") + 1 :])
        new_height_multiplier = height_multiplier / width_multiplier
        card_height: int = int(card_width * new_height_multiplier)
        rows: int = math.floor((self.page_height - 2 * margin) / (card_height + space))
        finished: bool = False
        for row in range(rows):
            for column in range(columns):
                self.draw.rectangle(
                    [
                        (
                            margin + (card_width + space) * column,
                            margin + (card_height + space) * row,
                        ),
                        (
                            margin - space + (card_width + space) * (column + 1),
                            margin - space + (card_height + space) * (row + 1),
                        ),
                    ],
                    fill=color,
                    outline=border_color,
                    width=5,
                )
                self.draw.text(
                    (
                        margin + (card_width + space) * column + 15,
                        margin + (card_height + space) * row + 15,
                    ),
                    self.all_texts[self.texts_count],
                    font=self.font,
                    fill=text_color,
                )
                if self.texts_count < self.all_texts_number - 1:
                    self.texts_count += 1
                else:
                    finished = True
                    break
            if finished:
                break
        return finished

    def generate_multiple_pages(
        self,
        columns: int,
        ratio: str,
        color: str,
        border_color: str,
        text_color: str,
        filename: str,
    ) -> None:
        self.all_texts_number: int = 0
        self.all_texts: list[str] = []
        self.all_texts_number, self.all_texts = fh.get_cards_texts(filename)
        self.texts_count: int = 0
        page_count: int = 1
        finished: bool = False
        while not finished:
            self.image: Image = Image.new(
                "RGB", (self.page_width, self.page_height), color="white"
            )
            self.draw: ImageDraw = ImageDraw.Draw(self.image)
            finished = self.create_cards(
                columns,
                ratio,
                color,
                border_color,
                text_color,
            )
            new_filename = "karty" + str(page_count) + ".png"
            self.image.save(new_filename)
            page_count += 1
