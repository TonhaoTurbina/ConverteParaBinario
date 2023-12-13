def obter_numero_positivo():
    """Evita o usuário de colocar um input inválido."""
    while True:
        try:
            inteiro = int(input('Digite um número inteiro não negativo: '))
            if inteiro >= 0:
                return inteiro
            else:
                print('Número digitado inválido. Tente novamente.')
        except ValueError:
            print('Número digitado inválido. Tente novamente.')

def inverter_string(string):
    """Inverte uma string."""
    return string[::-1]

def converte_binario(num):
    """Converte o número inteiro para binário."""
    return bin(num)[2:]

def main():
    inteiro = obter_numero_positivo()
    binario = converte_binario(inteiro)
    binario_reverso = inverter_string(binario)
    print(f'O {inteiro} em binário é {binario_reverso}')

if __name__ == '__main__':
    main()
