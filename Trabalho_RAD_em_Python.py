# Trabalho RAD em Python AV1
# Alunos:
# Lucas Pereira Dos Santos - 202002552051
# Vitor Dos Santos Barbosa Portela - 202002121025


#Remover possivél arquivo txt já criado
"""
import os
if os.path.exists("RAD_em_Python_Trabalho/Arquivo.txt"):
    os.remove("Arquivo.txt")
else:
    print("ESTO NON ECZISTE")
"""


# from RAD_em_Python_Trabalho import Connector_BD
# import psycopg2
"""Obs.: as chamadas de bibliotecas e de arquivos, bem como outras funções do resto foram 'comentadas' ou alteradas, pois só funcionavam
 com conexão direta com o banco de dados, então para garantir ao menos a interface foi colocada e dado mais atenção para
  a funcionalidade de manipulação de arquivos"""

import os
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese')
# Aqui eu entro no loop
a = 1
while a == 1:
    # Menu Seleção de funcionalidades
    os.system("cls")  # Comando limpa tela
    print("====================================================================")
    print("|Você deseja criar um novo arquivo ou abrir um já existente?")
    selecionar = str(input("|Para Criar um Arquivo [1] - Para Abrir um Arquivo [2] - Para Alterar um Arquivo [3] - Para Deletar um arquivo [4] - Para sair [5]: "))

    if selecionar == "1":
        os.system("cls") #Comando limpa tela
        #Menu Criação de arquivo
        print("====================================================================")
        #nomeArquivo = str(input("Informe o nome do arquivo a ser criado: "))
        Arquivo = open(str(input("|Informe o nome do arquivo a ser criado [Obs.: Insira o formato do arquivo ex.: .txt no final]: ")), "w") # Colocar para criar arquivos
        #print(Arquivo.read()
        print("====================================================================")
        print("|--Insira as suas Informações --")

        #Parte da Pessoa
        Arquivo.write("===============================")
        Arquivo.write("|Cpf: ")
        cpf_bd = Arquivo.write(str(input("Informe seu cpf: ")) + "\n")
        Arquivo.write("|Nome: ")
        nome_bd = Arquivo.write(str(input("Informe o seu nome: ")) + "\n")
        Arquivo.write("|Sobrenome: ")
        sobrenome_bd = Arquivo.write(str(input("Informe o seu sobrenome: ")) + "\n")
        Arquivo.write("|Idade: ")
        idade_bd = Arquivo.write(str(input("Informe a sua Idade: ")) + "\n")
        Arquivo.write("|Conta: ")
        conta_bd = Arquivo.write(str(input("Informe a sua Conta: ")) + "\n")

        # Parte da Conta

        Arquivo.write("|Agência: ")
        agencia_bd = Arquivo.write(str(input("Informe a sua Agência: ")) + "\n")
        Arquivo.write("|Número: ")
        numero_bd = Arquivo.write(str(input("Informe o seu Número: ")) + "\n")
        Arquivo.write("|Saldo: ")
        saldo_bd = Arquivo.write(str(input("Informe o seu Saldo: ")) + "\n")
        Arquivo.write("|Gerente: ")
        gerente_bd = Arquivo.write(str(input("Informe o seu Gerente: ")) + "\n")
        Arquivo.write("|Titular: ")
        titular_bd = Arquivo.write(str(input("Informe a sua Titular: ")) + "\n")

        Arquivo.close()

    if selecionar == "2":
        os.system("cls")  # Comando limpa tela
        # Menu Vizualização
        print("====================================================================")
        print("|Informe o arquivo a ser Aberto/Vizualizado: ")
        try:
            with open(input("|Informe o nome do arquivo a ser aberto [Obs.: Insira o formato do arquivo ex.: .txt no final]: "), "r+") as abrir: # Colocar para criar arquivos
                for Abrir in abrir:
                    print(Abrir)
        except:
            print("Insira corretamente o nome do arquivo com o .txt no final!")

    if selecionar == "3":
        os.system("cls")  # Comando limpa tela
        # Indice Alterar o arquivo
        print("====================================================================")
        # nomeArquivo = str(input("Informe o nome do arquivo a ser criado: "))
        Arquivo = open(str(input("|Informe o nome do arquivo a ser alterado [Obs.: Insira o formato do arquivo ex.: .txt no final]: ")),"w")  # Colocar para criar arquivos
        # print(Arquivo.read()

        print("====================================================================")
        print("|--Insira as suas Informações --")

        # Parte da Pessoa a ser editada

        Arquivo.write("===============================\n")
        Arquivo.write("|Cpf: ")
        cpf_bd = Arquivo.write(str(input("Informe seu cpf: ")) + "\n")
        Arquivo.write("|Nome: ")
        nome_bd = Arquivo.write(str(input("Informe o seu nome: ")) + "\n")
        Arquivo.write("|Sobrenome: ")
        sobrenome_bd = Arquivo.write(str(input("Informe o seu sobrenome: ")) + "\n")
        Arquivo.write("|Idade: ")
        idade_bd = Arquivo.write(str(input("Informe a sua Idade: ")) + "\n")
        Arquivo.write("|Conta: ")
        conta_bd = Arquivo.write(str(input("Informe a sua Conta: ")) + "\n")

        # Parte da Conta a ser editada

        Arquivo.write("|Agência: ")
        agencia_bd = Arquivo.write(str(input("Informe a sua Agência: ")) + "\n")
        Arquivo.write("|Número: ")
        numero_bd = Arquivo.write(str(input("Informe o seu Número: ")) + "\n")
        Arquivo.write("|Saldo: ")
        saldo_bd = Arquivo.write(str(input("Informe o seu Saldo: ")) + "\n")
        Arquivo.write("|Gerente: ")
        gerente_bd = Arquivo.write(str(input("Informe o seu Gerente: ")) + "\n")
        Arquivo.write("|Titular: ")
        titular_bd = Arquivo.write(str(input("Informe a sua Titular: ")) + "\n")

        Arquivo.close()

    if selecionar == "4":
        os.system("cls")  # Comando limpa tela
        # Menu Deleção de Arquivo
        print("====================================================================")
        try:
            os.remove(str(input("Informe o nome do arquivo para ser deletado [Obs.: Insira o formato do arquivo ex.: .txt no final]: ")))
            print("Seu arquivo foi deletado com Sucesso!")
        except:
            print("O nome foi escrito de forma incorreta! Digite novamente")


    print("====================================================================")
    a = int(input("|Você deseja voltar ao menu ou  sair? Menu [1] Sair [2]: "))
