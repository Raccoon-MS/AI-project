import random as rnd
import math
import time


class EntryNeuron(object):
    """docstring for EntryNeuron."""

    def __init__(self, taux ,coef, id):
        self.taux = taux
        self.id=id
        self.coef=coef
        self.error=0.0
        self.sum=0.0
        self.output=0.0
        self.weights= []
        self.x= []
        self.s= []
        pass

    def propagation(self):
        self.sum=0.0
        for i in range(len(self.x)):
            self.sum += self.x[i] * self.weights[i]
            pass
        self.output= 1 / (1 + math.exp(-self.coef*self.sum))
        pass

    def setInput(self,input):
        self.x= []
        self.weights= []
        for v in input:
            self.x.append(v)
            self.weights.append(rnd.uniform(-0.01,0.01))
            pass
        pass

    def setNext(self, ns):
        self.s= []
        for n in ns:
            self.s.append(n);
            pass
        pass

    def processError(self):
        self.error=0.0
        for ns in self.s:
            self.error+=ns.getWeight(self.id) * ns.getOutput()
            pass
        self.error=self.error * ( self.coef * self.output * (1 - self.output))
        pass

    def backProp(self):
        for i in range(len(self.weights)):
            self.weights[i]=self.taux * self.error * self.x[i]
            pass
        
        pass

    def getOutput(self):
        return self.output;
        pass

class HiddenNeuron(object):
    """docstring for HiddenNeuron."""

    def __init__(self, taux ,coef, id):
        self.taux = taux
        self.id=id
        self.coef=coef
        self.error=0.0
        self.sum=0.0
        self.output=0.0
        self.weights= []
        self.x= []
        self.s= []
        self.p= []
        pass

    def propagation(self):
        self.sum=0.0
        for i in range(len(self.x)):
            self.sum+=self.x[i].getOutput()*self.weights[i]
            pass
        self.output= 1 / (1 + math.exp(-self.coef*self.sum))
        pass

    def setPrevious(self,input):
        self.x= []
        self.weights= []
        for v in input:
            self.x.append(v)
            self.weights.append(rnd.uniform(-0.01,0.01))
            pass
        pass

    def setNext(self, ns):
        self.s= []
        for n in ns:
            self.s.append(n);
            pass
        pass

    def processError(self):
        self.error=0.0
        for ns in self.s:
            self.error+=ns.getWeight(self.id) * ns.getOutput()
            pass
        self.error=self.error * ( self.coef * self.output * (1 - self.output))
        pass

    def backProp(self):
        for i in range(len(self.weights)):
            self.weights[i]=self.taux * self.error * self.x[i].getOutput()
            pass
        pass

    def getOutput(self):
        return self.output;
        pass

    def getWeight(self, id):
        return self.weights[id];
        pass


class OutputNeuron(object):
    """docstring for OutputNeuron."""

    def __init__(self, taux ,coef, id):
        self.taux = taux
        self.id=id
        self.coef=coef
        self.error=0.0
        self.sum=0.0
        self.output=0.0
        self.weights= []
        self.x= []
        self.s= []
        self.p= []
        pass

    def propagation(self):
        self.sum=0.0
        for i in range(len(self.x)):
            self.sum+=self.x[i].getOutput()*self.weights[i]
            pass
        self.output= 1 / (1 + math.exp(-self.coef*self.sum))
        pass

    def setPrevious(self,input):
        self.x= []
        self.weights= []
        for v in input:
            self.x.append(v)
            self.weights.append(rnd.uniform(-0.01,0.01))
            pass
        pass

    def setNext(self, ns):
        self.s= []
        for n in ns:
            self.s.append(n);
            pass
        pass

    def processError(self,sa):
        self.error=sa - self.output
        pass

    def backProp(self):
        for i in range(len(self.weights)):
            self.weights[i]=self.taux * self.error *(self.coef * self.output * (1-self.output))*self.x[i].getOutput()
            pass
        pass

    def getOutput(self):
        return self.output;
        pass

    def getWeight(self, id):
        return self.weights[id];
        pass



class Reseau(object):
    """docstring for Reseau."""

    def __init__(self):
        self.input = []
        self.cache= []
        self.output= []
        self.errorOk=0.2
        self.d= []
        self.sa= []
        for i in range(10):
            self.input.append( EntryNeuron(0.1,2,i))
            pass
        for i in range(10):
            self.cache.append( HiddenNeuron(0.1,2,i))
            pass
        self.output.append( OutputNeuron(0.1,2,0))
            
        for n in self.input:
            n.setNext(self.cache)
            pass
        for n in self.cache:
            n.setPrevious(self.input)
            n.setNext(self.output)
            pass
        for n in self.output:
            n.setPrevious(self.cache)
            pass
        pass

    def chargerDonnees(self,datas, outputs):
        # toi tu charges tes vari donner mdr
        self.d= datas
        self.sa= outputs
        for n in self.input:
            n.setInput(self.d)
        pass

    def propagation(self):
        for n in self.input:
            n.propagation()
            pass
        for n in self.cache:
            n.propagation()
            pass
        for n in self.output:
            n.propagation()
            pass
        pass

    def processError(self):
        for i in range(len(self.output)):
            self.output[i].processError(self.sa)
            pass
        for n in self.cache:
            n.processError()
            pass
        for n in self.input:
            n.processError()
            pass
        pass

    def backProp(self):
        for n in self.output:
            n.backProp()
            pass
        for n in self.cache:
            n.backProp()
            pass
        for n in self.input:
            n.backProp()
            pass
        pass

    def printoutput(self):
        for n in self.output:
            print(n.getOutput())
            pass
        pass

class InputManager():
    def __init__(self, file):
        self.file = file
        self.data = []
        self.inputs = []
        self.results = []
        self.normalAlphabet = []
        self.codedAlphabet = {}
        self.len = 0

    def process(self):
        lines = open(self.file, "r")
        self.createAlphabet(lines)
        lines.close()
        self.codeAlphabet()
        lines = open(self.file, "r")
        self.translateAll(lines)
        lines.close()

    def createAlphabet(self, lines):
        for l in lines:
            if l.endswith("\n"):
                l = l[:-1]
            l = l[:-2]

            #Calcul au passage de la plus grande longueur de phrase
            if len(l) > self.len:
                self.len = len(l)

            for w in l:
                if not w in self.normalAlphabet:
                    self.normalAlphabet.append(w)
    
    def codeAlphabet(self):
        maxi = self.getMaxASCII()
        for w in self.normalAlphabet:
            code = ord(w) / maxi
            self.codedAlphabet[w] = code

    def getMaxASCII(self):
        maxi = 0
        for c in self.normalAlphabet:
            code = ord(c)
            if code > maxi:
                maxi = code
        return maxi

    def translateAll(self, lines):
        for l in lines:
            if l.endswith("\n"):
                l = l[:-1]

            result = int(l[-1])
            l = l[:-2]
            
            sentence = []
            for w in l:
                sentence.append(self.translateWord(w))

            self.data.append((sentence, result))
            self.inputs.append(sentence)
            self.results.append(result)
            
    def translateWord(self, word):
        return self.codedAlphabet[word]

    def getMaxLength(self):
        return self.len

    def getInputs(self):
        return self.inputs

    def getResults(self):
        return self.results


if __name__ == "__main__":
    im = InputManager("dataset.csv")
    im.process()
    inputLayerSize = im.getMaxLength()

    print(inputLayerSize)

    r = Reseau()

    inputs = im.getInputs()
    results = im.getResults()

    trainingStartTime = time.time()

    trainings = 0

    while trainings <= 50:
        trainings += 1
        for i in range(len(inputs)):
            r.chargerDonnees(inputs[i], results[i])

            r.propagation()
            r.processError()
            r.backProp()

    trainingEndTime = time.time()

    print("Training completed in: {} s".format(trainingEndTime - trainingStartTime))
    print(trainings)

    r.chargerDonnees(inputs[0], results[0])
    r.propagation()
    r.printoutput()
    print(results[0])


