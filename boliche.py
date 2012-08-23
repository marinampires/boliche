def calcula(jogada):
    pontuacao = []
    ponto_anterior = 0
    ponto_mais_que_anterior = 0

    for ponto in jogada:
        if(ponto == "/"):
            pontuacao += 10 - int(ponto_anterior)
        elif(ponto == "X"):
            pontuacao += 10
        elif(ponto != "-"):
            pontuacao += int(ponto)
            if(ponto_anterior == "X" or ponto_mais_que_anterior == "X"):
                pontuacao += int(ponto)
        else:
            ponto = 0
        ponto_mais_que_anterior = ponto_anterior
        ponto_anterior = ponto
    return pontuacao
