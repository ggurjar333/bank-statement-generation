from statistics import mean

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import itertools
from random import randint


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


class PDFGenerator:
    def __init__(self, filename, data):
        self.filename = filename
        self.c = canvas.Canvas(self.filename, pagesize=A4)
        self.w, self.h = A4
        self.max_rows_per_page = 45
        self.x_offset = 50
        self.y_offset = 50
        self.padding = 15
        self.xlist = [x + self.x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
        self.ylist = [self.h - self.y_offset - i * self.padding for i in range(self.max_rows_per_page + 1)]
        self.data = data

    def draw_grid(self):
        rows = self.data
        self.c.grid(self.xlist, self.ylist[:len(rows) + 1])

    def draw_data(self, rows):
        for y, row in zip(self.ylist[:-1], rows):
            for x, cell in zip(self.xlist, row):
                self.c.drawString(x + 2, y - self.padding + 3, str(cell))

    def generate_pdf(self):
        for rows in grouper(self.data, self.max_rows_per_page):
            rows = tuple(filter(bool, rows))
            self.draw_grid()
            self.draw_data(rows)
            self.c.showPage()

        self.c.save()


# data = [("NAME", "GR. 1", "GR. 2", "GR. 3", "AVG", "STATUS")]
#
# for i in range(1, 20):
#     exams = [randint(0, 10) for _ in range(3)]
#     avg = round(mean(exams), 2)
#     state = "Approved" if avg >= 4 else "Disapproved"
#     data.append((f"Student {i}", *exams, avg, state))
#
# print(data)
# pdf_generator = PDFGenerator("grid-students.pdf", data=data)
# pdf_generator.generate_pdf()