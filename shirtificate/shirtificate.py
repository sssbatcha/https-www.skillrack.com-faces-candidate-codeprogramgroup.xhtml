from fpdf import FPDF
fp =  open('downloads/boot.txt', 'r')
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', '', 11)
line = fp.read()
pdf.multi_cell(200, 5, line, 0, 1)
pdf.output('test.pdf', 'F')