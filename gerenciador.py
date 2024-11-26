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
        for row in reader:
            print(f'Nome: {row[0]}, Email: {row[1]}, Telefone: {row[2]}, Endereço: {row[3]}, Data de Nascimento: {row[4]}')

def atualizar_contato(nome_antigo, novo_nome, novo_email, novo_telefone, novo_endereco, nova_data_nascimento):
    if not os.path.exists(CSV_FILE):
        print("Nenhum contato encontrado.")
        return

    contatos = []
    encontrado = False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nome_antigo:
                contatos.append([novo_nome, novo_email, novo_telefone, novo_endereco, nova_data_nascimento])
                encontrado = True
            else:
                contatos.append(row)

    if encontrado:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contatos)
        print(f'Contato {nome_antigo} atualizado com sucesso!')
    else:
        print(f'Contato {nome_antigo} não encontrado.')

def deletar_contato(nome):
    if not os.path.exists(CSV_FILE):
        print("Nenhum contato encontrado.")
        return

    contatos = []
    encontrado = False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != nome:
                contatos.append(row)
            else:
                encontrado = True

    if encontrado:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contatos)
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
        
        try:
            opcao = input("Escolha uma opção: ").strip()
        except EOFError:  # Corrige erros no caso de EOF
            print("\nEntrada inválida. Tente novamente.")
            continue

        if opcao == '1':
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            telefone = input("Telefone: ").strip()
            endereco = input("Endereço: ").strip()
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()
            criar_contato(nome, email, telefone, endereco, data_nascimento)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            nome_antigo = input("Nome do contato a ser atualizado: ").strip()
            novo_nome = input("Novo Nome: ").strip()
            novo_email = input("Novo Email: ").strip()
            novo_telefone = input("Novo Telefone: ").strip()
            novo_endereco = input("Novo Endereço: ").strip()
            nova_data_nascimento = input("Nova Data de Nascimento (DD/MM/AAAA): ").strip()
            atualizar_contato(nome_antigo, novo_nome, novo_email, novo_telefone, novo_endereco, nova_data_nascimento)
        elif opcao == '4':
            nome = input("Nome do contato a ser deletado: ").strip()
            deletar_contato(nome)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu_principal()
