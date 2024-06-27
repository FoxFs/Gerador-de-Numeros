import tkinter as tk
from tkinter import messagebox
import random

#Função para gerar números de celulares
def gerar_numeros_celulares():
    ddd = int(ddd_entry.get())
    a1 = int(qtd_entry.get())
    resultados = []
    
    for n in range(a1):
        numeros = [random.randint(0, 9) for _ in range(8)]
        resultado = f"({ddd}) 9" + ''.join(map(str, numeros))
        resultados.append(resultado)
    
    resultado_texto = "\n".join(resultados)

    with open("Numeros.txt", "w") as arquivo:
        arquivo.write(resultado_texto)

    messagebox.showinfo("Numeros já gerados, tenha um bom dia!")
#Configs da interface
root = tk.Tk()
root.title("Gerador de Números de Celulares")

#Entrada para o DDD
tk.Label(root, text="Digite o DDD:").pack()
ddd_entry = tk.Entry(root)
ddd_entry.pack()

#Entrada para a quantidade de números
tk.Label(root, text="Quantos números você quer?").pack()
qtd_entry = tk.Entry(root)
qtd_entry.pack()

#Botão para gerar os números
gerar_button = tk.Button(root, text="Gerar Números", command=gerar_numeros_celulares)
gerar_button.pack()

#isso aqui vai gerar o texto 
resultado_text = tk.Text(root, height=10, width=30)
resultado_text.pack()

#Rodar a aplicação ate a janela fechar
root.mainloop()
