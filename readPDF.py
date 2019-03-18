"""
This python  script will use pyPDF2 to read pdf file.
"""


from PyPDF2 import PdfFileReader
#google text to speech API Lib.
from gtts import gTTS
import os
import time

class Pdf_handler:

	def get_pdf_info(self, path):
		try:
			with open(path, 'rb') as book:
					#open pdf and extract basic info.
					self.pdf = PdfFileReader(book)
					if not self.pdf.isEncrypted:
						self.info = self.pdf.getDocumentInfo()
						self.number_of_pages = self.pdf.getNumPages()
						#print(self.info.author)
						#print(self.info.title)
						#print(self.number_of_pages)
						self.read_pdf(17)
					else:
						#need password to open book
						pass

		except FileNotFoundError as e:
			print(e)
			#log exception here
		else:
			pass

	def read_pdf(self, page_no):
		page = self.pdf.getPage(page_no)
		text = page.extractText()
		#text_list = text.splitlines()
		print(text)
		self.text_to_speech(text)


	def text_to_speech(self, text):
		language = 'en'
		#for val in text_list:
		#val = "this is a testing text, checking if it is working or not. "
		myobj = gTTS(text=text, lang=language, slow=False)
		myobj.save("audio.mp3")
		os.system("mpg321 audio.mp3")
		


if __name__ == "__main__":
	instance = Pdf_handler()
	print('-------')
	instance.get_pdf_info('LPTHW.pdf')
