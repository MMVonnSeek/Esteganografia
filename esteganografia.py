import os

DELIMITER = b":::STEGA_START:::"

def ocultar(container_path, secreto_path, saida_path):
    with open(container_path, "rb") as f1, open(secreto_path, "rb") as f2:
        container = f1.read()
        secreto = f2.read()
    
    nome_arquivo = os.path.basename(secreto_path).encode()
    payload = nome_arquivo + b"\n" + secreto

    with open(saida_path, "wb") as f_out:
        f_out.write(container)
        f_out.write(DELIMITER)
        f_out.write(payload)

def extrair(arquivo_modificado, destino_pasta):
    with open(arquivo_modificado, "rb") as f:
        conteudo = f.read()

    if DELIMITER not in conteudo:
        raise ValueError("Nenhum dado oculto encontrado.")

    parte_oculta = conteudo.split(DELIMITER)[1]
    nome, dados = parte_oculta.split(b"\n", 1)

    caminho_final = os.path.join(destino_pasta, nome.decode())
    with open(caminho_final, "wb") as f_out:
        f_out.write(dados)
    
    return caminho_final
