import PyPDF2

with open('dummy.pdf',mode='rb') as file:
	#print(file)
	reader=PyPDF2.PdfFileReader(file)
	print(reader.numPages)

	page=reader.getPage(0)
	page.rotateClockwise(90)
	writer=PyPDF2.PdfFileWriter()
	writer.addPage(page)

	with open('tilt.pdf',mode='wb') as new_file:
		writer.write(new_file)