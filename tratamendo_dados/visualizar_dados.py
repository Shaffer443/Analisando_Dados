import selecionar_arquivo.selecionar_arquivo as i
import funcao_tratamento_dados as f
import pandas as pd
import sweetviz as sv

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

for t in tipos:
    caminhos = f.verifica_final_string(link_path[0],t)
    if t == letrasA:
        print("\n.csv", True)
        df = pd.read_csv(link_path[0])
        print(df)
        break
    elif t == letrasB:
        print("\n.xls", True)
        df = pd.read_excel(link_path[0])
        print(df)
        break

####################
# Modelando, info 01:

print("\nSelecione uma Opção:")
print(" 1 - Sweetviz Analyze")
print(" 0 - Sair")

numero = int(input("Informe o numero: "))

if numero == 1:
    my_report = sv.analyze(df)
    my_report.show_html()  # Default arguments will generate to "SWEETVIZ_REPORT.html"




