#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mòdul *main*
============

El modul main.py conte el programa principal.
Aquest programa crea una instància de Receptari
i una instància d’Interpret juntament amb les
funcions que implementen les ordres necessaries.

A continuació, engega l’intèrpret. Aquest es va
comunicant interactivament amb l’usuari fins acabar
la sessió.

L’interpret ha de tenir les seguents ordres:

producte <nom> -- Receptari.afegeix_producte(nomp)
    Afegeix un producte al receptari que te nom <nom>.

recepta <nom> -- Receptari.afegeix_recepta(n)
    Afegeix una recepta al receptari que te nom <nom>.

ingredient <nomp> <nomr> <qua> -- Receptari.afegeix_ingredient_recepta(nomr,nomp,q)
    Afegeix <qua> grams de l’ingredient de nom <nomp> a la recepta de nom <nomr>.


print <ent> [<nom>]
    Escriu per pantalla segons el valor de <ent>. Si <ent> és:

    receptes
        Escriu la llista de noms de receptes del receptari.
    productes
        Escriu la llista de noms de producte del receptari.

    recepta
        Escriu els ingredients i la quantitat que intervenen en la recepta de nom <nom>.

    receptes-ing
        Escriu la llista de noms de recepta en les que participa l’ingredient anomenat <nom>.

    surt
    Acaba l’execució del programa.
'''



'''
AIXO VA PERFCTE, EL K PODREM fer es k al recuperar ho buidi tot o es mala idea?
** recupera prova2

** print receptes
pa-tom
pa-oli
gofre

** print productes
ous
oli
pa
tomàquet
llet

** print recepta gofre
100g llet
50g ous

**  pero aixó ja tira yeeeeeeeeeeh
'''


from receptari import*
from interpret import*


def printlist(ent = str(), nom = str()):
    if ent == 'receptes':
        for recepta in r.receptes():
            print recepta


    elif ent == 'productes':
        for producte in r.ingredients():
            print producte


    elif ent == 'recepta':
        if nom in r.receptes():
            for p, q in r.recepta(nom):
                print str(q)+'g', p

        else:
            if nom == '': print ('No has introduit cap recepta')

            else: print ("La recepta < %s > no existeix")%(nom)


    elif ent == 'receptes-ing':
        if nom in r.ingredients():
            for recepta in r.receptes_ingredient(nom):
                print recepta

        else:
            if nom == '': print ('No has introduit cap producte')
            else: print ("El producte < %s > no existeix")%(nom)


    else:
        print "Ordres i/o arguments no vàlids. Per més informació executi la comanda **help**"
'''

$ python main.py
Traceback (most recent call last):
  File "main.py", line 116, in <module>
    i = Interpret(r.recupera, r.desa) #S
AttributeError: 'Receptari' object has no attribute 'recupera' Això
ok
'''

if __name__ == '__main__':
    r = Receptari() # no sera el self.set_begin k sempre s'executa en el bucle?
    i = Interpret(r.obre, r.desa) #A veure, potser si
    i.set_prompt('**')

    i.afegeix_ordre('producte', r.afegeix_producte)
    i.afegeix_ordre('receptes', r.receptes)
    i.afegeix_ordre('recepta', r.afegeix_recepta)
    i.afegeix_ordre('ingredient', r.afegeix_ingredient_recepta)
    i.afegeix_ordre('print', printlist)
    i.afegeix_ordre('desa', r.desa)
    i.afegeix_ordre('recupera', r.obre)

    print "Recorda consultar el menu d'ajuda amb la comanda **help** per qualsevol dubte"
    print
    i.run()
