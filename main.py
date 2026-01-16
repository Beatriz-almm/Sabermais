import tkinter as tk 
import pandas as pd 
import random

# carregar arquivo do excel
df= pd.read_excel("questions.xlsx")
# pegar perguntas aleatoriamente 
questions = df.sample(n=10).values.tolist()

# variaveis globais
score= 0 
pergunta_atual = 0 

# função p verificar resposta
def checkanswer(answer):
  global score, pergunta_atual
  if answer == resposta_certa.get():
    score+=1

pergunta_atual+=1
if pergunta_atual <len(questions):
  display_question()
else:
  show_result()




# função para exibir a prox pergunta 
def display_question():
  question, option1, option2, option3, option4, answer= questions[pergunta_atual]
  question_label.config(text=question)
  option1_btn.config(text="option1", state=tk.NORMAL, command=lambda:checkanswer(1))
  option2_btn.config(text="option2", state=tk.NORMAL,command=lambda:checkanswer(2))
  option3_btn.config(text="option3", state=tk.NORMAL,command=lambda:checkanswer(3))
  option4_btn.config(text="option4", state=tk.NORMAL,command=lambda:checkanswer(4))
  resposta_certa.set(answer)

# função para exibir o resultado final 
def show_result():
  messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz.\n\nPontuação final : {score/len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()
# função para jogar novamente 
def play_again():
  global score, pergunta_atual
  score= 0 
  pergunta_atual= 0 
  random.shuffle(perguntas)
  option1_btn.config(state=tk.NORMAL)
  option2_btn.config(state=tk.NORMAL)
  option3_btn.config(state=tk.NORMAL)
  option4_btn.config(state=tk.NORMAL)
  play_again_btn.pack_forget()



janela=tk.Tk()
janela.title("Saber+")
janela.geometry("400x450")

# cores da tela do quiz 
background_color="#ececec"
text_color="#000d40"
color_botao = "#011bf4"
botao_text_color = "#ffffff"
janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')



# icone na tela 

app_icone= PhotoImage(file"corujinha.png.png")
app_label= tk.label(janela, image=app_icone, bg=background_color)
app_label.pack(pady=10)


# componentes da interface
pergunta_label= tk.label(janela, text="",wraplength=380, bg=background_color, fg=text_color, font=("Arial" , 12 , "bold"))
pergunta_label.pack(pady=20)



option1_btn = tk.Button(janela, text="", width=30, bg=color_botao, fg=botao_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=color_botao, fg=botao_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=color_botao, fg=botao_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="Jogar Novamente", width=30, bg=color_botao, fg=botao_text_color, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela,command=play_again(), text="", width=30, bg=color_botao, fg=botao_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))


display_question()
janela.mainloop()

