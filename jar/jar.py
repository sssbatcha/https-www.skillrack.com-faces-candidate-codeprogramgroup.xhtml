class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity isn't non-negative")

        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self._capacity:
            raise ValueError("Adding more cookies than max capacity")
        elif n < 0:
            raise ValueError("Not enough cookies to remove")

        self._size = n

from fpdf import FPDF

class PDF():
    def __init__(self, txt):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size=48)

        self._pdf.cell(w=0, h=60, txt="CS50 Shirtificate",
                       new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw,
                        alt_text="CS50 Shirtificate")

        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=55, y=140, txt=f"{txt} took CS50")

    def save(self, name):
        self._pdf.output(name)