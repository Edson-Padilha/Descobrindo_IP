#author: Edson Marciano Rodrigues Padilha

import socket

def linhas():
    print('-'*70)

def cabecalho():
    linhas()
    print('ENDEREÇO DE IP'.center(70,' '))
    linhas()

def endereco():
    resp = "S"
    while(resp == "S"):
        cabecalho()
        url = input("Digite endereço url: ")
        ip = socket.gethostbyname(url)

        print(f"O endereço do IP referente a url informada é: {ip}")
        linhas()
        resp = input("Digite < S > para continuar: ").upper()

        if resp != "S":
            print("Você saiu do sistema...")
            linhas()


endereco()