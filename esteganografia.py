import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

DELIMITER = b":::STEGA_START:::"

def gerar_chave(senha: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(senha.encode()))

def ocultar(container_path, secreto_path, saida_path, senha):
    salt = os.urandom(16)
    chave = gerar_chave(senha, salt)
    fernet = Fernet(chave)

    with open(container_path, "rb") as f1, open(secreto_path, "rb") as f2:
        container = f1.read()
        secreto = f2.read()

    nome = os.path.basename(secreto_path).encode()
    criptografado = fernet.encrypt(nome + b"\n" + secreto)

    with open(saida_path, "wb") as f_out:
        f_out.write(container)
        f_out.write(DELIMITER)
        f_out.write(salt)  # salva o salt para regenerar a chave
        f_out.write(criptografado)

def extrair(arquivo_modificado, destino_pasta, senha):
    with open(arquivo_modificado, "rb") as f:
        conteudo = f.read()

    if DELIMITER not in conteudo:
        raise ValueError("Nenhum dado oculto encontrado.")

    parte_oculta = conteudo.split(DELIMITER)[1]
    salt = parte_oculta[:16]
    criptografado = parte_oculta[16:]

    chave = gerar_chave(senha, salt)
    fernet = Fernet(chave)

    try:
        dados = fernet.decrypt(criptografado)
    except:
        raise ValueError("Senha incorreta ou dados corrompidos.")

    nome, conteudo = dados.split(b"\n", 1)
    caminho_final = os.path.join(destino_pasta, nome.decode())

    with open(caminho_final, "wb") as f_out:
        f_out.write(conteudo)

    return caminho_final
