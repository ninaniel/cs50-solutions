from fpdf import FPDF

# by default, a FPDF document has a A4 format with portrait orientation
class PDF(FPDF):

    # creating title of pdf file, centered horizontally.
    def header(self):
        self.set_font("helvetica", "B", 44)
        self.cell(0, 40, "CS50 Shirtificate",  center = True, align="C")

    # adding image of <I Took CS50 T-shirt>; I - customized with a user_name.
    def shirtificate(self, shirt = "shirtificate.png"):
        self.name = "I"
        self.add_page()

        # w=pdf.epw >> adjusting image width to fit the pdf file width
        self.image(shirt, w=self.epw, x="C", y=60)

        self.set_font("helvetica", "B", 24)
        self.set_text_color(r = 255, g=255, b=255)

        # setting Ypos for cursor to adjust text on t-shirt
        self.set_y(120)
        self.cell(text=f"{self.name} took CS50!", center = True, align = "C")


    @property
    def name(self):
        return self._name

    # prompting name from user; name remains "I" if user inputs empty string
    @name.setter
    def name(self,name):
        self._name = input("Name: ").title()
        if not self._name:
            self._name = name


pdf = PDF()
pdf.shirtificate()
pdf.output("shirtificate.pdf")