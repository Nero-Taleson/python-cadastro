def cadastrar(Nome, Idade):
    return Nome, Idade


def ver_cadastro():
    print ("----- CADASTRO -----")
    print(f'Nome: {cadastro[0]}')
    print(f'Idade: {cadastro[1]}')

cadastro = None
while True:
    Pergunta = input(
    "\n===== MENU =====\n"
    "[1] Cadastrar\n"
    "[2] Ver cadastro\n"
    "[3] Sair\n"
    "Escolha: "
)
    if Pergunta == "1":
        Nome = input("Qual seu nome? ")
        Idade = input("Qual sua idade? ")
        cadastro = cadastrar(Nome, Idade)
    elif Pergunta == "2":
        if cadastro == None:
            print ("Nenhum cadastro encontrado")
        else:
            ver_cadastro()
    elif Pergunta == "3":
         break
    else:
        print("ERROR")

