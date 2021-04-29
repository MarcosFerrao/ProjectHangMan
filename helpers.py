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
    status = ''  # o estatus precisa ser zerad toda vz que for chamado.
    acertos = 0  # tambem precisa ser zerado para cada tentativa.

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra  # random word (Peru) letra informada 'e' mostra *e**
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


def jogo(palavra_secreta):
    """
    Função principal do jogo
    :param palavra_secreta: palavra secreta gerada a partir do arquivo texto
    :return:
    """
    chute = 0
    adivinhado = False
    suas_tentativas = []
    chances = total_tentativas(palavra_secreta)
    total_chances = chances

    print(f"Total de chances: {chances}")
    while chute < total_chances:
        letra_tentativa = input("\nInforme uma letra: ")

        # diminui as chances 1 a cada letra informada.
        chances -= 1

        # se a letra já foi informada ou adivnhada
        if letra_tentativa in suas_tentativas:
            print(f" *** ATENÇÃO ***\n Você já tentou essa letra.")
            pass
        elif len(letra_tentativa) == 1:  # precisa ser 1 letra somente na tentativa
            suas_tentativas.append(letra_tentativa)  # Adicionando as letras no local correto da palavra
            resultado = verifica_letra_informada(palavra_secreta, suas_tentativas, letra_tentativa)
            if resultado == palavra_secreta:
                adivinhado = True
                print(f"\n=== Parabéns, você venceu! A palavra é: '{palavra_secreta}'. ===")
                break
            else:
                print(f" - {' '.join(resultado)}")
        else:
            print(f"Entrada incorreta, informe somente '1' letra")

        print(f" - Tentativas restantes: {chances}")  # Mostra quantas tentativas restam
        chute += 1

    if chute == total_chances:
        print(f"*** Suas chances acabaram. A palavra secreta é : '{palavra_secreta}' ***")
