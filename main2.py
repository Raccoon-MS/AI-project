import numpy as np
import random as rnd
import math
import time


class NeuroneEntre(object):
    """docstring for NeuroneEntre."""

    def __init__(self, taux ,coef, id):
        self.taux = taux
        self.id=id
        self.coef=coef
        self.erreur=0.0
        self.somme=0.0
        self.sortie=0.0
        self.w=[]
        self.x=[]
        self.s=[]
        pass

    def propagation(self):
        self.somme=0.0
        for i in range(len(self.x)):
            self.somme+=self.x[i]*self.w[i]
            pass
        self.sortie= 1 / (1 + math.exp(-self.coef*self.somme))
        pass

    def setEntre(self,input):
        self.x=[]
        self.w=[]
        for v in input:
            self.x.append(v)
            self.w.append(rnd.uniform(-0.01,0.01))
            pass
        pass

    def setSuivant(self, ns):
        self.s=[]
        for n in ns:
            self.s.append(n);
            pass
        pass

    def calculErreur(self):
        self.erreur=0.0
        for ns in self.s:
            self.erreur+=ns.getPoid(self.id) * ns.getSortie()
            pass
        self.erreur=self.erreur * ( self.coef * self.sortie * (1 - self.sortie))
        pass

    def retroPropagation(self):
        for i in range(len(self.w)):
            self.w[i]=self.taux * self.erreur * self.x[i]
            pass
        pass

    def getSortie(self):
        return self.sortie;
        pass



class NeuroneCache(object):
    """docstring for NeuroneCache."""

    def __init__(self, taux ,coef, id):
        self.taux = taux
        self.id=id
        self.coef=coef
        self.erreur=0.0
        self.somme=0.0
        self.sortie=0.0
        self.w=[]
        self.x=[]
        self.s=[]
        self.p=[]
        pass

    def propagation(self):
        self.somme=0.0
        for i in range(len(self.x)):
            self.somme+=self.x[i].getSortie()*self.w[i]
            pass
        self.sortie= 1 / (1 + math.exp(-self.coef*self.somme))
        pass

    def setPrecedent(self,input):
        self.x=[]
        self.w=[]
        for v in input:
            self.x.append(v)
            self.w.append(rnd.uniform(-0.01,0.01))
            pass
        pass

    def setSuivant(self, ns):
        self.s=[]
        for n in ns:
            self.s.append(n);
            pass
        pass

    def calculErreur(self):
        self.erreur=0.0
        for ns in self.s:
            self.erreur+=ns.getPoid(self.id) * ns.getSortie()
            pass
        self.erreur=self.erreur * ( self.coef * self.sortie * (1 - self.sortie))
        pass

    def retroPropagation(self):
        for i in range(len(self.w)):
            self.w[i]=self.taux * self.erreur * self.x[i].getSortie()
            pass
        pass

    def getSortie(self):
        return self.sortie;
        pass

    def getPoid(self, id):
        return self.w[id];
        pass


class NeuroneSortie(object):
    """docstring for NeuroneSortie."""

    def __init__(self, taux ,coef, id):
        self.taux = taux
        self.id=id
        self.coef=coef
        self.erreur=0.0
        self.somme=0.0
        self.sortie=0.0
        self.w=[]
        self.x=[]
        self.s=[]
        self.p=[]
        pass

    def propagation(self):
        self.somme=0.0
        for i in range(len(self.x)):
            self.somme+=self.x[i].getSortie()*self.w[i]
            pass
        self.sortie= 1 / (1 + math.exp(-self.coef*self.somme))
        pass

    def setPrecedent(self,input):
        self.x=[]
        self.w=[]
        for v in input:
            self.x.append(v)
            self.w.append(rnd.uniform(-0.01,0.01))
            pass
        pass

    def setSuivant(self, ns):
        self.s=[]
        for n in ns:
            self.s.append(n);
            pass
        pass

    def calculErreur(self,sa):
        self.erreur=sa - self.sortie
        pass

    def retroPropagation(self):
        for i in range(len(self.w)):
            self.w[i]=self.taux * self.erreur *(self.coef * self.sortie * (1-self.sortie))*self.x[i].getSortie()
            pass
        pass

    def getSortie(self):
        return self.sortie;
        pass

    def getPoid(self, id):
        return self.w[id];
        pass
