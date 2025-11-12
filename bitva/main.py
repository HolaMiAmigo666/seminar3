#!/usr/bin/env python3
from kostka import Kostka
from lod import Lod, stihac, Korveta

class Sektor:

    def __init__(self, jmeno, lod_1, lod_2, kostka):
        self._jmeno = jmeno
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka
    
    def _vypis_lod(self, lod):
        print(lod)
        print(f'Trup: {lod.graficky_trup(lod._trup, lod._max_trup)}')
        if isinstance(lod, stihac):
            print(f'Energie: {lod.graficka_energie()}')
    

    def souboj(self):
        import random
        print(f'Vitej v sektoru {self._jmeno}!')
        print(f'================={len(self._jmeno)*"="}')
        print()
        print(f'Dnes se stretnou {self._lod_1} a {self._lod_2}.')
        print('Zhajit souboj...')
        input()

        if random.randint(0, 1):
            self._lod_1, self._lod_2 = self._lod_2, self._lod_1

        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykreslit()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())
            self._vypis_lod(self._lod_2)

            if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykreslit()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())
                self._vypis_lod(self._lod_1)

    def _vypis_zpravu(self, zprava):
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(0.5)
    
    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])
    
    def _vykreslit(self):
        self._vycisti()
        print(f'============== Sektor {self._jmeno} ================')
        print('Lode:\n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()


if __name__ == '__main__':
    k = Kostka(30)
    l = Kostka(31)

    lod1 = Lod('Mnau', 100, 50, 22, l)
    lod2 = stihac('Haf', 100, 40, 20, l, 60, 40)
    
    smetanova_draha = Sektor("Smetanova draha", lod1, lod2, k)
    m = Sektor("muchomurka", lod1, lod2, k)
    smetanova_draha.souboj()
