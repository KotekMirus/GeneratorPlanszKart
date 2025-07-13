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
        padding: int = 7
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
                self.add_text_to_card(
                    self.all_texts[self.texts_count],
                    text_color,
                    card_width,
                    (
                        margin + (card_width + space) * column + padding,
                        margin + (card_height + space) * row + padding,
                    ),
                )
                if self.texts_count < self.all_texts_number - 1:
                    self.texts_count += 1
                else:
                    finished = True
                    break
            if finished:
                break
        return finished

    def add_text_to_card(
        self, text: str, text_color: str, card_width: int, top_left_corner: tuple[int]
    ) -> None:
        dummy_img = Image.new("RGB", (self.page_width, self.page_height))
        draw = ImageDraw.Draw(dummy_img)
        lines: list[str] = []
        words: list[str] = text.split()
        current_line: str = ""
        for word in words:
            test_line: str = current_line + (" " if current_line else "") + word
            bbox: tuple[int] = draw.textbbox(top_left_corner, test_line, font=self.font)
            line_width: int = bbox[2] - bbox[0]
            if line_width <= card_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        ref_bbox: tuple[int] = draw.textbbox((0, 0), "Ay", font=self.font)
        line_height: int = (ref_bbox[3] - ref_bbox[1]) + 5
        y: int = top_left_corner[1]
        for line in lines:
            self.draw.text(
                (top_left_corner[0], y), line, font=self.font, fill=text_color
            )
            y += line_height

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
        png_files_list: list[str] = []
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
            new_filename = "cards" + str(page_count) + ".png"
            self.image.save(new_filename)
            png_files_list.append(new_filename)
            page_count += 1
        fh.convert_pngs_to_pdf(png_files_list)
