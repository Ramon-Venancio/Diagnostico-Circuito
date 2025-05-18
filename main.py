def salvarArquivo(C):
    with open('C1.txt','w') as arquivo:
        arquivo.write(str(C))
    print("Arquivo salvo com sucesso!\n")

def testarCombinação():
    return 0

def decimal_para_bits(decimal, num_bits):
    bits = []
    for _ in range(num_bits):
        bits.append(decimal % 2)
        decimal = decimal // 2
    return bits[::-1]

def gerarCombinacoe(nComb,nEnt):
    combinacoe = []

    for decimal in range(nComb):
        combinacoe.append(decimal_para_bits(decimal, nEnt))

    return combinacoe

def criarTV():
    circuito = eval(open("C1.txt").read())
    entradas = circuito['entradas']
    saidas = circuito['saidas']
    gates = {}
    for gate in circuito['gates']:
        gates[f'{gate}'] = 0
        # gates[f'{gate}'].append(circuito[f'{gate}'])
        # gates[f'{gate}'].append(0)

    TV = ""
    quantCombinacoes = 2^len(entradas)
    quantEntradas = len(entradas)

    for e in entradas:
        TV += f'{e} '
    TV += "| Saida"
            
    for linhaBits in gerarCombinacoe(quantCombinacoes, quantEntradas):
        for gate in circuito['gates']:
            for j in circuito[f'{gate}']:
                for index,k in enumerate(entradas):
                    if (k == j):
                        print("")


def menu():
    circuito = {'entradas':['A','B','C'],'saidas':['Y'],'gates':['g1','g2', 'g3'],'g1':['nand','y1','A','B'],'g3':['and','Y','B','y1','y2'],'g2':['not','y2','C']}

    while (True):
        perg = int(input("O que você quer?\n[1] Salvar um circuito\n[2] Criar uma TV (Tabela Verdade)\n[3] Verificar defeito em circuito\n[4] Sair do programa\n: "))

        if (perg == 1):
            salvarArquivo(circuito)
        elif (perg == 2):
            criarTV()
        elif (perg == 3):
            print("Não criado ainda")
        elif (perg == 4):
            break
        else:
            print("Digite um valor valido!")

def testes():
    combinacoes = gerarCombinacoe(16, 4)
    for i in combinacoes:
        print(f'{i}: {operacoeLogicas['nor'](*i)}')


operacoeLogicas = {
    "and": lambda *args: all(args),
    "or": lambda *args: any(args),
    "not": lambda a: not a,
    "nand": lambda *args: not all(args),
    "nor": lambda *args: not any(args),
    "xor": lambda *args: print(args),
    "nxor": lambda *args: print(args)
}
testes()
# menu()