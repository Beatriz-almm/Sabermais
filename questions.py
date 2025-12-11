import pandas as pd 
# nossa lista de perguntas 
perguntas = [
    ["De onde é a invenção do chuveiro elétrico?",
     "França", "Inglaterra", "Brasil", "Itália",3],

    ["Quais o menor e o maior país do mundo?",
     "Vaticano e Rússia", "Nauru e China", "Mônaco e Canadá", "São Marino e Índia",1],

    ["Qual o nome do presidente do Brasil que ficou conhecido como Jango?",
     "Jânio Quadros", "Jacinto Anjos", "Getúlio Vargas", "João Goulart",4],

    ["Atualmente, quantos elementos químicos a tabela periódica possui?",
     "113", "109", "108", "118",4],

    ["Quais as duas datas que são comemoradas em novembro?",
     "Independência do Brasil e Dia da Bandeira",
     "Proclamação da República e Dia Nacional da Consciência Negra",
     "Dia do Médico e Dia de São Lucas",
     "Dia de Finados e Dia Nacional do Livro",2],

    ["Qual das alternativas abaixo apenas contêm classes de palavras?",
     "Vogais, semivogais e consoantes",
     "Artigo, verbo transitivo e verbo intransitivo",
     "Fonologia, Morfologia e Sintaxe",
     "Substantivo, verbo e preposição",4],

    ["Qual foi o recurso utilizado inicialmente pelo homem para explicar a origem das coisas?",
     "A Filosofia", "A Biologia", "A Matemática", "A Mitologia",4],

    ["Qual o maior animal terrestre?",
     "Baleia Azul", "Dinossauro", "Elefante africano", "Girafa",3],

    ["Que líder mundial ficou conhecida como 'Dama de Ferro'?",
     "Dilma Rousseff", "Angela Merkel", "Margaret Thatcher", "Hillary Clinton",3],

    ["As pessoas de qual tipo sanguíneo são consideradas doadores universais?",
     "Tipo A", "Tipo B", "Tipo O", "Tipo AB",3],

    ["As obras Abaporu, Operários e Antropofagia foram pintadas por qual artista brasileiro?",
     "Di Cavalcanti", "Anita Malfatti", "Candido Portinari", "Tarsila do Amaral",4],

    ["O que é Brexit?",
     "Saída do Reino Unido da Zona Euro",
     "Saída do Reino Unido da União Europeia",
     "Saída da Inglaterra do Reino Unido",
     "Fim da monarquia no Reino Unido",2],

    ["Em que país foi construído o Muro de Berlim?",
     "Estados Unidos", "China", "Coreia do Norte", "Alemanha",4],

    ["Qual destas substâncias faz parte da composição do vidro?",
     "Petróleo", "Fibra", "Celulose", "Areia",4],

    ["Qual foi o famoso navio que naufragou em sua viagem inaugural, em 1912?",
     "Titanic", "Britannic", "Lusitania", "Queen Mary",1]]
# criar dataframe do pandas 
df=pd.DataFrame(perguntas,columns=["Perguntas","Opção 1","Opção 2","Opção 3","Opção 4 ","Resposta"])
# salvar em excel 
df.to_excel("questions.xlsx", index=False)
print("Perguntas inseridas!!")