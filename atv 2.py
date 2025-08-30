tarefas = []

def adicionar_tarefa():
    print("\n === Add de Tarefas ===")
    descricao = input("Digite a descrição da tarefa: ")
    
    tarefa = {
        "descricao": descricao,
        "status": "pendente"
    }
    
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas():
    print("\n === Lista de tarefas ===")
    
    if not tarefas:
        print("Não há tarefas cadastrada")

    for i, tarefa in enumerate(tarefas, start=1):
      print(f"{i}. {tarefa['descricao']} - {tarefa['status']}")

def concluir_tarefa():
    listar_tarefas()

    while True:
      num_tarefa = int(input("Número da tarefa para concluir: ")) -1

      if 0 <= num_tarefa < len(tarefas):
        tarefas[num_tarefa]["status"] = "concluída"
        print("Tarefa concluída!")
        break
      else:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()

    while True:
      indice = int(input("Escolha o número da tarefa que quer remover: ")) - 1

      if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print(" Tarefa removida com sucesso!")
            break
      else:
         print("Número inválido.")
         

def filtrar_tarefas():
    listar_tarefas()

    print()
    
    status = input("Digite o status para filtrar (pendente/concluida): ")
    
    for tarefa in tarefas:
        if tarefa['status'] == status:
            print(f"{tarefa['descricao']} - {tarefa['status']}")


def Menu():
    print("\n === Menu ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Filtrar tarefas por status")
    print("6. Sair")

while True:
    Menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        filtrar_tarefas()
    elif opcao == "6":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")