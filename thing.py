from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("resumeC.pdf")
merger.append("transcriptC.pdf")

merger.write("merged.pdf")
merger.close()
