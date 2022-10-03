# PROJECT SUMMARY
The NASA Technical Report Server (NTRS) includes hundreds of thousands of items containing scientific and technical information (STI) funded by NASA. To enable searches of this large NTRS database, this project involves Ai development that can read a collection of PDF files, summarize those files, produce statistical reports of the language usage, and list topic keywords. In this project, several techniques will be used including machine learning modelling and statistical analysis to produce the desired report summary of each document. By doing so, future researchers would be able to use this information to find desired historical data quickly.

# LINK TO FINAL PROJECT
https://wesleychiang96-nasa-pdf-analytics-stream-app-wzl0jx.streamlitapp.com/

***Please download the Result report and zoom in to get a clearer image regarding the words displayed on Bi-gram and Trigram Graph

# PROJECT DEMO GUIDE:
https://youtu.be/sOjIjFFgyWg

# LINK TO PROJECT "DEMO"
https://youtu.be/sOjIjFFgyWg

![image](https://user-images.githubusercontent.com/77789825/193482738-7791c832-649b-4df2-9ed1-dc83c4e29ecd.png)

# WHAT EXACTLY DOES IT DO?
NASA NLP Analytics is an Ai SOFTWARE that carries out natural language processing to analyse the scientific report in order to produce statistical reports of language used and content prediction. In this case, This software will automatedly analyse each document included inside a corpus prepared. The software developed not only can integrate with the NASA website but also with third-party software in producing an automated application. The project demo will display the 56 technical reports retrieved from NASA Technical Report Server and the report analysis produced by our software to enable comparison.

# HOW DOES IT WORK?
In short, the AI application developed can be divided into several steps, including text extraction, keyword analysis, text summarization, content prediction and pdf production. In this area, I will explain in detail the 3 main features of the software :

1. Text Analysis based on keywords 

To achieve this objective, NLTK Scikit-learn python library is utilised to carry out the analysis of the text extracted from the pdf report. Apart from single word data analysis, 2 and 3 words terms were also analysed to obtain the frequency of the count. This is to provide a more in-depth analysis of the overall content. Next, all the data will be visualized by using Malpltolib Python packages in graph format. Wordcloud is included to give the reader a clearer picture of the report.

2. Report Text Summarization 

Text Summarization is the most complex part of the whole software to ensure accuracy. In this case, GPT-3 neural network machine learning is leveraged. The state-of-the-art machine learning model is able to produce high quality and understandable summary of the original text without affecting its original meaning compared to another model.

3. Content Scope Prediction 

Similar to report text summarization, GPT-3 machine learning from OPenAi is applied to carry out this task. On top of that, I carry out model-retraining by building my own dataset from the NASA Information Scope Documentation. It is applied to predict the scope and the interest of the overall text to give the reader a clearer image. And with all the information analysed, the information will be displayed and produced in a report.

# WHAT DO WE HOPE TO ACHIEVE?
We believe that this software will be able to retrieve valuable reports from the report analysis so that the data collected can be applied to help researchers in accessing the right information that they want. Accessing all those thousand and hundreds of documents would be trouble, especially for users of the NASA website. The readily developed software will help to overcome this problem. With the information analysed, it can not only be further developed to build a query system or even a recommendation system for users to access reports. We hope that this software can change the situation and save users time in reading the reports with thousands of words

# HACKATHON JOURNEY
This hackathon is really an opportunity for me to apply my skill and knowledge to a potential project. Natural Language Processing is really things, especially in the financial sector and a lot more. Having my previous experience in a past hackathon (Banking industries hackathon), I get to know how real-world data scientists would do in building and leveraging technology in text analytics. Those experiences really help me to make up my mind in participating in this hackathon to apply my knowledge. As a solo player this time, it's quite challenging for me in terms of time management. Few days prior to the hackathon, I even started to search for related information and screened through the problem statements. So I started my preparartion early and carry out the developement step by step from data cleaning, testing and debugging. In short, it is a really special experience for me and I enjoy the most!


# TOOLS:
NASA Technical Report Server
Python Library
Pycharm
Git and Github
OPenAI

# SPACE AGENCY DATA
SOURCES: NASA TECHNICAL REPORT SERVER
(Link: https://ntrs.nasa.gov/search?center=CDMS）

All the data was retrieved with the purpose of building a corpus of report samples. The following Drive consists of all the 56 data reports downloaded from the website:
https://drive.google.com/drive/folders/1jN5qZb-rkgrGGdoofbK2emVZ4WEQEQse?usp=sharing

# REFERENCES
NASA STI Repository OpenAPI: Data Dictionary - Citation Search Response (https://sti.nasa.gov/docs/OpenAPI-Data-Dictionary-062021.pdf)
NASA Scientific and Technical Information Scope and Subject Category Guide  (https://ntrs.nasa.gov/api/citations/20000025197/downloads/20000025197.pdf)

# TAGS
#NLP#AI#DATA#ANALYTICS#ML#STATISTICAL#SOLO
