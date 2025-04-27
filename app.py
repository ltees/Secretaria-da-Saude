import os

def exibir_nome_do_programa():
    print("Secretaria da Saúde\n")

def exibir_opcoes():
    print("1. Paciente")
    print("2. Médico ou profissional da saúde")
    print("3. Secretaria da saúde")
    print("4. Administradores do sistema\n")

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)

def paciente():
    exibir_subtitulo("Página do paciente")
    print("""
        1. Entrar
        2. Cadastrar
""")
    opcao_paciente = int(input("Digite o número desejado:"))
    if opcao_paciente == 1:
        nome_usuario = input("Digite seu nome de login:")
        senha = input("Digite sua senha:")
    elif opcao_paciente == 2:
        print("Vá para a página de cadastro")
    else:
        opcao_invalida()


def opcao_invalida():
    os.system("cls")
    print("Essa opção é invalida\n")

def escolher_opcao():
    opcao = int(input("Digite o número da opção desejada:"))
    match opcao:
        case 1:
            paciente()
        case 2:
            print("Médico ou profissional da saúde escolhido")
        case 3:
            print("Secretaria da saúde escolhido")
        case 4:
            print("Administradores do sistema escolhido")
        case 5:
            opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
