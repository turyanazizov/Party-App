import PyPDF2

def replace_words_in_pdf(input_pdf, output_pdf, word_to_replace, replacement_word):
    pdf_reader = PyPDF2.PdfFileReader(input_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        modified_text = text.replace(word_to_replace, replacement_word)
        page = pdf_reader.getPage(page_num)
        page.mergePage(PyPDF2.pdf.PageObject.createTextObject(modified_text))
        pdf_writer.addPage(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == '__main__':
    input_pdf_file = 'ticket.pdf'
    output_pdf_file = 'output.pdf'
    word_to_replace = 'Turyan Azizov'
    replacement_word = 'Ali Aliyev'

    replace_words_in_pdf(input_pdf_file, output_pdf_file, word_to_replace, replacement_word)