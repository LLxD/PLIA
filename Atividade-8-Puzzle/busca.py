from estado import Estado
from queue import Queue
from queue import LifoQueue


#BUSCA EM LARGURA
def BFS(estado_atual , tamanho):
    raiz = Estado(estado_atual, None, None, 0, 0)
    if raiz.sucesso():
        return raiz.solucao()
    fila = Queue()
    fila.put(raiz)
    explorados = []
    
    while not(fila.empty()):
        noh_atual = fila.get()
        explorados.append(noh_atual.estado)
        
        filhos = noh_atual.expandir(tamanho)
        for filho in filhos:
            if filho.estado not in explorados:
                if filho.sucesso():
                    return filho.solucao(), len(explorados)
                fila.put(filho)
    return

#BUSCA EM PROFUNDIDADE COM LIMITAÇÃO DE PROFUNDIDADE
def DFS(estado_atual , n): 
    raiz = Estado(estado_atual, None, None, 0, 0)
    if raiz.sucesso():
        return raiz.solucao()
    fila = LifoQueue()
    fila.put(raiz)
    explorados = []
    
    while not(fila.empty()):
        noh_atual = fila.get()
        profundidade_maxima = noh_atual.profundidade
        explorados.append(noh_atual.estado)
        
        if profundidade_maxima == 30:
            continue

        filhos = noh_atual.expandir(n)
        for filho in filhos:
            if filho.estado not in explorados:
                if filho.sucesso():
                    return filho.solucao(), len(explorados)
                fila.put(filho)
    return ("Não foi encontrada solução com a profundidade máxima atual", len(explorados))