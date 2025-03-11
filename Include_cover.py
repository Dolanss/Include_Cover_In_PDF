import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


input_folder = Path(r'C:\Users\gabriel.oliveira\OneDrive - Grupo Value\Área de Trabalho\Teste')
cover_pdf = Path(r'C:\Users\gabriel.oliveira\Downloads\pdf_sample_2.pdf')

def add_cover(input_pdf, output_pdf, cover_pdf):
    cover = PdfReader(cover_pdf)
    original = PdfReader(input_pdf)
    writer = PdfWriter()

    # Adicionando a capa
    writer.add_page(cover.pages[0])

    # Adicionando páginas do documento original
    for page_num in range(len(original.pages)):
        writer.add_page(original.pages[page_num])

    # Escrevendo o novo PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# Processamento dos arquivos PDF no diretório
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        input_pdf = input_folder / filename
        output_pdf = input_folder / f'output_{filename}'
        add_cover(input_pdf, output_pdf, cover_pdf)
        print(f'Capa adicionada ao arquivo: {filename}')

print('Processamento concluído!')