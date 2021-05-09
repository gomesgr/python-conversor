class ZenitPolar:
    def __init__(self):
        self.zenit_polar_dict = {'Z': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R', 'Í': 'Á', 'É': 'Ó',
            'z': 'p', 'e': 'o', 'n': 'l', 'i': 'a', 't': 'r'}


    def encriptar(self, palavra):
        """            
            # Criado por Gabriel R. Gomes
            # Conversor de textos para Zenit Polar
            # O método coleta a palavra individual e letra por letra o converte se existir no 
            # dicionário 'zenit_polar_dict', para que não haja a conversão da mesma letra 
            # múltiplas vezes, usa-se 'enumerate()' para identificar cada
            # letra, mesmo que repetida, única no loop (contraditório porém é verdade).
            # Através do indice é possível então, identificar a posição da letra em questão
        """
        letras = list(palavra)
        for indice, objeto in enumerate(letras):
            for zenit, polar in self.zenit_polar_dict.items():
                if zenit in objeto:
                    letras[indice] = polar
                if polar in objeto:
                    letras[indice] = zenit
        return ''.join(letras)


if __name__ == '__main__':
    zenit_polar = ZenitPolar()
    print(zenit_polar.encriptar('qUeIjO'))
