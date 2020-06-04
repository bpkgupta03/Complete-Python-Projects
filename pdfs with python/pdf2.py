import PyPDF2

with open('twopagepdf.pdf',mode='rb') as file:
	reader=PyPDF2.PdfFileReader(file)

	page1=reader.getPage(0)
	print(page1)
	page2=reader.getPage(1)
	print(page2)

	page1.rotateClockwise(90)
	page2.rotateCounterClockwise(90)

	writer=PyPDF2.PdfFileWriter()
	writer.addPage(page1)
	writer.addPage(page2)

	#once run same file cant use further so making changes if any then create a another file
	with open('tilt3.pdf',mode='wb') as new_file:
		writer.write(new_file)
		