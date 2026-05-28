

def questaoUm (numero):
    if numero > 0:
        resto = int(numero%10)
        numero = int(numero / 10)
        return str(resto) + questaoUm(numero)
    else:
        return ""
    
def questaoDois(vetorInteiros):
    if len(vetorInteiros) > 0:
        soma = vetorInteiros.pop(0)
        return soma + questaoDois(vetorInteiros)
    else:
        return 0
    
def questaoTres(N):
    if N > 0:
        return N + questaoTres(N-1)
    else: return 0
    
def questaoQuatro(vetorVinteElementos):
    if len(vetorVinteElementos) > 0:
        novoVetor = []
        novoVetor.append(vetorVinteElementos.pop(-1))
        return  novoVetor + questaoQuatro(vetorVinteElementos)
    else:
        return []
    
def questaoCinco(K, N):
    if N > 0:
        resto = N % 10
        N = int(N / 10)
        if K == resto:
            return 1 + questaoCinco(K, N)
        else:
            return questaoCinco(K, N)
    else:
        return 0
    
def questaoSeis (n1, n2):
    if n2 > 0:
        return n1 + questaoSeis(n1, n2-1)
    else: return 0

def questaoSete (N):
    if N < 0:
        return 
    questaoSete(N-1)
    print(N)

def questaoOito(N):
    if N >= 0:
        print(N)
        return questaoOito(N-1)
    

def questaoNove(N):
    if N < 0:
        return
    questaoNove(N-1)
    if N % 2 == 0:
        print(N)

def questaoDez(N):
    if N >= 0:
        if N % 2 == 0:
            print(N)
        return questaoNove(N-1)
    
def questaoOnze(N):
    if N > 0:
        if N % 2 == 1:
            return N * questaoOnze(N-1)
        else:
            return questaoOnze(N-1)
    else:
        return 1
    
    
def questaoDoze(N):
    if N > 0:
        fatorialN = questaoDozeSegundaFuncao(N)
        return fatorialN * questaoDoze(N-1)
    else:
        return 1
    
def questaoDozeSegundaFuncao(N):
    if N > 0:
        return N * questaoDozeSegundaFuncao(N-1)
    else:
        return 1


vetor = [1,2,3,4,5]    


print(questaoDoze(4))