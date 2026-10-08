def cadastrarjogador():
    nome = input("Digite seu nome: ")
    pontuacao = input("Digite sua pontuacao: ")
    arquivo = open("jogadores.txt", "a")
    # Correção: Ajustado para " - " com espaços para bater com a leitura do ranking
    arquivo.write(nome + " - " + pontuacao + "\n")
    arquivo.close()
    print("Jogador salvo com sucesso!\n")


def verRanking():
    jogadores = []
    try:
        arquivo = open("jogadores.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        print("Nenhum jogador cadastrado ainda.\n")
        return

    for linha in linhas:
        if " - " in linha:
            partes = linha.strip().split(" - ")
            nome = partes[0]
            pontuacao = int(partes[1])
            jogadores.append((nome, pontuacao))

    jogadores.sort(key=lambda x: x[1], reverse=True)

    print("\n=== RANKING ===")
    posicao = 1
    for jogador in jogadores:
        print(f"{posicao} - {jogador[0]} - {jogador[1]}")
        posicao += 1
    print("Total de jogadores:", len(linhas), "\n")


def buscarjogador():
    nome_busca = input("Digite o nome do jogador: ")
    try:
        arquivo = open("jogadores.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        print("Nenhum jogador cadastrado ainda.\n")
        return

    encontrado = False
    print("\n=== RESULTADO DA BUSCA ===")
    for linha in linhas:
        if nome_busca.lower() in linha.lower():
            print(linha.strip())
            encontrado = True

    if not encontrado:
        print("Jogador nao encontrado.")
    print()


# Menu Principal
while True:
    print("1 - Cadastrar jogador")
    print("2 - Ver ranking")
    print("3 - Buscar jogador")
    print("4 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrarjogador()
    elif opcao == "2":
        verRanking()
    elif opcao == "3":
        buscarjogador()
    elif opcao == "4":
        print("Saindo do sistema.......")
        break
    else:
        print("Opcao invalida!\n")
