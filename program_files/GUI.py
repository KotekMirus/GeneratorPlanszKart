import tkinter as tk
from tkinter import ttk
import page_generator


class MainWindow:
    def __init__(self):
        self.filename: str | None = None
        self.page: page_generator.Page = page_generator.Page()
        self.main: tk.Tk = tk.Tk()
        self.window_width: int = 650
        self.window_height: int = 650
        self.main.geometry("{0}x{1}".format(self.window_width, self.window_height))
        self.main.title("Generator Plansz Kart")
        self.main.configure(background="#26021e")
        for i in range(6):
            self.main.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.main.grid_columnconfigure(i, weight=1)
        self.add_widgets()

    def add_widgets(self):
        button_pad_x: tuple[float, float] = (
            0.1462 * self.window_width,
            0.1462 * self.window_width,
        )
        button_pad_y: tuple[float, float] = (
            0.0346 * self.window_height,
            0.0346 * self.window_height,
        )
        entry_pad_x: tuple[float, float] = (
            0.0462 * self.window_width,
            0.0462 * self.window_width,
        )
        entry_pad_y: tuple[float, float] = (
            0.0308 * self.window_height,
            0.0308 * self.window_height,
        )
        big_entry_pad_x: tuple[float, float] = (
            0.0462 * self.window_width,
            0.0462 * self.window_width,
        )
        big_entry_pad_y: tuple[float, float] = (
            0.0308 * self.window_height,
            0.0308 * self.window_height,
        )
        combobox_pad_x: tuple[float, float] = (
            0.0769 * self.window_width,
            0.0769 * self.window_width,
        )
        combobox_pad_y: tuple[float, float] = (
            0.0308 * self.window_height,
            0.0308 * self.window_height,
        )
        button_choose_file: tk.Button = tk.Button(
            self.main, text="Wybierz plik", command=None
        )
        button_confirm: tk.Button = tk.Button(
            self.main,
            text="Wygeneruj",
            command=lambda: self.page.generate_multiple_pages(
                5, "3:4", "white", "black", "black", "C:/Users/kozde/Desktop/test.txt"
            ),
        )
        entry_rows: tk.Entry = tk.Entry(self.main)
        entry_columns: tk.Entry = tk.Entry(self.main)
        entry_color: tk.Entry = tk.Entry(self.main)
        entry_ratio: tk.Entry = tk.Entry(self.main)
        entry_footer: tk.Entry = tk.Entry(self.main)
        combobox_font: ttk.Combobox = ttk.Combobox()
        combobox_font_size: ttk.Combobox = ttk.Combobox()
        button_choose_file.grid(
            row=0,
            column=0,
            rowspan=1,
            columnspan=2,
            sticky="nsew",
            padx=button_pad_x,
            pady=button_pad_y,
        )
        button_confirm.grid(
            row=5,
            column=0,
            rowspan=1,
            columnspan=2,
            sticky="nsew",
            padx=button_pad_x,
            pady=button_pad_y,
        )
        entry_rows.grid(
            row=1,
            column=0,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        entry_columns.grid(
            row=1,
            column=1,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        entry_color.grid(
            row=2,
            column=0,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        entry_ratio.grid(
            row=2,
            column=1,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        entry_footer.grid(
            row=4,
            column=0,
            rowspan=1,
            columnspan=2,
            sticky="nsew",
            padx=big_entry_pad_x,
            pady=big_entry_pad_y,
        )
        combobox_font.grid(
            row=3,
            column=0,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=combobox_pad_x,
            pady=combobox_pad_y,
        )
        combobox_font_size.grid(
            row=3,
            column=1,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=combobox_pad_x,
            pady=combobox_pad_y,
        )

    def run(self):
        self.main.mainloop()
