import PyPDF2
import sys

inputs=sys.argv[1:]
#print(inputs)
def pdf_combiner(pdf_list):
	merger=PyPDF2.PdfFileMerger(pdf_list)
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	
	merger.write('super2.pdf')
	
pdf_combiner(inputs)