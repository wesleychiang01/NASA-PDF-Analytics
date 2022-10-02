import os
import string
from os.path import basename, splitext
from statistical_analysis import Statistics
from summary_text import Text_analysis
from pdf_production import PDF_Production
from nltk.tokenize import word_tokenize
import contractions
import enchant
import fitz
import nltk.corpus
import nltk.data
import xlsxwriter
from nltk.corpus import stopwords
from spellchecker import SpellChecker

eng_dict = enchant.Dict("en_US")


class Company_Report:
    def open_pdf(self, directory):
        i = 0

        for pdf_file in os.listdir(directory):
            i += 1

            report_name = pdf_file.split(".")
            latest_name = report_name[0]
            print(latest_name)

            self.pdf_name = splitext(basename(latest_name))[0]
            self.source_file_name = pdf_file
            self.doc = fitz.open(directory + '/' + pdf_file)

            self.start_page = 0
            self.stop_page = len(self.doc)
            print(len(self.doc))

            total_page = 0

            text = ""

            for page in range(self.start_page, self.stop_page):
                wanted_page = self.doc.load_page(page)
                text += wanted_page.get_text()
                total_page += 1

            # Lower down case
            words = text.lower().split()
            self.remove_punctuation(words)

    def remove_punctuation(self, words):
        # Remove Punctuation
        table = str.maketrans('', '', string.punctuation)
        no_punct = [w.translate(table) for w in words]
        text_no_punct = " ".join(no_punct)

        punc = '''¢£'''
        text_no_punct2 = " "
        for ele in text_no_punct:
            if ele not in punc:
                text_no_punct2 += ele

        # Remove Number & Extra Space
        text_no_num = ''.join([i for i in text_no_punct2 if not i.isdigit()])
        text_parsed = " ".join(text_no_num.split())
        # print(text_parsed)

        # Text Contraction
        contrated_text = contractions.fix(text_parsed)
        print('Step1:' + contrated_text)

        self.remove_Stop_words(contrated_text)

    def remove_Stop_words(self, text):
        stoplist = set(stopwords.words("english"))
        removed_stopwords_text = " ".join([word for word in text.split() if word not in stoplist])
        print('Step2:' + removed_stopwords_text)

        self.lemmatize_tokens(removed_stopwords_text)
        # self.spellcorrect_tokens(removed_stopwords_text)

    # TEXT Lemmatizer
    def lemmatize_tokens(self, text):
        tokens = text.lower().split()
        lemmatizer = nltk.stem.WordNetLemmatizer()
        tokens_new = [lemmatizer.lemmatize(token) for token in tokens]
        self.text_parsed = " ".join(tokens_new)
        print('Step3:' + self.text_parsed)

        self.spellcorrect_tokens(self.text_parsed)

    # TEXT Stemming (eg.trouble > troubl) # SKIP
    def stem_tokens(self, text):
        tokens = text.lower().split()
        stemmer = nltk.stem.PorterStemmer()
        tokens_new = [stemmer.stem(token) for token in tokens]
        text_parsed = " ".join(tokens_new)
        print(text_parsed)

    # TOKEN Autocorrect
    def spellcorrect_tokens(self, text):
        # tokens = text.lower().split()
        # spell = SpellChecker()
        # text_parsed = ' '.join([spell.correction(word) for word in tokens])
        threshold = 1

        words = word_tokenize(text)
        text_parsed = ' '.join([word for word in words if len(word) > threshold])
        print('Step4:' + text_parsed)

        file = open("parsed.txt", "w")
        file.write(text_parsed)
        file.close

        text_summary = f'{text:19400.19400}'
        a = Statistics()
        a.wordcloud(text_parsed)

        b = Text_analysis("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")
        b.get_summary(text_summary)

        c = PDF_Production()
        c.PDF(self.pdf_name)

    # DECIDED NOT TO DO WORD SEGMENTATION
    def segment_str(self, chars, exclude=None):
        words = []

        if not chars.isalpha():  # don't check punctuation etc.; needs more work
            return [chars]

        if not exclude:
            exclude = set()

        working_chars = chars
        while working_chars:
            # iterate through segments of the chars starting with the longest segment possible
            for i in range(len(working_chars), 1, -1):
                segment = working_chars[:i]
                if eng_dict.check(segment) and segment not in exclude:
                    words.append(segment)
                    working_chars = working_chars[i:]
                    break
            else:  # no matching segments were found
                if words:
                    exclude.add(words[-1])
                    return self.segment_str(chars, exclude=exclude)
                # let the user know a word was missing from the dictionary,
                # but keep the word
                print('"{chars}" not in dictionary (so just keeping as one segment)!'
                      .format(chars=chars))
                return [chars]
        # return a list of words based on the segmentation
        return words

    def insert_excel(self, text):
        wb = xlsxwriter.Workbook("Excel1.xlsx")
        ws = wb.add_worksheet()
        row = 0
        col = 0
        for line in text:
            ws.write(row, col, line)
            row += 1
            col = 0

        wb.close()


if __name__ == '__main__':
    Output = Company_Report()
    Output.open_pdf('corpus')



