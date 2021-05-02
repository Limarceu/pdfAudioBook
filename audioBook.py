import PyPDF4 as pdff
import pyttsx3 as tts


#set the voice to 'en' or 'pt'

'''Some pdf files not works, so you need to open it with text editor like word from windows and save it as pdf.'''
#To Read Pdf File
file_path = 'Richard Dawkins - O Capelão do Diabo.pdf'
file1 = pdff.PdfFileReader(open(file_path, 'rb'))

#Instance of speaker
readder = tts.init()

#Reader page by page in Unicode
#Just because this book, I did start to read from page 6
for paper in range(6,file1.getNumPages()):
    sheett = file1.getPage(paper)
    ready = sheett.extractText()
    # If you want save audio
    readder.save_to_file(ready, f'book_{paper}.mp3')  
    print(ready)
    readder.say(ready)
    readder.runAndWait()


