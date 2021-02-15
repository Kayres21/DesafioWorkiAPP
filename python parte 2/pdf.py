from fpdf import FPDF 
import csv


def make_pdf():

        with open('result.csv', newline= '') as f:
                reader = csv.reader(f)
                reader
                        
                pdf = FPDF()
                pdf.add_page()
                
                page_width = pdf.w - 2 * pdf.l_margin
                
                pdf.set_font('Times','B',20.0) 
                pdf.cell(page_width, 0.0, 'Usuarios Data', align='C')
                pdf.ln(10)
                pdf.image('emblemmatic-pdf-logo-24.png', x= page_width/6, y=0, w=20, h= 20)
                pdf.set_font('Courier', '', 8)

                col_width = page_width/6

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                        pdf.cell(col_width*1.5, th, str(row[0].encode('mbcs').decode('utf8')), border=1)
                        pdf.cell(col_width, th, row[2].encode('mbcs').decode('utf8'), border=1)
                        pdf.cell(col_width, th, row[3].encode('mbcs').decode('utf8'), border=1)
                        pdf.cell(col_width*1.4, th, row[4].encode('mbcs').decode('utf8'), border=1)
                        pdf.cell(col_width*0.7, th, row[5].encode('mbcs').decode('utf8'), border=1)
                        pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times','',10.0) 
                

                pdf.output('resultados.pdf', 'F')

