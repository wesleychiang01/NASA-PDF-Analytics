from pdf2image import convert_from_path
from pytesseract import image_to_string


# QUALITY OF TEXT NOT SO EFFICIENT
def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file, poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')


def convert_image_to_text(file):
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += convert_image_to_text(img)
        # print("Page n°{}".format(pg))
        # print(convert_image_to_text(img))
    return final_text


if __name__ == '__main__':
    path_to_pdf = 'corpus/19660001637.pdf'
    tesseract_text = (get_text_from_any_pdf(path_to_pdf))

    file = open("parsed.txt", "w")
    file.write(tesseract_text)
    file.close