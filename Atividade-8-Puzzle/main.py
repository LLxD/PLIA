from busca import BFS, DFS
n = 3
print("Insira sua matriz",n,"*",n)
raiz = []
for i in range(0,n*n):
    print("Digite o número",i+1)
    p = int(input())
    raiz.append(p)

print("Estado inicial: ", raiz)


def inversoes(matriz):
    contador = 0
    for i in range(len(matriz)-1):
        for j in range(i+1 , len(matriz)):
            if (( matriz[i] > matriz[j]) and matriz[i] and matriz[j]):
                contador += 1
    return contador

def decifravel(puzzle):
    contador_inversoes = inversoes(puzzle)
    if (contador_inversoes %2 ==0):
        return True
    return False


#1,8,2,0,4,3,7,6,5 é resolvível
#1,3,4,5,2,0,6,8,7 também
#2,1,3,4,5,6,7,8,0 não é resolvível

if decifravel(raiz):
    print("Decifrando... \n")
    DFS_solucao = DFS(raiz, n)
    print('Solução usando BUSCA EM PROFUNDIDADE: ', DFS_solucao[0])
    print('Número mínimo de movimentos: ', len(DFS_solucao[0][0]))
    print('Número de nós explorados: ', DFS_solucao[1]) 
    BFS_solucao = BFS(raiz, n)
    print('Solução usando BUSCA EM LARGURA: ', BFS_solucao[0][0])
    for passos in BFS_solucao[0][1]:
        print(passos)
    print('Número mínimo de movimentos: ', len(BFS_solucao[0][0]))
    print('Número de nós explorados: ', BFS_solucao[1])    
          
    
    
else:
    print("Não decifrável")


