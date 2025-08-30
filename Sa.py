pessoas = []
cargos_validos = ['cliente', 'funcionário', 'fornecedor']

def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")

    while True:
        nome = input("Informe seu Nome: ").strip()
        if nome == "":
            print("Nome não pode ser vazio.")
            continue
        break

    while True:
        cpf = input("Informe seu CPF (apenas números): ")
        if cpf == "":
            print("Cpf não pode ser vazio")
            continue
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido. Deve conter exatamente 11 dígitos.")
            continue
        break

    while True:
        idade = input("Informe sua Idade: ").strip()
        if idade == "":
            print("Idade não pode ser vazia.")
            continue
        if '-' in idade:
            print("Idade deve conter apenas números inteiros.")
            continue
        idade_int = int(idade)
        if idade_int <= 0 or idade_int > 120:
            print("Idade inválida! Digite um número entre 1 e 120.")
            continue
        break

    while True:
        email = input("Informe seu E-mail: ")
        if email == "":
            print("Email não pode ser vazio.")
            continue
        if "@" in email and "." in email:
            break
        else:
            print("E-mail inválido. Deve conter '@' e '.'.")

    while True:
        cep = input("Informe seu CEP (apenas números): ").strip()
        if cep == "":
            print("Cep não pode ser vazio.")
            continue
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Deve conter exatamente 8 dígitos numéricos.")
            continue
        break

    while True:
        telefone = input("Informe seu telefone (somente números): ").strip()
        if telefone == "":
            print("Telefone não pode ser vazio.")
            continue
        if not telefone.isdigit() or len(telefone) not in (10, 11):
            print("Telefone inválido. Use 10 ou 11 dígitos.")
            continue
        break

    while True:
        cargo = input("Informe o cargo (cliente, funcionário, fornecedor): ").strip().lower()
        if cargo not in cargos_validos:
            print("Cargo inválido. Escolha entre cliente, funcionário ou fornecedor.")
            continue
        break

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "email": email,
        "telefone": telefone,
        "cep": cep,
        "cargo": cargo
    }
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    print("\n--- Lista de Pessoas ---")

    if not pessoas:
        print("Nenhuma pessoa cadastrada no sistema.")
        return

    for i, pessoa in enumerate(pessoas, start=1):
        print(f"\nPessoa {i}:")
        print(f"  Nome    : {pessoa['nome']}")
        print(f"  CPF     : {pessoa['cpf']}")
        print(f"  Idade   : {pessoa['idade']}")
        print(f"  Email   : {pessoa['email']}")
        print(f"  CEP     : {pessoa['cep']}")
        print(f"  Telefone: {pessoa['telefone']}")
        print(f"  Cargo   : {pessoa['cargo']}")

def editar_pessoa():
    listar_pessoas()
    if not pessoas:
        return
    indice_input = input("Digite o número da pessoa para editar: ")

    if indice_input.isdigit():
        indice = int(indice_input) - 1
    else:
        print("Entrada inválida.")
        return

    if 0 <= indice < len(pessoas):
        print("Deixe o campo vazio para manter o valor atual.")
        
        pessoa = pessoas[indice]

        nome = input(f"Novo nome ({pessoa['nome']}): ")
        cpf = input(f"Novo CPF ({pessoa['cpf']}): ")
        idade = input(f"Nova idade ({pessoa['idade']}): ")
        email = input(f"Novo email ({pessoa['email']}): ")
        cep = input(f"Novo CEP ({pessoa['cep']}): ")
        telefone = input(f"Novo telefone ({pessoa['telefone']}): ")
        cargo = input(f"Novo cargo ({pessoa['cargo']}): ").strip().lower()

        if nome.strip():
            pessoa['nome'] = nome

        if cpf.isdigit() and len(cpf) == 11:
            pessoa['cpf'] = cpf

        if idade.isdigit() and int(idade) > 0:
            pessoa['idade'] = idade

        if "@" in email and "." in email:
            pessoa['email'] = email

        if cep.isdigit() and len(cep) == 8:
            pessoa['cep'] = cep

        if telefone.isdigit() and len(telefone) in (10, 11):
            pessoa['telefone'] = telefone

        if cargo:
            if cargo in cargos_validos:
                pessoa['cargo'] = cargo
            else:
                print("Cargo inválido. Mantendo valor anterior.")

        print("Pessoa atualizada com sucesso!")
    else:
        print("Número inválido.")

def excluir_pessoa():
    listar_pessoas()
    if not pessoas:
        return

    entrada = input("Digite o número da pessoa para excluir: ")
    
    if not entrada.isdigit():
        print("Entrada inválida. Digite um número.")
        return

    indice = int(entrada) - 1

    if 0 <= indice < len(pessoas):
        confirm = input(f"Tem certeza que deseja excluir {pessoas[indice]['nome']}? (s/n): ")
        if confirm.lower() == 's':
            pessoas.pop(indice)
            print("Pessoa excluída com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Número inválido.")

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Editar Pessoa")
        print("4. Excluir Pessoa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
#teste alteração
