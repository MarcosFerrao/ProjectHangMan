import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS

def gerar_palavra_secreta():
    """
    Função para randomicamente seleconar uma palavra do arquivo texto
    :return: uma palavra aleatoria
    """

    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as file_object:
        palavra = file_object.read().splitlines()

    return random.choice(palavra)
