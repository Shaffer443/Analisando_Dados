import os
import tkinter as tk
from tkinter import filedialog

# Cria uma janela invisível do Tkinter
root = tk.Tk()
root.withdraw()

print('Quantos arquivos serão inseridos?')
qtd_input = int(input("Digite a quantidade (1, 2, 3...): "))

# Define os tipos de arquivos permitidos
filetypes = [
    ("Arquivos CSV", "*.csv"),
    ("Planilhas Excel", "*.xls"),
    ("Planilhas Excel (XLSX)", "*.xlsx"),
    ("Todos os arquivos", "*.*")
]

# Lista para armazenar os caminhos dos arquivos
lista_associado_arquivo = {}

for i in range(1, qtd_input + 1):
    print(f"\nSelecione o arquivo #{i}:")
    arquivo_selecionado = filedialog.askopenfilename(
        title=f"Selecione o arquivo #{i}",
        filetypes=filetypes
    )

    if arquivo_selecionado:
        nome_variavel = f"arquivo_{i}"
        lista_associado_arquivo[nome_variavel] = arquivo_selecionado
        print(f"Arquivo {nome_variavel} selecionado: {os.path.basename(arquivo_selecionado)}")
    else:
        print("Nenhum arquivo foi selecionado.")

# Exibe o dicionário final com os nomes das variáveis e seus caminhos
print("\nArquivos selecionados:")
for chave, caminho in lista_associado_arquivo.items():
    print(f"{chave}: {caminho}")


