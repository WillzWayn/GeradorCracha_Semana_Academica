import qrcode                                            #Biblioteca para criação do QrCode
from PIL import Image, ImageTk, ImageFont, ImageDraw     #Manipulação de Imagens


#########################

# Variaveis de tamanhos EM MM
mm = 3.7795275591 #  1 mm = 3.78 px

tamanhoPapelCracha = (int(210*mm)+1,int(297*mm)+1) #Recomendo deixar em A4 para ganhar mais qualidade na impressão
tamanhoQR = (int(40*mm)+1,int(40*mm)+1)
xDoPapel = int(140*mm)+1
yDoPapel = int(35*mm)+1

###########################

# Variaveis de posição

posicaoQR = (10,575)

posicaoAlturaNome = (530)
posicaoAlturaUniv = (600)

##########################


#Dentro da lista TXT existe uma separação do nome e universidade, qual caracter é usado para separar?
#ex: William Wayn_UFRRJ, Vai separar William Wayn e UFRRJ
carac = '_'

#######################


### NOME DO ARQUIVO COM A FOTO DO CRACHA
nomeCracha = 'crach2.png'

def escritoNoqr():
    return nome

 

## LOOP, Abre um arquivo LISTA e pega os nomes separados pela tecla enter e armazena em jv
with open("LISTA.txt") as f:
    for line in f:
        cracha = Image.open(nomeCracha)
        cracha = cracha.resize(tamanhoPapelCracha, Image.ANTIALIAS)
        print ('Gerando o crachá:',line.replace('\n','').split('_'))    #Printa o nome que será feito o cracha no terminal 
        
        jv=line.replace('\n','') # Separa as linhas do texto
        jv = jv.split('_') #No arquivo lista.txt deixei NOME_UNIV, usando esse comando, ele cria um vetor com NOME, UNIV
        #onde jv[0] vai ser o nome da pessoa, e jv[1] a universidade
        univ = jv[1] # cria uma variavel chamada univ
        nome = jv[0]  #como ja tinha feito o codigo todo e adicionei a universidade depois, mudei o nome da variavel jv[0] p jv. ai nao precisei mexer no codigo
        #tamanho do nome para shiftar na etiqueta
        
     
        #ESSAS ALTERAÇÕES FORAM FEITAS PARA CENTRALIZAR O NOME NA ETIQUETA
        tamNome = len(nome)*4+10
        tamUniv = len(univ)*4  
        
        ##############
        ##GERANDO Qr##
        ##############
        
        imgQr = qrcode.make(escritoNoqr()) #Cria QR
        imgQr = imgQr.resize(tamanhoQR, Image.ANTIALIAS) #Muda tamanho do QR
        
        cracha.paste(imgQr,posicaoQR) #Cola a posição do QR
        font = ImageFont.truetype("arial.ttf", 25)
        draw = ImageDraw.Draw(cracha) ####
        draw.text(((xDoPapel-tamanhoQR[0])/2 + tamanhoQR[0] - tamNome+40, yDoPapel/2+posicaoAlturaNome), nome ,(0,0,0), font=font) ## NOME
        draw.text(((xDoPapel-tamanhoQR[0])/2 + tamanhoQR[0] - tamUniv+40, yDoPapel/2+posicaoAlturaUniv), univ, (255,0,0), font=font)
        cracha.save('Crachas Gerados/'+nome+'.png')
        
        
