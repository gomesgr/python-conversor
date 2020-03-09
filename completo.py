import collections as col
import time
import cv2
import pytesseract as ocr
import numpy as np
from PIL import Image

''' 
    Z E N I T values
    P O L A R keys
'''

class ZenitPolar:
    def __init__(self, arquivo):
        self.zenit_polar_dict = col.OrderedDict({'Z': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R', 'Í': 'Á', 'É': 'Ó'})
        self.arquivo = arquivo
        self.arquivo_zenit = open('zenit.txt', 'w')
        self.texto = ''

    def mostra_arquivo_leitura(self):
        print(self.arquivo.read())

    def separa_palavras(self):
        palavra_lista = []
        for paragrafo in self.arquivo:
            for palavra_string in paragrafo.split():
                palavra_lista.append( palavra_string )
        return palavra_lista

    def le_arquivo(self, arquivo):
        print(arquivo)
        
    # Criado por Gabriel R. Gomes
    # Conversor de textos para Zenit Polar
    # O método coleta a palavra individual maiúscula, no método transformar_zenit e, letra
    # por letra o converte se existir no dicionário 'zenit_polar_dict', para que não haja 
    # a conversão da mesma letra múltiplas vezes, usa-se 'enumerate()' para identificar cada
    # letra, mesmo que repetida, única no loop (contraditório porém é verdade).
    # Através do indice é possível então, identificar a posição da letra em questão
    def muda_zenit(self, palavra):
        for indice, letra in enumerate(palavra):
            print(f'A palavra é: {palavra}')
            for zenit, polar in self.zenit_polar_dict.items():
                if (zenit in letra):
                    print('Trocou ' + palavra[indice], end='')
                    palavra[indice]=(polar)
                    print(' por ' + polar)
                if polar in letra:
                    print('Trocou ' + palavra[indice], end='')
                    palavra[indice]=(zenit)
                    print(' por ' + zenit)
        return ''.join(palavra)
    
    # O método a seguir individualiza as palavras e as transforma puramente 'uppercase' (caixa alta)
    # facilitando assim a conversão do texto. Infelizmente a notação original pode e vai
    # mudar, no entando, funciona muito bem
    # O 'for' coleta cada palavra individualmente, as transforma em uppercase, e, se o contador
    # for divisível por 10, ou seja, de 10 em 10 palavras, será inserido uma quebra de linha,
    # a cada 100, um parágrafo é gerado.
    # Quando gerado (parágrafo), a primeira letra será sempre maiúscula, dando ao texto um tom
    # mais coerente de acordo com as normas de linguagem.
    def transformar_zenit(self):
        lista_palavras = self.separa_palavras()
        cont = 0
        for palavra in lista_palavras:
            resultado = self.muda_zenit(list(palavra.upper()))
            if cont % 10 == 0 and cont != 0:
                self.texto += '\n'
                # self.arquivo_zenit.write('\n')
            if cont % 100 == 0:
                self.texto += '\r'
                self.texto += str(resultado).capitalize() + ' '
                # self.arquivo_zenit.write('\r')
                # self.arquivo_zenit.write(str(resultado).capitalize() + ' ')
            else:
                self.texto += str(resultado).lower() + ' '
                # self.arquivo_zenit.write(str(resultado).lower() + ' ')
            cont += 1
        self.arquivo_zenit.write(self.texto)
        self.arquivo_zenit.close()
        print(self.texto)

class Transformador:
    def __init__(self, imagem, caminho):
        self.imagem = imagem
        self.caminho = caminho
    
    def transformar_em_texto(self):
        texto = ocr.image_to_string(self.imagem)
        # arquivo = open(self.caminho, 'w+')
        with open(self.caminho, 'w+') as arquivo:
            arquivo.write(texto)
        


if __name__ == '__main__':
    # Configurando local do tesseract
    ocr.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    caminho = 'fotos_leitura/unicid.jpg'

    imagem_lida = Image.open(caminho)
    imagem_convertida = np.array(imagem_lida)
    imagem_cinza = cv2.cvtColor(imagem_convertida, cv2.COLOR_BGR2GRAY)
    imagem_canificada = cv2.Canny(imagem_cinza, 20, 100)
    imagem_embacada = cv2.blur(imagem_canificada, (2, 2))

    # o caminho onde o texto da imagem sera guardado
    caminho_gerado = 'gerado_da_foto.txt'

    transformador = Transformador(imagem_lida, caminho_gerado)
    tempo_antes_conv = time.time()
    transformador.transformar_em_texto()
    tempo_depois_conv = time.time()

    arquivo = ZenitPolar(open(transformador.caminho, 'r'))
    tempo_antes = time.time()
    arquivo.transformar_zenit()
    print(f'Tradução feita em : {(time.time() - tempo_antes):.3f}s\nConversão feita em {(tempo_depois_conv - tempo_antes_conv):.3f}s')
