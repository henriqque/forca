import random
#importa uma biblioteca já existente

palavras = ['abacate','chocolate','paralelepipedo','goiaba']
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def principal():
    #Função principal do programa
    print('F O R C A')

    palavraSecreta = sortearPalavra()
    #atribui uma função a uma variavel
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break
        #duas funções inseridas em um if, para quando o jogador perder ou vencer o jogo o programa parar
        
def perdeuJogo():
    global FORCAIMG
    #insere uma função global,que é uma função que serve para todo o programa
    if len(letrasErradas) == len(FORCAIMG):
        return True
    else:
        return False
    #diz ao programa que caso o número de letras erradas seja o mesmo de desenhos da forca, retornar true ou false para que o jogo continue ou acabe
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False
    #diz ao programa que caso a letra digitada esteja na palavra, dar true e se não tiver dar false
    return ganhou        
    #return é usado para indicar o que vai retornar quando chamar a função
    #caso todas as letras estejam certas indica que você ganhou


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    #pede ao jogador para que digite uma letra que ele acredite ter na palavra
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    #alerta ao jogador que só pode digitar uma letra, caso ela digite mais de uma
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    #alerta ao jogador que ele já digitou a letra anteriormente
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    #alerta ao jogador que só se pode digitar letras caso ele digite um número ou outro caractere
    else:
        return palpite
    #caso nenhum erro seja cometido retorna a letra digitada a função
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    #caso a letra esteja errada, desenha outra parte do boneco na forca
    
     
    vazio = len(palavraSecreta)*'-'
    #adiciona um "-" em cada espaço de uma letra não digitada
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
        #caso a letra esteja correta, adiciona a letra ao conjunto das letras certas
    else:
        letrasErradas += palpite
        #caso a letra esteja errada, adiciona a letra ao conjunto das letras erradas
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) #printa na tela as letras corretas já digitadas
    print('Erros: ',letrasErradas) #printa na tela as letras erradas já digitadas
    print(vazio) #printa na tela as letras já adivinhadas e os "-" no lugar das letras ainda não adivinhadas
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()
#sorteia uma palavra da biblioteca criada com as palavras escolhidas

    
principal()
