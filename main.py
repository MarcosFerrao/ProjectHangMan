from helpers import gerar_palavra_secreta, jogo

if __name__ == '__main__':
    palavra_secreta = gerar_palavra_secreta()
   #print(palavra_secreta) sem esse comentario é possivel ver  palavra secreta.
    # for loop que imprim palavras escondicda com *****
    print("\n==== JOGO DA FORCA ====")
    print("\nA palavra é: \n")
    for letra in palavra_secreta:
        print("*", end=" ")

    # calculando o tamanho da palavra
    tamanho_palavra = len(palavra_secreta)
    print(f"\nDica: A palavra tem {tamanho_palavra} letras")

    jogo(palavra_secreta)
