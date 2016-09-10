__author__ = 'alekh'
import backpropagation as bp
import matplotlib.pyplot as plt
import itertools


# Class for holding your data - one object for each line in the dataset
class DataInstance:

    def __init__(self,qid,rating,features):
        self.qid = qid #ID of the query
        self.rating = rating #Rating of this site for this query
        self.features = features #The features of this query-site pair.

    def __str__(self):
        return "Datainstance - qid: " + str(self.qid) + ". rating: " + str(self.rating) + ". features: " + str(self.features)


# A class that holds all the data in one of our sets (the training set or the testset)
class DataHolder:

    def __init__(self, dataset):
        self.dataset = self.loadData(dataset)

    def loadData(self, file):
        # Input: A file with the data.
        # Output: A dict mapping each query ID to the relevant documents, like this: dataset[queryID] = [dataInstance1, dataInstance2, ...]
        data = open(file)
        dataset = {}
        for line in data:
            # Extracting all the useful info from the line of data
            lineData = line.split()
            rating = int(lineData[0])
            qid = int(lineData[1].split(':')[1])
            features = []
            for elem in lineData[2:]:
                if '#docid' in elem: #We reached a comment. Line done.
                    break
                features.append(float(elem.split(':')[1]))
            # Creating a new data instance, inserting in the dict.
            di = DataInstance(qid, rating, features)
            if qid in dataset.keys():
                dataset[qid].append(di)
            else:
                dataset[qid] = [di]
        return dataset


def runRanker(trainingset, testset, epochs):
    # Dataholders for training and testset
    dhTraining = DataHolder(trainingset)
    dhTesting = DataHolder(testset)

    # Creating an ANN instance - feel free to experiment with the learning rate (the third parameter).
    nn = bp.NN(46,10,0.0001)

    trainingPatterns = [] # For holding all the training patterns we will feed the network
    testPatterns = [] # For holding all the test patterns we will feed the network
    for qid in dhTraining.dataset.keys():
        dataInstances = dhTraining.dataset[qid]
        dataInstances.sort(key=lambda x: x.rating, reverse=True)
        for i in xrange(len(dataInstances)-1):
            for j in xrange(i+1, len(dataInstances)):
                if dataInstances[i].rating != dataInstances[j].rating: 
                    trainingPatterns.append((dataInstances[i], dataInstances[j]))

    for qid in dhTesting.dataset.keys():
        dataInstances = dhTesting.dataset[qid]
        dataInstances.sort(key=lambda x: x.rating, reverse=True)
        for i in xrange(len(dataInstances)-1):
            for j in xrange(i+1, len(dataInstances)):
                if dataInstances[i].rating != dataInstances[j].rating: 
                    testPatterns.append((dataInstances[i], dataInstances[j]))
    
    training_error = []
    test_error = []
    # Check ANN performance before training
    print 'Before training:'
    test_error.append(nn.countMisorderedPairs(testPatterns))
    training_error.append(nn.countMisorderedPairs(trainingPatterns))
    print 'After training:'
    for i in xrange(epochs):
        # Running <epochs> iterations, measuring testing performance after each round of training.
        nn.train(trainingPatterns)
        # Check ANN performance after training.
        print 'iteration ' + str(i+1) + " of " + str(epochs) + ':'
        test_error.append(nn.countMisorderedPairs(testPatterns))
        training_error.append(nn.countMisorderedPairs(trainingPatterns))
    print
    return training_error, test_error


def main():
    runs = 5
    epochs = 100
    total_test_error = [0]*(epochs+1)
    total_training_error = [0]*(epochs+1)
    # Calculating the average
    for i in xrange(runs):
        print 'run ' + str(i+1) + ' out of ' + str(runs) + ':'
        training_error, test_error = runRanker("train.txt", "test.txt", epochs)
        for i in xrange(len(training_error)):
            total_training_error[i] += training_error[i]
        for i in xrange(len(test_error)):
            total_test_error[i] += test_error[i]
    total_test_error = [e/runs for e in total_test_error]
    total_training_error = [e/runs for e in total_training_error]

    # Plotting and saving error graph.   
    plt.plot([1-e for e in total_training_error], 'r*--', label = 'training error')
    plt.plot([1-e for e in total_test_error], 'bo--', label = 'test error')
    plt.xlabel('epochs')
    plt.ylabel('correctly ordered pairs ratio')
    plt.legend(loc = 4)
    #plt.ylim(0, 1)
    plt.savefig('assignment5_plot.png')
    plt.show()


if __name__ == '__main__':
    main()

    










