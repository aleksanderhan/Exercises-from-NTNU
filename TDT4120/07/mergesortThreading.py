from sys import stdin
import Queue
import threading


def mergeSort(tasks, decks):
	A = tasks[0]
	B = tasks[1]
	i, j = 0, 0
	res = []

	# Appending the values from list A and B to res in sorted order
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			res.append(A[i])
			i += 1
		else:
			res.append(B[j])
			j += 1

	# Appending the rest of the lists A and B to res
	while i < len(A):
		res.append(A[i])
		i += 1
	while j < len(B):
		res.append(B[j])
		j += 1

	decks.put(res)
	global completedTasks
	completedTasks += 1

	
def taskMaker(decks, tasks):
	global taskCount
	while taskCount < n-1:
		a = decks.get(block=True)
		b = decks.get(block=True)
		tasks.put((a,b))
		taskCount += 1	


'''Main'''
# Making datastructures
decks = Queue.Queue()
letters = {}
n = 0 #number of decks
for line in stdin:
	n += 1
	temp = line.split(':')
	deck = map(int, temp[1].strip().split(','))
	decks.put(deck)
	for number in deck:
		letters[number] = temp[0]


#Making tasks to merge
tasks = Queue.Queue()
taskCount = 0
taskMakerThread = threading.Thread(target=taskMaker, args=(decks,tasks))
taskMakerThread.daemon = True
taskMakerThread.start()


# Merg sorting decks in decks list
completedTasks = 0
while completedTasks < n-1 and threading.active_count() < 8:
	try:
		task = tasks.get(block=True, timeout=0.005)
	except:
		continue;
	t = threading.Thread(target=mergeSort, args=(task,decks))
	t.daemon = True
	t.start()


# Creating word from sorted decks
word = ''
finalDeck = decks.get(block=True)
for i in finalDeck:
	word += letters[i]
print word















