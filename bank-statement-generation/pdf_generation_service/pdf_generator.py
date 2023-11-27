import itertools
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

def preprocess(self):
    if not self.data:
        return []
    headers = tuple(self.data[0].keys())
    values = [tuple(entry.values()) for entry in self.data]
    preprocessed_data = [headers] + values
    return preprocessed_data    

class PDFGenerator:
    def __init__(self, filename, data):
        self.filename = filename
        self.c = canvas.Canvas(self.filename, pagesize=A4)
        self.w, self.h = A4
        self.max_rows_per_page = 45
        self.x_offset = 50
        self.y_offset = 50
        self.padding = 15
        self.xlist = [x + self.x_offset for x in [0, 200, 250]]      
        self.ylist = [self.h - self.y_offset - i * self.padding for i in range(self.max_rows_per_page + 1)]
        self.data = data

    def draw_grid(self, data):
        rows = data
        self.c.grid(self.xlist, self.ylist[:len(rows) + 1])

    def draw_data(self, rows):
        for y, row in zip(self.ylist[:-1], rows):
            for x, cell in zip(self.xlist, row):
                self.c.drawString(x + 2, y - self.padding + 3, str(cell))

    def generate_pdf(self):
        data = preprocess(self)
        for rows in grouper(data, self.max_rows_per_page):
            rows = tuple(filter(bool, rows))
            self.draw_grid(data)
            self.draw_data(rows)
            self.c.showPage()

        self.c.save()