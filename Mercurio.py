import os


def processar_resporta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}Olá {nome} na minha visão vale muito apena, isso porque Python é uma das linguagem que mais cresce no mundo e possui salarios mensais que vão desde R$2.100,00 até mais de R$ 10.000,00.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}Olá {nome} para aprender os conceitos básicos de Python, pode demorar entre 1 e 3 meses. Já para aprender os temas mais avançados, pode demorar entre 4 e 12 meses.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}Olá {nome} quando conseguir escrever um programa curto em minutos. O tempo necessário para aprender os fundamentos básicos da linguagem pode variar de dois a seis meses.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}Olá {nome} pode estudar através de vidos gratuitos no YouTube, livros e sites de programação, porém se buscar um curso na Udemy, Alura entre potros.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')
    

def start():
    # Apresentar o chatbot
    print('Olá Bem-vindo ao serviços.com')
    # Pedir o nome:
    nome =input('Digite seu nome: ')
    # Pedir o e-mail
    email =input('Digite seu e-mail: ')
    
    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.
            linesep}[2] - Quanto tempo leva para conseguir um emprego com Python?{os.
            linesep}[3] - Quando vou saber que estou Bom o suficiente para conseguir um emprego em Python?{os.
            linesep}[4] - Onde me recomenta estudar Python para conseguir um emprego hoje?{os.
            linesep}')
        # Processar a resposta enviada
        processar_resporta(resposta, nome)
    
if __name__ =='__main__':
    start()