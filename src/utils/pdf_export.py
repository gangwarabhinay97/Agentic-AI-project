from fpdf import FPDF
import os
class PDFReportGenerator:
    @staticmethod
    def create_pdf(text, out_path='outputs/report.pdf'):
        pdf = FPDF(); pdf.add_page(); pdf.set_font('Helvetica', size=12)
        pdf.cell(0, 10, 'Autonomous Data Analysis Report', ln=True, align='C')
        for line in text.split('\n'): pdf.multi_cell(0, 8, line.encode('latin-1', 'replace').decode('latin-1'))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        pdf.output(out_path)
        return out_path
