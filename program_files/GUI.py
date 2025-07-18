import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
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

    def add_widgets(self) -> None:
        font = ("Arial", 25)
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
        button_choose_file: tk.Button = tk.Button(
            self.main, text="Wybierz plik", font=font, command=self.choose_file
        )
        button_confirm: tk.Button = tk.Button(
            self.main,
            text="Wygeneruj",
            font=font,
            command=self.generate_cards_pages,
        )
        self.entry_columns: tk.Entry = tk.Entry(self.main, font=font)
        self.entry_ratio: tk.Entry = tk.Entry(self.main, font=font)
        self.entry_footer: tk.Entry = tk.Entry(self.main, font=font)
        self.entry_font_size: tk.Entry = tk.Entry(self.main, font=font)
        self.entry_color: tk.Entry = tk.Entry(self.main, font=font)
        self.entry_text_color: tk.Entry = tk.Entry(self.main, font=font)
        self.entry_columns.insert(0, "5")
        self.entry_ratio.insert(0, "3:4")
        self.entry_footer.insert(0, "stopka")
        self.entry_font_size.insert(0, "43")
        self.entry_color.insert(0, "white")
        self.entry_text_color.insert(0, "black")
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
            row=4,
            column=0,
            rowspan=1,
            columnspan=2,
            sticky="nsew",
            padx=button_pad_x,
            pady=button_pad_y,
        )
        self.entry_columns.grid(
            row=1,
            column=0,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        self.entry_ratio.grid(
            row=1,
            column=1,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        self.entry_footer.grid(
            row=2,
            column=0,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        self.entry_font_size.grid(
            row=2,
            column=1,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        self.entry_color.grid(
            row=3,
            column=0,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )
        self.entry_text_color.grid(
            row=3,
            column=1,
            rowspan=1,
            columnspan=1,
            sticky="nsew",
            padx=entry_pad_x,
            pady=entry_pad_y,
        )

    def generate_cards_pages(self) -> None:
        if self.filename is None:
            messagebox.showinfo("Brakujące dane", "Nie wybrano pliku z tekstami kart.")
            return
        self.page.set_font(int(self.entry_font_size.get()))
        self.page.generate_multiple_pages(
            int(self.entry_columns.get()),
            self.entry_ratio.get(),
            self.entry_color.get(),
            "black",
            self.entry_text_color.get(),
            self.filename,
            self.entry_footer.get(),
        )

    def choose_file(self) -> None:
        desktop_directory: str = os.path.join(
            os.path.join(os.environ["USERPROFILE"]), "Desktop"
        )
        file_path: str = askopenfilename(
            filetypes=[("Pliki tekstowe", "*.txt")],
            initialdir=desktop_directory,
        )
        if file_path is not None:
            self.filename = file_path

    def run(self) -> None:
        self.main.mainloop()
