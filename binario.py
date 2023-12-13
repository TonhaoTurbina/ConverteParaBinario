def obter_numero():
    """ Evita o usuário de colocar um input inválido. """
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
            if inteiro >= 0:
                return inteiro
            else:
                print('Número digitado inválido. Tente novamente.')
        except ValueError:
            print('Número digitado inválido. Tente novamente.')

def converte_binario(num):
    """ Converte o número inteiro para binário. """
    return bin(num)[2:]

def main():
    inteiro_positivo = obter_numero()
    binario = converte_binario(inteiro_positivo)
    print(f'O {inteiro_positivo} em binário é {binario}')

if __name__ == '__main__':
    main()
