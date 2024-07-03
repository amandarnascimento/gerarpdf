import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
from reportlab.pdfgen import canvas

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        caminho_pasta.set(pasta_selecionada)

def docx_para_pdf(caminho_arquivo_word, caminho_arquivo_saida):
    try:
        doc = Document(caminho_arquivo_word)
        pdf = canvas.Canvas(caminho_arquivo_saida)
        largura, altura = pdf._pagesize  # Obtém o tamanho da página
        for i, paragraph in enumerate(doc.paragraphs):
            pdf.drawString(10, altura - 20 * (i + 1), paragraph.text)
        pdf.save()
    except Exception as e:
        raise e

def gerar_pdfs():
    pasta = caminho_pasta.get()
    if not pasta:
        messagebox.showerror("Erro", "Nenhuma pasta selecionada.")
        return

    pasta_saida = os.path.join(pasta, "PDFs criados")
    os.makedirs(pasta_saida, exist_ok=True)

    arquivos_word = [f for f in os.listdir(pasta) if f.endswith('.docx')]
    if not arquivos_word:
        messagebox.showinfo("Informação", "Nenhum arquivo Word encontrado na pasta selecionada.")
        return

    for arquivo_word in arquivos_word:
        caminho_arquivo_word = os.path.join(pasta, arquivo_word)
        caminho_arquivo_saida = os.path.join(pasta_saida, f"{os.path.splitext(arquivo_word)[0]}.pdf")
        try:
            docx_para_pdf(caminho_arquivo_word, caminho_arquivo_saida)
            time.sleep(1)  # Adicionar atraso para evitar problemas de automação com o Word
        except Exception as e:
            with open("erro_log.txt", "a") as log_file:
                log_file.write(f"Erro ao converter {arquivo_word}: {str(e)}\n")
            messagebox.showerror("Erro", f"Erro ao converter {arquivo_word}: {str(e)}")

    messagebox.showinfo("Sucesso", f"{len(arquivos_word)} arquivos foram convertidos em PDF.")

app = tk.Tk()
app.title("Gerar PDF")

caminho_pasta = tk.StringVar()

tk.Label(app, text="Selecione a pasta:").pack(pady=10)
tk.Entry(app, textvariable=caminho_pasta, width=50).pack(padx=10)
tk.Button(app, text="Selecionar Pasta", command=selecionar_pasta).pack(pady=10)
tk.Button(app, text="Gerar PDFs", command=gerar_pdfs).pack(pady=10)

app.mainloop()
