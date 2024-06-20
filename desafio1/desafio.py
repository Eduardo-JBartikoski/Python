s = 'abcdefabcde'  # Correção: Combine as duas strings em uma única

if len(s) % 2 != 0:
    s += "_"

grupo = [s[i:i+2] for i in range(0, len(s), 2)]

print(grupo)  # Exibir os grupos resultantes