frase = "olá meu nome é eduardo tenho 27 anos"


grupos = [frase[i:i+2] for i in range(0,len(frase),2)]
if len(grupos) == 1:
    grupos += '_'
print (grupos)