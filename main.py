import numpy as np
import random as rnd
import math

class Neuron():
    def __init__(self, layer, id, numberOfWeights):
        self.id = id
        self.layer = layer
        if numberOfWeights == 0:
            self.weights = [1]
        else:
            self.weights = []
            for i in range(0, numberOfWeights):
                self.weights.append(rnd.uniform(-0.01,0.01))

        self.bias = rnd.random()
        self.output = (0,0)

    def think(self, inputs):
        self.output = 0
        value = 0
        for i in inputs:
            v, w = i
            value += w[self.id]*v
        self.output = (self.sigmoid(self.bias + value), self.weights)
            
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

class NeuronLayer():
    def __init__(self, id, numberOfNeurons, nextLayerSize):
        self.id = id
        self.neurons = []
        for i in range(0, numberOfNeurons):
            self.neurons.append(Neuron(id, i, nextLayerSize))
    
    def think(self, inputs):
        for n in self.neurons:
            n.think(inputs)

    def getOutputs(self):
        outputs = []
        for n in self.neurons:
            outputs.append(n.output)
        return outputs
    
class NeuralNetwork():
    def __init__(self, params):
        self.layers = []
        for i in range(0, len(params)):
            nextLayerSize = 0
            if i < len(params) - 1:
                nextLayerSize = params[i+1]
            self.layers.append(NeuronLayer(i, params[i], nextLayerSize))

    def think(self, inputs):
        self.layers[0].think(inputs)
        for i in range(1, len(self.layers)):
            self.layers[i].think(self.layers[i-1].getOutputs())
        return self.layers[len(self.layers)-1].getOutputs()
        

    def train(self, initial_inputs, required_outputs, trainning_limit):
        for i in range(0, trainning_limit):
            self.think(initial_inputs)

        pass

class InputConverter():
    def __init__(self, file):
        self.file = file
        self.data = []
        self.normalAlphabet = []
        self.codedAlphabet = {}

    def convert(self):
        lines = open(self.file, "r")
        self.createAlphabet(lines)
        lines.close()
        self.codeAlphabet()
        lines = open(self.file, "r")
        self.translateAll(lines)
        lines.close()
        return self.data

    def createAlphabet(self, lines):
        for l in lines:
            if l.endswith("\n"):
                l = l[:-1]
            words = l.split(" ")
            words = words[:-1]
            for w in words:
                if not w in self.normalAlphabet:
                    self.normalAlphabet.append(w)
    
    def codeAlphabet(self):
        maxi = len(self.normalAlphabet) + 1
        index = 0
        for w in self.normalAlphabet:
            code = index / maxi
            self.codedAlphabet[w] = code
            index += 1

    def translateAll(self, lines):
        for l in lines:
            if l.endswith("\n"):
                l = l[:-1]

            words = l.split(" ")

            result = int(words[-1])
            words = words[:-1]
            
            sentence = []
            for w in words:
                sentence.append(self.translateWord(w))
            self.data.append((sentence, result))
            
    def translateWord(self, word):
        return self.codedAlphabet[word]

    def maxSentenceLength(self):
        maxi = 0
        for d in self.datas:
            s, r = d
            if len(s) > maxi:
                maxi = len(s)
        return maxi 


if __name__ == "__main__":
    datas = InputConverter("dataset.csv").convert()
    inputLayerSize = datas.maxSentenceLength()
    
    archi = [inputLayerSize, 15, 1]
    network = NeuralNetwork(archi)
    result = network.think([(1,[1,1]), (1,[1,1])])
    for r in result:
        v, w = r
        print(v)"""
    
            


#Sites utilisés:
#   -https://www.kdnuggets.com/2018/10/simple-neural-network-python.html
#
#
#