import PyPDF2
import sys
inputs=sys.argv[1:]
#print(inputs)
def pdf_merge(inputs):
	merger=PyPDF2.PdfFileMerger()
	for pdf in inputs:
		merger.append(pdf)
	merger.write('super_certificatess.pdf')
pdf_merge(inputs)

