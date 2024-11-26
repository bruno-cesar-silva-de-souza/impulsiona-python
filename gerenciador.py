import csv
import os

CSV_FILE = 'contatos.csv'

def criar_contato(nome, email, telefone, endereco, data_nascimento):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, email, telefone, endereco, data_nascimento])
    print(f'Contato {nome} criado com sucesso!')

def listar_contatos():
    if not os.path.exists(CSV_FILE):
        print("Nenhum contato encontrado.")
        return

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignora o cabeçalho
        for row in reader:
            print(f'Nome: {row[0]}, Email: {row[1]}, Telefone: {row[2]}, Endereço: {row[3]}, Data de Nascimento: {row[4]}')

def atualizar_contato(nome_antigo, novo_nome, novo_email, novo_telefone, novo_endereco, nova_data_nascimento):
    contatos = []
    encontrado = False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        contatos = list(reader)

    for i, row in enumerate(contatos):
        if row[0] == nome_antigo:
            contatos[i] = [novo_nome, novo_email, novo_telefone, novo_endereco, nova_data_nascimento]
            encontrado = True
            break
    
    if encontrado:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contatos)
        print(f'Contato {nome_antigo} atualizado com sucesso!')
    else:
        print(f'Contato {nome_antigo} não encontrado.')

def deletar_contato(nome):
    contatos = []
    encontrado = False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        contatos = list(reader)

    contatos_novos = [row for row in contatos if row[0] != nome]

    if len(contatos_novos) < len(contatos):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contatos_novos)
        print(f'Contato {nome} deletado com sucesso!')
    else:
        print(f'Contato {nome} não encontrado.')

def menu_principal():
    while True:
        print("\n--- Gerenciador de Contatos ---")
        print("1. Criar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Deletar Contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            criar_contato(nome, email, telefone, endereco, data_nascimento)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            nome_antigo = input("Nome do contato a ser atualizado: ")
            novo_nome = input("Novo Nome: ")
            novo_email = input("Novo Email: ")
            novo_telefone = input("Novo Telefone: ")
            novo_endereco = input("Novo Endereço: ")
            nova_data_nascimento = input("Nova Data de Nascimento (DD/MM/AAAA): ")
            atualizar_contato(nome_antigo, novo_nome, novo_email, novo_telefone, novo_endereco, nova_data_nascimento)
        elif opcao == '4':
            nome = input("Nome do contato a ser deletado: ")
            deletar_contato(nome)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '_main_':
    menu_principal()