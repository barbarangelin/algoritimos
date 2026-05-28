
"""algoritimo guloso!"""
def maximizar_quantidade_de_arquivos(armazenamento_pendrive, arquivos):
    arquivos_escolhidos = []
    capacidade_preenchida = 0
    parada = False
    while capacidade_preenchida <= armazenamento_pendrive and parada == False:
        arquivos.sort()
        if arquivos[0] + capacidade_preenchida > armazenamento_pendrive:
            parada = True
        else:
            arquivos_escolhidos.append(arquivos[0])
            capacidade_preenchida+=arquivos.pop(0)

    return arquivos_escolhidos, capacidade_preenchida

arquivos =  [15, 20, 30, 30, 40, 50, 80, 100, 120, 200, 500, 900]

print(maximizar_quantidade_de_arquivos(1000,arquivos))







