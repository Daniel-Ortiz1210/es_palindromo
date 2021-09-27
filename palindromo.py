def es_palindromo(texto):
    texto_original = texto
    texto = texto.lower()
    texto = texto.replace(" ", "")
    if texto[::] == texto[::-1]:
        print(texto_original + ' es palíndromo')
    else:
        print(texto_original + ' no es palíndromo')
    
if __name__ == '__main__':
    es_palindromo('Alli ves Sevilla')
    es_palindromo('Anita lava la tina')
    es_palindromo('Mi mama me mima')
    es_palindromo('Tres tristes tigeres')
    es_palindromo(input('Escribe tu propia palabra o frase: '))