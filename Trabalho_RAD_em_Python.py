# Trabalho RAD em Python AV1

#Remover possivél arquivo txt já criado
"""
import os
if os.path.exists("AtividadesFaculdade/TrabalhoAV1/Arquivo.txt"):
    os.remove("Arquivo.txt")
else:
    print("ESTO NON ECZISTE")
"""
import os

# Aqui eu entro
n = 1

while n == 1:
    print("====================================================================")
    print("|Você deseja criar um novo arquivo ou abrir um já existente?")
    selecionar = int(input("|Para Criar um Arquivo [1] - Para Abrir um Arquivo [2] - Para Alterar um Arquivo [3] - Para Deletar um arquivo [4] - Para sair [5]: "))

    if selecionar == 1:
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
        nome = Arquivo.write(str(input("Informe o seu nome: ")) + "\n")

        Arquivo.write("|Sobrenome: ")
        sobrenome_bd = Arquivo.write(str(input("Informe o seu sobrenome: ")) + "\n")

        Arquivo.write("|Idade: ")
        idade_bd = Arquivo.write(str(input("Informe a sua Idade: ")) + "\n")

        Arquivo.write("|Conta: ")
        conta_bd = Arquivo.write(str(input("Informe a sua Conta: ")) + "\n")

Conversar em @Pereirapro
