from PIL import Image, ImageDraw, ImageFont
import math


class Page:
    def __init__(self) -> None:
        self.page_width: int = 2480
        self.page_height: int = 3508
        self.image: Image = Image.new(
            "RGB", (self.page_width, self.page_height), color="white"
        )
        self.draw: ImageDraw = ImageDraw.Draw(self.image)

    def create_cards(
        self, columns: int, ratio: str, color: str, border_color: str, text_color: str
    ) -> None:
        font = ImageFont.truetype("arial.ttf", 47)
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
                    "Mirus",
                    font=font,
                    fill=text_color,
                )

    def create(self) -> None:
        self.create_cards(5, "3:4", "white", "black", "black")
        self.image.save("karty.png")
