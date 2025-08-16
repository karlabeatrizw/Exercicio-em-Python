# Programa com uma tupla com varias palavra
# Programa deve mostrar para cada palavra as suas vogais

palavras = ('vogais','boca','dizer','contar','inventar','assobiar','brincadeira')

vogais = 'aeiouAEIOU'

for palavra in palavras: #vai separar as paravras
    apenas_vogais = '' # variavel para add as vogais
    for letra in palavra: # vai verificar a palavra por palavra separadamente
        if letra in vogais: # se a letra for uma vogal ele vai juntar com as outras vogais
            apenas_vogais += letra

    print(palavra, "->", apenas_vogais)