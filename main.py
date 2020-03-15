import numpy as np
import random as rnd
import math

class Neuron():
    def __init__(self):
        self.weight = rnd.random()
        self.output = 0

    def think(self, inputs):
        self.output = 0
        value = 0
        for i in inputs:
            v, w = i
            value += w*v
        self.output = (self.sigmoid(value), self.weight)
            
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

class NeuronLayer():
    def __init__(self, numberOfNeurons):
        self.neurons = []
        for i in range(0, numberOfNeurons):
            self.neurons.append(Neuron())
    
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
            self.layers.append(NeuronLayer(params[i]))

    def think(self, inputs):
        self.layers[0].think(inputs)
        for i in range(1, len(self.layers)):
            self.layers[i].think(self.layers[i-1].getOutputs())
        return self.layers[len(self.layers)-1].getOutputs()
        

    def train(self, initial_inputs, required_outputs, trainning_limit):
        for i in range(0, trainning_limit):
            self.think(initial_inputs)

        pass

if __name__ == "__main__":
    archi = [3, 5, 1]
    network = NeuralNetwork(archi)
    print(network.think([(1,1), (0,1), (0,0)]))
    
            


#Sites utilisés:
#   -https://www.kdnuggets.com/2018/10/simple-neural-network-python.html
#
#
#