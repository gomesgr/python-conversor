# coding: utf-8

import collections as col
import time

''' 
    Z E N I T values
    P O L A R keys
'''


class ZenitPolar:
    def __init__(self, arquivo):
        self.zenit_polar_dict = col.OrderedDict({'Z': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R', 'Í': 'Á', 'É': 'Ó'})
        self.arquivo = arquivo
        self.arquivo_zenit = ''

    def mostra_arquivo_leitura(self):
        print(self.arquivo.read())

    def separa_palavras(self):
        palavra_lista = []
        for paragrafo in self.arquivo:
            for palavra_string in paragrafo.split():
                palavra_lista.append(palavra_string)
        return palavra_lista

    def le_arquivo(self, arquivo):
        print(arquivo)

    def cria_arquivo(self, nome_arquivo):
        self.arquivo_zenit = open('arquivos_txt\\' + nome_arquivo + '.txt', 'w+')
        return self.arquivo_zenit

    # Criado por Gabriel R. Gomes
    # Conversor de textos para Zenit Polar
    def muda_zenit(self, palavras):
        palavras = list(palavras)
        for letra, objeto in enumerate(palavras):
            print(f'A palavra é: {palavras}')
            for zenit, polar in self.zenit_polar_dict.items():
                if zenit in objeto:
                    print('1 Trocou ' + palavras[letra], end='')
                    palavras[letra] = polar
                    print(' por ' + polar)
                if polar in objeto:
                    print('2 Trocou ' + palavras[letra], end='')
                    palavras[letra] = zenit
                    print(' por ' + zenit)
        return ''.join(palavras)

    #
    #  
    def transformar_zenit(self):
        if not self.arquivo_zenit:
            print('Diretório inexistente')
            return
        lista_palavras = self.separa_palavras()
        cont = 0
        for palavra in lista_palavras:
            resultado = self.muda_zenit(palavra.upper())
            if cont % 10 == 0 and cont != 0:
                self.arquivo_zenit.write('\n')
            if cont % 100 == 0:
                self.arquivo_zenit.write('\r')
                self.arquivo_zenit.write(str(resultado).capitalize() + ' ')
            else:
                self.arquivo_zenit.write(str(resultado).lower() + ' ')
            cont += 1


zenit_polar = ZenitPolar(open('arquivos_txt\\wiki_cafe_mania.txt', 'r'))
tempo_antes = time.time()
arq = zenit_polar.cria_arquivo('Arquivo Zenit')
zenit_polar.transformar_zenit()
print(f'Done in {(time.time() - tempo_antes):.3f}s')
