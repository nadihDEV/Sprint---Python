import pandas as pd

# Dados do quiz
dados_quiz = {
    "Pergunta": [
        "Qual foi a primeira temporada da Fórmula E?",
        "Quem é o piloto com mais vitórias na Fórmula E?",
        "Qual é a principal diferença entre a Fórmula E e a Fórmula 1?",
        "Qual é o nome do campeonato de pilotos da Fórmula E?",
        "Em que cidade ocorreu a primeira corrida da Fórmula E?",
        "Qual é a velocidade média dos carros da Fórmula E?",
        "Qual é a equipe que mais ganhou o campeonato mundial de Fórmula E?",
        "Quais ou qual piloto(s) brasileiro(s) que ganharam o mundial de Fórmula E?"
    ],
    "Alternativas": [
        "1) 2013  2) 2014  3) 2015  4) 2016",
        "1) Lucas di Grassi  2) Jean-Éric Vergne  3) Sebastien Buemi  4) Nelson Piquet",
        "1) Fórmula E usa carros elétricos  2) Fórmula 1 usa gasolina",
        "1) Campeonato Mundial de Fórmula E  2) Copa do Mundo de Fórmula E",
        "1) Paris  2) Pequim  3) Nova Iorque  4) Londres",
        "1) Abaixo de 300 km/h  2) Entre 200 e 280 km/h  3) Acima de 300 km/h  4) Entre 280 e 300 km/h",
        "1) Mercedes  2) Techeetah  3) Audi  4) Andretti",
        "1) Nelson Piquet Jr e Lucas di Grassi  2) Lucas di Grassi  3) Nelson Piquet Jr  4) Bruno Senna e Nelson Piquet Jr"
    ],
    "Resposta_Certa": [
        "2",  # 2014
        "2",  # Jean-Éric Vergne
        "1",  # Fórmula E usa carros elétricos
        "1",  # Campeonato Mundial de Fórmula E
        "2",  # Pequim
        "3",  # Acima de 300 km/h
        "2",  # Techeetah
        "1"   # Nelson Piquet Jr e Lucas di Grassi
    ]
}

# Criando o DataFrame
df_quiz = pd.DataFrame(dados_quiz)

def coletar_informacoes():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu e-mail: ")
    return nome, idade, email

def fazer_quiz(df, nome):
    score = 0
    total_perguntas = len(df)

    print(f"\nBem-vindo ao Quiz da Fórmula E, {nome}!\n")
    
    for index, row in df.iterrows():
        print(f"{index + 1}. {row['Pergunta']}")
        print(row['Alternativas'])
        
        resposta_usuario = input("Digite o número da sua resposta: ")

        resposta_usuario = resposta_usuario.strip()
        if resposta_usuario.startswith('1'):
            resposta_usuario = '1'
        elif resposta_usuario.startswith('2'):
            resposta_usuario = '2'
        elif resposta_usuario.startswith('3'):
            resposta_usuario = '3'
        elif resposta_usuario.startswith('4'):
            resposta_usuario = '4'

        if resposta_usuario == row['Resposta_Certa']:
            print("Correto!\n")
            score += 1
        else:
            print(f"Incorreto! A resposta correta é: {row['Resposta_Certa']}\n")
    
    print(f"Você acertou {score} de {total_perguntas} perguntas corretamente.")
    print(f"Sua pontuação final: {score / total_perguntas * 100:.2f}%")

# Coletando informações do usuário
nome, idade, email = coletar_informacoes()

# Executando o quiz
fazer_quiz(df_quiz, nome)
