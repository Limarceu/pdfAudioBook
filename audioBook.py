import PyPDF4 as pdff
import pyttsx3 as tts


#set the voice to 'en' or 'pt'


#To Read Pdf File
file_path = 'C:\\users\\marcelodiana\\desktop\\Richard Dawkins - O Capelão do Diabo.pdf'
file1 = pdff.PdfFileReader(open(file_path, 'rb'))

#Instance of speaker
readder = tts.init()

#Reader page by page in Unicode
for paper in range(6,file1.getNumPages()):
    sheett = file1.getPage(paper)
    ready = sheett.extractText()
    print(ready)
    readder.say(ready)
    #readder.save_to_file(textPage, 'E:\\book.mp3')
    readder.runAndWait()


