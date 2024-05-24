def converter_lista_para_string(lista):
    titulo = []
    
    maiuscula = True
    
    for char in lista:
        if char == "/":
            titulo.append(" ")
            maiuscula = True
        else:
            if maiuscula:
                titulo.append(char.upper())
                maiuscula = False
            else:
                titulo.append(char)
    
    return "".join(titulo)

letras = ["e", "s", "q", "u", "e", "c", "e", "r", "a", "m", "/", "d", "e", "/", "m", "i", "m"]
print(converter_lista_para_string(letras))

def pares_e_impares(numeros):
    pares = []
    impares = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    
    return [pares, impares]

numeros = [1, 3, 5, 2, 4]
print(pares_e_impares(numeros))

def cria_matriz(m, n):
    matriz = []
    
    contador = 1
    
    for i in range(m):
        linha = []
        
        for j in range(n):
            linha.append(contador)
            contador += 1
        
        matriz.append(linha)
    
    return matriz

m = 2
n = 3
print(cria_matriz(m, n))

def filtrar_palavras(frase, letra):
    palavras = frase.split()
    
    palavras_filtradas = []
    
    for palavra in palavras:
        if letra.lower() in palavra.lower():
            palavras_filtradas.append(palavra)
    
    return palavras_filtradas

frase = "Afonso acertou a cerca ontem"
letra = "a"
print(filtrar_palavras(frase, letra))

eh_perfeito = lambda num: num == sum([i for i in range(1, num) if num % i == 0])

numero = 6
print(eh_perfeito(numero))

