import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

input_folder = Path(r'C:\Users\gabriel.oliveira\OneDrive - Grupo Value\Área de Trabalho\Teste')
cover_pdf = Path(r'C:\Users\gabriel.oliveira\Downloads\Capa - Devolutiva Complementar.pdf')
summary_pdf = Path(r'C:\Users\gabriel.oliveira\Downloads\Súmario - Devolutiva Complementar.pdf') 
other_sources_pdf = Path(r'C:\Users\gabriel.oliveira\Downloads\Canal de Atendimento e Contatos - Devolutiva Complementar 1.pdf')  

def add_cover_and_summary(input_pdf, output_pdf, cover_pdf, summary_pdf, other_sources_pdf):
    cover = PdfReader(cover_pdf)
    summary = PdfReader(summary_pdf)
    other_sources = PdfReader(other_sources_pdf)
    original = PdfReader(input_pdf)
    writer = PdfWriter()

    # Adicionando a capa
    writer.add_page(cover.pages[0])

    # Adicionando o sumário
    writer.add_page(summary.pages[0])

    # Adicionando páginas do documento original
    for page_num in range(len(original.pages)):
        writer.add_page(original.pages[page_num])

    # Adicionando a página de outras origens no final
    writer.add_page(other_sources.pages[0])

    # Escrevendo o novo PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# Processamento dos arquivos PDF no diretório
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        input_pdf = input_folder / filename
        output_pdf = input_folder / f'output_{filename}'
        add_cover_and_summary(input_pdf, output_pdf, cover_pdf, summary_pdf, other_sources_pdf)
        print(f'Capa, sumário e outras origens adicionados ao arquivo: {filename}')

print('Processamento concluído!')
