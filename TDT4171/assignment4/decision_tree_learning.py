import random
from math import log2


class Decision_tree_node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_branch(self, label, subtree):
        self.children[label] = subtree

    def __repr__(self, level=0):
        ret = "\t"*level+"value: "+repr(self.value)+"\n"
        for k, v in self.children.items():
            ret += v.__repr__(level+1)
        return ret


def decision_tree_learning(examples, attributes, parent_examples, importance_func):
    if not examples:
        return Decision_tree_node(_plurality_value(parent_examples))

    if _same_classification(examples):
        return Decision_tree_node(examples[0][-1])

    if not attributes:
        return Decision_tree_node(_plurality_value(examples))

    #A = max([importance_func(a, examples) for a in attributes])
    temp = {}
    for a in attributes:
        temp[a] = importance_func(a, examples)
    A = max(temp, key=temp.get)
    root = Decision_tree_node(A)
    attributes.remove(A)
    for value in (1, 2):
        exs = [e for e in examples if e[A] == value]
        subtree = decision_tree_learning(exs, attributes, examples, importance_func)
        root.add_branch(value, subtree)
    return root


# Tests if all the objects in the examples has the same class
def _same_classification(examples):
    same_class = True
    classification = examples[0][-1] 
    for ex in examples:
        if ex[-1] != classification:
            same_class = False
            break
    return same_class


def _plurality_value(examples):
    count = {}
    for ex in examples:
        if ex[-1] in count:
            count[ex[-1]] += 1
        else:
            count[ex[-1]] = 1
    return max(count, key=count.get)


# Picks a random attribute   
def importance_random(attribute, examples):
    return random.random()


def importance_entropy_gain(attribute, examples):
    p = [e[-1] for e in examples].count(1)
    return _B(p/len(examples)) - _remainder(attribute, examples)


# This function could be cleaner and more general, but should do its job for the assignment
def _remainder(attribute, examples):
    E1 = [e[-1] for e in examples if e[attribute] == 1]
    E2 = [e[-1] for e in examples if e[attribute] == 2]
    p1 = E1.count(1)
    p2 = E2.count(1)
    return (len(E1)/len(examples))*_B(p1/len(E1)) + (len(E2)/len(examples))*_B(p2/len(E2))


# entropy of a boolean variable
def _B(q):
    if q == 0 or q == 1:
        return 0
    else:
        return -(q*log2(q) + (1.0-q)*log2(1.0-q))


# Shannon entropy of a random variable with probabilities P
def _shannon_entropy(P):
    return -sum([P[v_k] * log2(P[v_k]) for v_k in range(len(P))])

