import kostka
import lod

k = kostka(10)
lod1 = lod.Lod('Mnau', 100, 20, 18, k)
lod2 = lod.Lod('Haf', 100, 15, 22, k)

lod.utoc(lod2)
print (lod1.vypis_zpravu())
print (lod2.vypis_zpravu())