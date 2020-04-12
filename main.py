import numpy as np
import random as rnd
import math
import time

def sigmoid(x):
        return 1 / (1 + math.exp(-x))

def derivativeSigmoid(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

class Neuron():
    def __init__(self, layer, id):
        self.id = id
        self.layer = layer
        self.weight = rnd.uniform(-0.01,0.01)
        self.bias = 0 #rnd.random()
        self.output = 0

    def think(self, inputs):
        self.output = 0
        value = 0
        for i in inputs:
            value += i
        self.output = sigmoid((self.weight * value) + self.bias)

    def backpropagation(self, error):
         delta = error * derivativeSigmoid(self.output)
         #print(delta)
         self.weight += delta * self.output
            
    

class NeuronLayer():
    def __init__(self, id, numberOfNeurons):
        self.id = id
        self.neurons = []
        for i in range(0, numberOfNeurons):
            self.neurons.append(Neuron(id, i))
    
    def think(self, inputs):
        for n in self.neurons:
            n.think(inputs)

    def backpropagation(self, error):
        for n in self.neurons:
            n.backpropagation(error)

    def getOutputs(self):
        outputs = []
        for n in self.neurons:
            outputs.append(n.output)
        return outputs
    
class NeuralNetwork():
    def __init__(self, params):
        self.layers = []
        for i in range(0, len(params)):
            self.layers.append(NeuronLayer(i, params[i]))

    def think(self, inputs):
        self.layers[0].think(inputs)
        for i in range(1, len(self.layers)):
            self.layers[i].think(self.layers[i-1].getOutputs())
        return self.layers[len(self.layers)-1].getOutputs()
        

    def train(self, im, trainning_limit):
        inputs = im.getInputs()
        correct_outputs = im.getResults()
        #print(inputs)
        for iteration in range(0, trainning_limit):
            outputs = []
            for i in inputs:
                self.think(i)
                outputs.append(self.getOutput())
            #print(outputs)
            errorSum = 0
            for i in range(0, len(outputs)):
                difference = correct_outputs[i] - outputs[i]
                errorSum += difference * difference

            error = errorSum * 0.5
            self.backpropagation(error)
            print("e{} = {}".format(iteration, error))

    def backpropagation(self, error):
        i = 0
        for l in self.layers:
            if i == 0:
                i += 1
                continue
            l.backpropagation(error)
            i+=1

    def getOutput(self):
        return self.layers[-1].neurons[0].output

    #errueur neurone = pod * err

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
    archi = [10, 12, 1]
    network = NeuralNetwork(archi)

    trainingStartTime = time.time()

    network.train(im, 1500)

    trainingEndTime = time.time()

    print("Training completed in: {} s".format(trainingEndTime - trainingStartTime))

    print(network.getOutput())

    
            


#Sites utilisés:
#   -https://www.kdnuggets.com/2018/10/simple-neural-network-python.html
#
#
#