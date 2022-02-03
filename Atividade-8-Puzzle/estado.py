class Estado:
    goal = [1, 2, 3, 4, 0, 5, 6, 7, 8] 
    #isso precisa ser alterado manualmente caso o N mude
    #por exemplo, precisa ser [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] com n = 4.
    
    def __init__(self, estado, pai, direcao, profundidade, custo):
        self.estado = estado
        self.pai = pai
        self.direcao = direcao
        self.profundidade = profundidade

        if pai:
            self.custo = pai.custo + custo

        else:
            self.custo = custo

            
            
    def sucesso(self):
        if self.estado == self.goal:
            return True
        return False          
                    


    @staticmethod
    
    def movimentos_possiveis(x,n): 
        movimentos = ['Direita', 'Esquerda', 'Cima', 'Baixo']
        if x % n == 0:
            movimentos.remove('Direita')
        if x % n == n-1:
            movimentos.remove('Esquerda')
        if x - n < 0:
            movimentos.remove('Cima')
        if x + n > n*n - 1:
            movimentos.remove('Baixo')

        return movimentos

    def expandir(self , n): 
        x = self.estado.index(0)
        movimentos = self.movimentos_possiveis(x,n)
        
        filhos = []
        for direcao in movimentos:
            temp = self.estado.copy()
            if direcao == 'Direita':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direcao == 'Esquerda':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direcao == 'Cima':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direcao == 'Baixo':
                temp[x], temp[x + n] = temp[x + n], temp[x]
            filhos.append(Estado(temp, self, direcao, self.profundidade + 1, 1))
        return filhos

    
    def solucao(self):
        movimentos = []
        solucao = []
        solucao.append(self.direcao)
        path = self
        while path.pai != None:
            movimentos.append(path.estado)
            path = path.pai
            solucao.append(path.direcao)
        solucao = solucao[:-1]
        solucao.reverse()
        movimentos.reverse()
        return solucao,movimentos