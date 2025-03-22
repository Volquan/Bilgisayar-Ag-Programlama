class Hesap:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

    def bol(self):
        return self.sayi1 / self.sayi2

    def toplama(self):
        return self.sayi1 + self.sayi2

    def cikarma(self):
        return self.sayi1 - self.sayi2

    def sonuc(self):
        print("carpma sonucu:", self.carp())
        print("bölme sonucu:", self.bol())
        print("toplama sonucu:", self.toplama())
        print("cıkarma sonucu:", self.cikarma())


sayi1 = int(input("birinci sayıyı gir: "))
sayi2 = int(input("ikinci sayıyı gir: "))


hesap = Hesap(sayi1, sayi2)
hesap.sonuc()
