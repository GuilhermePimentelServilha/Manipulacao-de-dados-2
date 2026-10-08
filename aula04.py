def cadastrarjogador():
    nome = input("Digite seu nome: ")
    pontuacao = input("Digite sua pontuação: ")
 
    arquivo =open("Jogador.txt","a")
    arquivo.write(nome + "_" + pontuacao + "\n")
    arquivo.close()
 
    print("Jogador Salvo")
 
def verRanking():
    jogadores = []
    arquivo = open("jogadores.txt","r")
    linhas = arquivo.readline()
    arquivo.close()
 
    for linha in linhas:
        partes = linha.strip().split(" _ ")
        nome = partes[0]
        pontuacao = int(partes[1])
 
    jogadores.append((nome,pontuacao))
 
 
    jogadores.sort(key=lambda x: x[1], reverse=True)
    print("=== RANKING ===")
    posicao = 1
 
    for jogador in jogadores:
        print(posicao, "-", jogador[0], "-", jogador[1])    
        posicao += 1
 
    print("Total de Jogadores:", int(linhas))
 
def buscarjogador():
    nome_busca = input("digite o nome do jogador: ")
 
    arquivo = open("jogadores.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
 
    encontrado = False
 
    for linha in linhas:
        if nome_busca in linha:
            print("jogador encontrado:")
            print(linha)
            encontrado = True
 
    if not encontrado:
        print("jogador nao encontrado")
 
    encontrado = False
 
    for linha in linhas:
        if nome_busca in linha:
            print("jogador nao encontrado")
            print(linha)
            encontrado = True
 
        if not encontrado:
            print("jogador nao encontrado")

while True:
     print("1 - cadastrar jogador")
     print("2 - ver ranking")
     print("3 - buscar jogador")
     print("4 - sair ")
 
     opcao = input("escolha uma opção: ")
 
     if opcao == "1":
            cadastrarjogador()
     elif opcao == "2":
            verRanking()
     elif opcao == "3":
            buscarjogador()
     elif opcao == "4":
            print("saindo do sistema ......")
            break
     else:
            print("opção invalida")
           
                       
       
 
 
                         
 
