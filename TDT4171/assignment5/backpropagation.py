import math
import random
import copy

# The transfer function of neurons, g(x)
def logFunc(x):
    return (1.0/(1.0+math.exp(-x)))

# The derivative of the transfer function, g'(x)
def logFuncDerivative(x):
    return math.exp(-x)/(pow(math.exp(-x)+1,2))

def randomFloat(low, high):
    return random.random()*(high-low) + low

# Initializes a matrix of all zeros
def makeMatrix(m, n):
    M = []
    for i in xrange(m):
        M.append([0]*n)
    return M

class NN: # Neural Network
    def __init__(self, numInputs, numHidden, learningRate=0.001):
        # Inputs: number of input and hidden nodes. Assuming a single output node.
        # +1 for bias node: A node with a constant input of 1. Used to shift the transfer function.
        self.numInputs = numInputs + 1
        self.numHidden = numHidden

        # Current activation levels for nodes (in other words, the nodes' output value)
        self.inputActivation = [1.0]*self.numInputs
        self.hiddenActivations = [1.0]*self.numHidden
        self.outputActivation = 1.0 # Assuming a single output.
        self.learningRate = learningRate

        # create weights
        # A matrix with all weights from input layer to hidden layer
        self.weightsInput = makeMatrix(self.numInputs,self.numHidden)
        # A list with all weights from hidden layer to the single output neuron.
        self.weightsOutput = [0 for i in xrange(self.numHidden)] # Assuming single output
        # set them to random vaules
        for i in xrange(self.numInputs):
            for j in xrange(self.numHidden):
                self.weightsInput[i][j] = randomFloat(-0.5, 0.5)
        for j in xrange(self.numHidden):
            self.weightsOutput[j] = randomFloat(-0.5, 0.5)

        # Data for the backpropagation step in RankNets.
        # For storing the previous activation levels (output levels) of all neurons
        self.prevInputActivations = []
        self.prevHiddenActivations = []
        self.prevOutputActivation = 0
        # For storing the previous delta in the output and hidden layer
        self.prevDeltaOutput = 0
        self.prevDeltaHidden = [0 for i in xrange(self.numHidden)]
        # For storing the current delta in the same layers
        self.deltaOutput = 0
        self.deltaHidden = [0 for i in xrange(self.numHidden)]

    def propagate(self, inputs):
        if len(inputs) != self.numInputs-1:
            raise ValueError('wrong number of inputs')

        # input activations
        self.prevInputActivations=copy.deepcopy(self.inputActivation)
        for i in xrange(self.numInputs-1):
            self.inputActivation[i] = inputs[i]
        self.inputActivation[-1] = 1 # Set bias node to -1.

        # hidden activations
        self.prevHiddenActivations=copy.deepcopy(self.hiddenActivations)
        for j in xrange(self.numHidden):
            Sum = 0.0
            for i in xrange(self.numInputs):
                # print self.ai[i] ," * " , self.wi[i][j]
                Sum = Sum + self.inputActivation[i] * self.weightsInput[i][j]
            self.hiddenActivations[j] = logFunc(Sum)

        # output activations
        self.prevOutputActivation=self.outputActivation
        Sum = 0.0
        for j in xrange(self.numHidden):
            Sum = Sum + self.hiddenActivations[j] * self.weightsOutput[j]
        self.outputActivation = logFunc(Sum)
        return self.outputActivation

    def computeOutputDelta(self):
        P_ab = logFunc(self.prevOutputActivation - self.outputActivation)
        self.prevDeltaOutput = logFuncDerivative(self.prevOutputActivation)*(1 - P_ab)
        self.deltaOutput = logFuncDerivative(self.outputActivation)*(1 - P_ab)
        
    def computeHiddenDelta(self):
        for i in xrange(self.numHidden):
            self.prevDeltaHidden[i] = logFuncDerivative(self.prevHiddenActivations[i])*self.weightsOutput[i]*(self.prevDeltaOutput - self.deltaOutput)
            self.deltaHidden[i] = logFuncDerivative(self.hiddenActivations[i])*self.weightsOutput[i]*(self.prevDeltaOutput - self.deltaOutput)
            
    def updateWeights(self):
        for i in xrange(self.numInputs):
            for j in xrange(self.numHidden):
                self.weightsInput[i][j] += self.learningRate*(self.prevDeltaHidden[j]*self.prevInputActivations[i] - self.deltaHidden[j]*self.inputActivation[i])
        for i in xrange(self.numHidden):
            self.weightsOutput[i] += self.learningRate*(self.prevHiddenActivations[i]*self.prevDeltaOutput - self.hiddenActivations[i]*self.deltaOutput)

    def backpropagate(self):
        self.computeOutputDelta()
        self.computeHiddenDelta()
        self.updateWeights()

    # Prints the network weights
    def weights(self):
        print('Input weights:')
        for i in xrange(self.numInputs):
            print(self.weightsInput[i])
        print()
        print('Output weights:')
        print(self.weightsOutput)

    def train(self, patterns, iterations=1):    
        for i in xrange(iterations):
            for p in patterns:
                self.propagate(p[0].features)
                self.propagate(p[1].features)
                self.backpropagate()

    def countMisorderedPairs(self, patterns):
        numMisses = 0
        for p in patterns:
            A = self.propagate(p[0].features)
            B = self.propagate(p[1].features)
            numMisses += A <= B
        errorRate = float(numMisses)/len(patterns)
        print 'Number of misses: ' + str(numMisses) + ', total: ' + str(len(patterns)) + ', error rate: ' + str(errorRate)
        return errorRate
            


        