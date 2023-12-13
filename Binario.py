def obter_numero():
    """ Evita o usuário de colocar um input inválido. """
    while True:
        try:
            inteiro = int(input('Digite um número inteiro ou 0 para encerrar: '))
            return inteiro
        except ValueError:
            print('Número digitado inválido. Tente novamente.')

def converte_binario(num):
    """ Converte o número inteiro para binário e adiciona os 8 digitos. """
    binario_absoluto = bin(num & ((1 << 8) - 1))[2:]
    binario_completo = binario_absoluto.zfill(8)

    return binario_completo

def main():
    while True:
        inteiro = obter_numero()
        if inteiro == 0:
            break
        binario = converte_binario(inteiro)
        print(f'O {inteiro} em binário é {binario[:4]} {binario[4:]}')

if __name__ == '__main__':
    main()
