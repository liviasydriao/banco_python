'''criar duas novas funções, cadastrar usuário (cliente) e cadastrar conta corrente'''

def deposito(valor,saldo,extrato):
    

    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
            print("Operação falhou! O valor informado é inválido.")
            
    return extrato, saldo

def saque (valor, saldo, extrato,numero_saques,limite, LIMITE_SAQUES):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def obter_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome,cpf,endereco,data,usuarios):
    cpf_existe = False
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            print("usuário já existe, operação inválida!\n")
            cpf_existe = True
            break
    if not cpf_existe:
            usuarios.append({
                'nome':nome,
                'cpf':cpf,
                'endereco':endereco,
                'data':data
                })
    return usuarios

def criar_cc(cpf,usuarios,num_conta,contas):
    usuario = None
    for pessoa in usuarios:
        if cpf == pessoa['cpf']:
            usuario = pessoa
            break
    
    if usuario is None:
        print("Usuário não encontrado. Crie um usuário primeiro.")
        return contas
    
    for conta in contas:
        if num_conta == conta['num_conta']:
            print("Conta corrente já existe. Operação inválida.")
            return contas
    
    contas.append({
        'agencia': '0001',
        'num_conta': num_conta,
        'usuario': usuario['nome']  # Aqui pegamos apenas o nome do usuário para listar
    })
    return contas

def listar_contas(contas):
    print("\n================ CONTAS CORRENTES ================")
    for conta in contas:
        print(f"* O usuário {conta['usuario']} tem conta corrente de número {conta['num_conta']} e agência {conta['agencia']}\n")
    print("==================================================")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[cc] Cadastrar conta corrente
[l] Listar contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        extrato, saldo = deposito(valor,saldo,extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(valor, saldo, extrato,numero_saques)

    elif opcao == "e":
        obter_extrato(saldo, extrato)

    elif opcao == "c":
        cpf = int(input("Informe seu cpf: "))
        nome = input("Informe seu nome: ")
        endereco = input("Informe seu endereço: ")
        data = input("Informe sua data de nascimento: ")
        
        usuarios = criar_usuario(nome,cpf,endereco,data,usuarios)
        
    elif opcao == "cc":
        num_conta = int(input("Informe o numero da conta corrente: "))
        cpf = int(input("Informe seu cpf: "))
        
        contas = criar_cc(cpf,usuarios,num_conta,contas)     
        
    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
