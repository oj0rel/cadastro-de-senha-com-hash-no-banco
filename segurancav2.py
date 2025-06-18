import re
import hashlib
import sqlite3


def cadastrar_email():
    while True:
        email_hold = str(input("Insira seu email: "))
        senha_hold = str(input("Insira sua senha (Deve conter no mínimo: 8 caracteres, 1 letra maíuscula, minúscula, caracter especial (@#$) e número):"))

        if "@" in email_hold and "." in email_hold:
            print("O endereço de email atende aos requisitos necessários.")
            senha_correta = True

            print("---"*20)

            if len(senha_hold) < 8:
                print("A senha deve ter no mínimo 8 caracteres.")
                senha_correta = False
            if not re.search(r"[A-Z]", senha_hold):
                print("A senha deve conter pelo menos uma letra maiúscula.")
                senha_correta = False
            if not re.search(r"[a-z]", senha_hold):
                print("A senha deve conter pelo menos uma letra minúscula.")
                senha_correta = False
            if not re.search(r"[@#$]", senha_hold):
                print("A senha deve conter pelo menos um caractere especial (@#$).")
                senha_correta = False
            if not re.search(r"[0-9]", senha_hold):
                print("A senha deve conter pelo menos um número.")
                senha_correta = False

            if senha_correta:
                print("A senha atende aos requisitos necessários.")
                return email_hold, senha_hold
            else:
                print("A senha não atende aos requisitos desejados. Por favor, tente novamente.")
                print("---"*20)

        else:
            print("Por favor, insira um email válido com o domínio (@exemplo.com).")
            print("---"*20)


def criptografar_senha(senha):
    hash_md5 = hashlib.md5(senha.encode()).hexdigest()
    senha_criptografada = hash_md5
    return senha_criptografada


def gravar_no_banco(email, senha):
    conexao = sqlite3.connect("registros.db")

    cur = conexao.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usuario(email TEXT PRIMARY KEY, senha TEXT)")

    cur.execute("SELECT email FROM usuario WHERE email = ?", (email,))
    if cur.fetchone():
        print("Este e-mail já está cadastrado no sistema. Tente outro.")
        print("---" * 20)
    else:
        cur.execute("""
            INSERT INTO usuario (email, senha) VALUES (?, ?)
        """, (email, senha))
        conexao.commit()
        print("O usuário foi registrado!")
        print("---" * 20)

    conexao.close()


def validar_senha():
    email_digitado = input("Digite seu e-mail: ")
    senha_digitado = input("Digite sua senha: ")
    senha_criptografada = criptografar_senha(senha_digitado)

    conexao = sqlite3.connect("registros.db")
    cur = conexao.cursor()
    cur.execute("SELECT senha FROM usuario WHERE email = ?", (email_digitado,))
    resultado_senha = cur.fetchone()
    conexao.close()

    if resultado_senha is None:
        print("O usuário não existe no banco de dados.")
        print("---"*20)
    else:
        senha_cadastrada = resultado_senha[0]
        if senha_cadastrada == senha_criptografada:
            print("Senha correta!")
            print("---"*20)
        else:
            print("A senha está incorreta!")
            print("---"*20)


def pesquisar_hash():
    email_digitado = input("Digite seu e-mail: ")

    conexao = sqlite3.connect("registros.db")
    cur = conexao.cursor()
    cur.execute("SELECT senha FROM usuario WHERE email = ?", (email_digitado,))
    resultado_senha = cur.fetchone()
    conexao.close()

    if resultado_senha is None:
        print("O usuário não existe no banco de dados.")
        print("---"*20)
    else:
        print(f"A senha do email é: {resultado_senha[0]}")
        print("---"*20)


def main():
    while True:
        print("---"*20)
        escolha = int(input("Digite o que deseja fazer:\n1 - CADASTRO DE SENHA\n2 - VALIDAR SENHA\n3 - PESQUISA DO HASH NO BANCO\n0 - SAIR\nEscolha: "))

        if escolha == 0:
            break;
        
        elif escolha == 1:
            email, senha = cadastrar_email()
            senha_criptografada = criptografar_senha(senha)
            gravar_no_banco(email, senha_criptografada)

        elif escolha == 2:
            validar_senha()
        
        elif escolha == 3:
            pesquisar_hash()
        
        else:
            print("Opção Inválida!\nTente Novamente\n")

main()