import openai

openai.api_key = "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"


class Text_analysis:
    def __init__(self, api_key):
        self.summary = []
        self.classify = []
        openai.api_key = api_key

    def get_summary(self, cleaned_text):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Summarize the following report very concisely:\n\n" + cleaned_text + "\nCONCISE SUMMARY:",
            temperature=0.70,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        self.summary = response['choices'][0]['text']
        print("Step5:"+self.summary.strip())

        file = open("summary.txt", "w")
        file.write(self.summary.strip())
        file.close

        self.get_keywords(self.summary)

    def get_keywords(self, cleaned_text):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Extract keywords from the following report:\n\n" + cleaned_text + "\nKeywords:\n",
            temperature=0.70,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        self.keywords = response['choices'][0]['text']
        print('Step6:' + self.keywords)

        file = open("keywords.txt", "w")
        file.write(self.keywords.strip())
        file.close

        print(self.keywords)

        self.classification()

    def classification(self):
        with open('keywords.txt') as f:
            lines = f.read()

        response = openai.Completion.create(
            model="curie:ft-personal-2022-10-01-16-44-39",
            prompt=lines + " ->",
            temperature=0.70,
        )
        # print(response)
        self.classify = response['choices'][0]['text']
        print('Step7:' + self.classify)

        with open("classification.txt", "w") as f:
            f.write(self.classify.strip())

        self.classification2()

    def classification2(self):
        with open('keywords.txt') as f:
            lines = f.read()

        response = openai.Completion.create(
            model="curie:ft-personal-2022-10-02-02-00-04",
            prompt=lines + " ->",
            temperature=0.70,
        )
        # print(response)
        self.classify2 = response['choices'][0]['text']
        print('Step8:'+self.classify2)

        file = open("classification2.txt", "w")
        file.write(self.classify2.strip())
        file.close


if __name__ == '__main__':
    with open('parsed.txt') as f:
        text = f.read()
        # print(text)

    a = Text_analysis("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")
    cleaned_text = text
    # a.get_summary(cleaned_text)
    a.get_keywords(cleaned_text)
    # datapath = "Photovoltaic cell is used to absorb solar energy "
    # a.classification(datapath)
