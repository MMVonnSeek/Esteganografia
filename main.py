import tkinter as tk
from tkinter import filedialog, messagebox
import esteganografia
import os

class App:
    def __init__(self, root):
        self.root = root
        root.title("Esteganografia Binária com Senha")
        root.geometry("400x250")
        root.resizable(False, False)

        self.label = tk.Label(root, text="Escolha uma ação:")
        self.label.pack(pady=10)

        self.btn_ocultar = tk.Button(root, text="Ocultar Arquivo em MP3", command=self.ocultar)
        self.btn_ocultar.pack(pady=10)

        self.btn_extrair = tk.Button(root, text="Extrair Arquivo de MP3", command=self.extrair)
        self.btn_extrair.pack(pady=10)

    def pedir_senha(self, titulo="Digite uma senha"):
        top = tk.Toplevel(self.root)
        top.title(titulo)
        top.geometry("300x120")
        top.resizable(False, False)

        tk.Label(top, text="Senha:").pack(pady=5)
        senha_entry = tk.Entry(top, show="*", width=30)
        senha_entry.pack(pady=5)
        senha_confirmada = []

        def confirmar():
            senha_confirmada.append(senha_entry.get())
            top.destroy()

        tk.Button(top, text="Confirmar", command=confirmar).pack(pady=10)
        self.root.wait_window(top)
        return senha_confirmada[0] if senha_confirmada else None

    def ocultar(self):
        mp3_path = filedialog.askopenfilename(title="Escolha o arquivo MP3", filetypes=[("MP3 files", "*.mp3")])
        if not mp3_path:
            return

        secreto_path = filedialog.askopenfilename(title="Escolha o arquivo a ocultar")
        if not secreto_path:
            return

        saida_path = filedialog.asksaveasfilename(title="Salvar como", defaultextension=".mp3")
        if not saida_path:
            return

        senha = self.pedir_senha("Digite uma senha para criptografar")
        if not senha:
            return

        try:
            esteganografia.ocultar(mp3_path, secreto_path, saida_path, senha)
            messagebox.showinfo("Sucesso", f"Arquivo ocultado com sucesso em:\n{saida_path}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def extrair(self):
        modificado_path = filedialog.askopenfilename(title="Escolha o MP3 modificado", filetypes=[("MP3 files", "*.mp3")])
        if not modificado_path:
            return

        pasta_destino = filedialog.askdirectory(title="Escolha a pasta para salvar o arquivo extraído")
        if not pasta_destino:
            return

        senha = self.pedir_senha("Digite a senha para descriptografar")
        if not senha:
            return

        try:
            caminho = esteganografia.extrair(modificado_path, pasta_destino, senha)
            messagebox.showinfo("Sucesso", f"Arquivo extraído para:\n{caminho}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
