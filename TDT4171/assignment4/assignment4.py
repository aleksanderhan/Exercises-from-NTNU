#!/usr/bin/env python
from decision_tree_learning import *


def read_file(path):
    data = []
    with open(path, 'r') as f:
        for line in f:
            data.append([int(i) for i in line.split()])
    return data


def classify(tree, ex):
    node = tree
    while node.children: 
        node = node.children[ex[node.value]]
    return node.value


def test_accuracy(tree, data):
    correct = 0
    for line in data:
        if line[-1] == classify(tree, line):
            correct += 1
    print("Correct:", str(correct) + "/" + str(len(data)))


def main():
    trainingdata = read_file("data/training.txt")
    testdata = read_file("data/test.txt")

    print("Random importance")
    dtree1 = decision_tree_learning(trainingdata, list(range(7)), [], importance_random)
    test_accuracy(dtree1, testdata)
    print("Tree structure:")
    print(dtree1)
    print()
    print("Information gain importance")
    dtree2 = decision_tree_learning(trainingdata, list(range(7)), [], importance_entropy_gain)
    test_accuracy(dtree2, testdata)
    print("Tree structure:")
    print(dtree2)




if __name__ == "__main__":
    main()
