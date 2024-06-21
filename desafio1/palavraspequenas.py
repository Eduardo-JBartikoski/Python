def find_short(s):
    # your code here
    palavras = s.split()
    comprimento_minimo = len(palavras[0])
    
    for palavra in palavras:
        comprimento_atual = len(palavra)
        if comprimento_atual < comprimento_minimo:
            comprimento_minimo = comprimento_atual
    return comprimento_minimo # l: shortest word length