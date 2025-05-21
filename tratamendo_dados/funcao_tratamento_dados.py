import re


def verifica_final_string(string, letras):
    """
    Verifica se o final da string (após o último ponto) contém as letras específicas.

    Args:
      string: A string a ser verificada.
      letras: A lista das letras a serem verificadas.
    """
    # Encontra o último ponto e pega a parte da string após o ponto.
    posicao_ponto = string.rfind(".")
    if posicao_ponto != -1:
        substring_final = string[posicao_ponto + 1:]

        # Verifica se a substring final tem três caracteres.
        if len(substring_final) == 3:
            # Verifica se as letras estão presentes na substring.
            if all(letra in substring_final for letra in letras):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# Exemplo de uso:
#string = "exemplo.abc"
#letras = ["a", "b", "c"]
#if verifica_final_string(string, letras):
#    print("O final da string contém as letras específicas.")
#else:
#    print("O final da string não contém as letras específicas.")