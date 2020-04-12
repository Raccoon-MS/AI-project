import random as rnd
import math
import time

def sigmoid(x):
        return 1 / (1 + math.exp(-x))

def derivativeSigmoid(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

class Neuron():
    def __init__(self, layer, nbOfInputs, lastLayer=False):
        self.id = id
        self.layer = layer
        self.error = 0

        if layer == 0:
            self.weights = []
            for i in range(nbOfInputs):
                self.weights.append(1)
        else:
            self.weights = []
            for i in range(nbOfInputs):
                self.weights.append(rnd.uniform(-0.01,0.01))    
        self.bias = 0 #rnd.random()
        self.output = 0
        self.lastLayer = lastLayer
        self.inputs = []

    def think(self, inputs):
        self.output = 0
        self.inputs = inputs
        value = 0
        for i in range(len(inputs)):
            value += inputs[i] * self.weights[i]
        self.output = sigmoid(value + self.bias)

    def setError(self, error):
        self.error=error * ( 0.1 * self.output * (1 - self.output))

    def backpropagation(self):
        taux = 2
        coefficient = 0.1
        if self.lastLayer:
            for i in range(len(self.inputs)):
                self.weights[i] = taux * self.error * (coefficient * self.output * (1 - self.output)) * self.inputs[i]
        else:
            for i in range(len(self.inputs)):
                self.weights[i]= taux * self.error * self.inputs[i]


class NeuronLayer():
    def __init__(self, id, numberOfNeurons, previousLayerSize, lastLayer=False):
        self.id = id
        self.neurons = []
        self.error = 0

        for i in range(0, numberOfNeurons):
            self.neurons.append(Neuron(id, previousLayerSize, lastLayer))
    
    def think(self, inputs):
        for n in self.neurons:
            n.think(inputs)

    def processError(self, nextLayer):
        self.error = 0
        for i in range(len(self.neurons) - 1):
            for n in nextLayer.neurons:
                error = n.weights[i] * n.output
            self.neurons[i].setError(error)

    def backpropagation(self):
        for n in self.neurons:
            n.backpropagation()

    def getOutputs(self):
        outputs = []
        for n in self.neurons:
            outputs.append(n.output)
        return outputs
    
class NeuralNetwork():
    def __init__(self, params, inputSize):
        self.layers = []
        for i in range(0, len(params)):
            if i == 0:
                self.layers.append(NeuronLayer(i, params[i], inputSize))
            elif i == len(params) - 1:
                self.layers.append(NeuronLayer(i, params[i], params[i-1], True))
            else:
                self.layers.append(NeuronLayer(i, params[i], params[i-1]))


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
            for i in range(len(inputs)):
                self.think(inputs[i])
                outputs.append(self.getOutput())

                localError = correct_outputs[i] - self.getOutput()
                #print(localError)
                self.layers[-1].neurons[0].error = localError
                self.layers[-1].error = localError

                for layerId in range(len(self.layers) - 1):
                    self.layers[len(self.layers) - (layerId + 1)].processError(self.layers[len(self.layers) - (layerId + 2)])

                self.backpropagation()
            #print(outputs)
            errorSum = 0
            for i in range(0, len(outputs)):
                difference = correct_outputs[i] - outputs[i]
                errorSum += difference * difference

            error = errorSum * 0.5


            print("e{} = {}".format(iteration, error))

    def backpropagation(self):
        for li in range(0, len(self.layers)):
            self.layers[li].backpropagation()

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
    archi = [10, 10, 1]
    network = NeuralNetwork(archi, inputLayerSize)

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