from fpdf import FPDF


class PDF_Production:
    def PDF(self, pdf_name):
        # save FPDF() class into a variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # change the colour of the text
        pdf.set_text_color(23, 56, 78)

        # set style and size of font
        pdf.set_font("Arial", size=9)

        # create a cell
        pdf.multi_cell(200, 10, txt=pdf_name, align='C')

        # open the text file in read mode
        with open('classification.txt') as f:
            lines = f.read()
            print(lines.split('->'))
            pdf.multi_cell(187.5, 6, txt="Scope: "+lines.split('->')[1])

        # open the text file in read mode
        with open('classification2.txt') as f:
            lines = f.read()
            print(lines.split('->'))
            pdf.multi_cell(187.5, 6, txt="Interest: " + lines.split('->')[1])

        # add another cell
        pdf.cell(200, 10, txt="Summary", ln=1, align='L')

        # create a image
        pdf.image("Most Frequent 10 words.jpeg", 0, 105, w=200)

        # open the text file in read mode
        f = open("summary.txt", "r")

        # insert the texts in pdf
        for x in f:
            pdf.multi_cell(187.5, 6, border=1, txt=x)

        # create a image
        pdf.image("wordcloud.png", 3, 235, w=190)

        # create a image
        pdf.image("Most Frequent 15 Bi-Grams.jpeg", 5, 170, w=100)

        # create a image
        pdf.image("Most Frequent 15 Tri-Grams.jpeg", 105, 170, w=100)

        pdf.output(name=pdf_name+'.pdf')
        print('FINISH:Process Generating PDF Done')


if __name__ == '__main__':
    Output = PDF_Production()
    Output.PDF('19660001637')
