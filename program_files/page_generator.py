from PIL import Image, ImageDraw, ImageFont


class Page:
    def __init__(self) -> None:
        self.page_width: int = 2480
        self.page_height: int = 3508
        self.image: Image = Image.new(
            "RGB", (self.page_width, self.page_height), color="white"
        )
        self.draw: ImageDraw = ImageDraw.Draw(self.image)

    def create_cards(self, columns, ratio) -> None:
        margin: int = 30
        space: int = 15
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
        print(new_height_multiplier)
        print(card_width, card_height)
        # self.draw.text((10, 40), "Hello PNG!", fill="black")

    def create(self) -> None:
        self.create_cards(5, "3:4")
        self.image.save("karty.png")
