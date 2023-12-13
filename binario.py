def obter_numero():
    """ Evita o usuário de colocar um input inválido. """
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
            return inteiro
        except ValueError:
            print('Número digitado inválido. Tente novamente.')

def converte_binario(num):
    """ Converte o número inteiro para binário e adiciona os 8 digitos. """
    if num >= 0:
        binario_absoluto = bin(num)[2:]
        binario_completo = binario_absoluto.zfill(8)
    else:
        binario_absoluto = bin(num & ((1 << 8) - 1))[2:]
        binario_completo = binario_absoluto.zfill(8)

    return binario_completo

def main():
    inteiro = obter_numero()
    binario = converte_binario(inteiro)
    print(f'O {inteiro} em binário é {binario[:4]} {binario[4:]}')

if __name__ == '__main__':
    main()
