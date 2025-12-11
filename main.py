import tkinter as tk 
import pandas as pd 
import random

df= pd.read_excel("questions.xlsx")
perguntas = df.sample(n=10).values.tolist()
print(perguntas)

janela=tk.Tk()
janela.title("Saber+")
janela.geometry("400x450")
# cores da tela do quiz 
background_color="#ececec"
text_color="#000d40"
color_botao = ""
