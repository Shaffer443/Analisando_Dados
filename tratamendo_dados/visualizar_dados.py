import selecionar_arquivo.selecionar_arquivo as i
import funcao_tratamento_dados as f
import pandas as pd
import numpy as np
import sweetviz as sv
from ydata_profiling import ProfileReport
import openpyxl
import xlrd
import webbrowser

####################################################################
# Quantidades de chaves em um dicionário e informar seus nomes:
arquivos = i.lista_associado_arquivo
qtd_chaves_com_arquivos = len(i.lista_associado_arquivo.keys())
print(f"\nO sistema contém {qtd_chaves_com_arquivos} chave(es).")
print("Com os dados abaixo:")

link_path = []

for k in i.lista_associado_arquivo:
    print(f"\n{arquivos[k]}")
    link_path.append(arquivos[k])

letrasA = ["c","s","v"]
letrasB = ["x","l","s"]

tipos=[letrasA, letrasB]

#for t in tipos:
#    caminhos = f.verifica_final_string(link_path[0],t)
#    if t == letrasA:
#        print(".csv", True)
#        df = pd.read_csv(link_path[0])
#        print(df)
#        break
#    if t == letrasB:
#        print(".xls", True)
#        df = pd.read_excel(link_path[0], )
#        print(df)
#        break

arquivo = link_path[0]

if arquivo.endswith('.csv'):
    df = pd.read_csv(arquivo, encoding='utf-8')  # ou 'latin1', se necessário
elif arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
    df = pd.read_excel(arquivo)
else:
    raise ValueError("Formato de arquivo não suportado.")



####################
# Modelando, info 01:

print("\nSelecione uma Opção:")
print(" 1 - Sweetviz Analyze")
print(" 2 - ydata-profiling")
print(" 0 - Sair")

numero = int(input("Informe o numero: "))

if numero == 1:
    my_report = sv.analyze(df)
    my_report.show_html()  # Default arguments will generate to "SWEETVIZ_REPORT.html"
if numero == 2:
    # Modelo
    # df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
    profile = ProfileReport(df, title="Profiling Report")
    #profile.to_notebook_iframe()
    #profile.to_widgets()
    profile.to_file("relatorio.html")
    webbrowser.open("relatorio.html")




