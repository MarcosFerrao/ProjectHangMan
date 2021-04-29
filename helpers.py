import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS


def gerar_palavra_secreta():
    """
    Função para randomicamente seleconar uma palavra do arquivo texto
    :return: uma palavra aleatoria
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as file_object:
        palavras = file_object.read().splitlines()
    return random.choice(palavras)


def verifica_letra_informada(palavra_secreta, suas_tentativas, tentativa):
    """
    Verificar se a letra dada está correta
    :param palavra_secreta:  Gerada com base no arquivo texto de plaras secretas.
    :param suas_tentativas:  Lista com todas as tentativas.
    :param tentativas: letras inseridas nesta jogada
    :return: retorna um status
    """
    status = '' # o estatus precisa ser zerad toda vz que for chamado.
    acertos = 0 # tambem precisa ser zerado para cada tentativa.

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra # random word (Peru) letra informada 'e' mostra *e**
        else:
            status += '*'
        if letra.lower() == tentativa.lower():
            acertos += 1
    print(f"\n - Acertou {acertos} letra(s) '{tentativa}'")

    return status

def total_tentativas(palavra_secreta):
    """
    Esta função define a quantidade de tentativas de acordo com a palavra secreta
    :param palavra_secreta: palavra erada aleatoriamente
    :return: Quantidade de tentativas
    """
    chances = len(palavra_secreta)
    return chances + TENTATIVAS_ADICIONAIS