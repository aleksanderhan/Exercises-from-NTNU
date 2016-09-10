import random
from copy import copy
from math import exp


class Simulated_annealing_solver(object):

	def __init__(self, T_max = 100000, dT = 1, n = 10):
		self.n = n # number of neighbors created
		self.T_max = T_max
		self.dT = dT
		random.seed() #initializes the rng with a new seed

	def set_problem(self, problem):
		self.problem = problem

	def solve(self):
		P = self.problem.initial_condition
		T = self.T_max
		F = self.problem.objective_function
		threshold = self.problem.threshold
		F_P = F(P)
		generate_neighbors = self.problem.generate_neighbors
		while F_P < threshold:
			if T <= 0:
				print 'Threshold not reached, solution might not be optimal and/or violates one of the constraints'
				break;

			neighbors = generate_neighbors(P, self.n)
			F_neighbors = map(F, neighbors)

			max_idx = F_neighbors.index(max(F_neighbors))
			P_max = neighbors[max_idx]

			q = (F_neighbors[max_idx] - F_P)/F_P
			p = min(1, exp(-q/T))
			if random.random() > p:
				P = P_max
			else:				
				P = neighbors[random.randint(0, len(neighbors) - 1)]

			T -= self.dT
			F_P = F(P)

		self.problem.solution = P		
	

class SA_problem(object):

	def __init__(self, initial_condition, threshold):
		self.initial_condition = initial_condition
		self.solution = None
		self.threshold = threshold


class Egg_carton_puzzle(SA_problem):

	def __init__(self, m, n, k, initial_condition, threshold):
		SA_problem.__init__(self, initial_condition, threshold)
		self.m = m
		self.n = n
		self.k = k

	def objective_function(self, V):
		# Given that there are less than k eggs in each given direction (horizontal, 
		# vertical and the diagonals) the score is the sum of the number of eggs+1 in
		# each direction.
		score = 0.0001

		# Rows
		for i in xrange(self.m):
			number_of_eggs = 0
			for j in xrange(self.n):
				number_of_eggs += V[i*self.n + j]
			# Violation of the constraints, i.e. solution is garbage
			if number_of_eggs > self.k:
				return 0.0001
			# Computes the score
			score += self.direction_score(number_of_eggs)
		
		# Colums
		for j in xrange(self.n):
			number_of_eggs = 0
			for i in xrange(self.m):
				number_of_eggs += V[i*self.n + j]

			if number_of_eggs > self.k:
				return 0.0001			
			score += self.direction_score(number_of_eggs)
		
		# Diagonals 1
		# Shift to the right and pad the rows with 0s
		d1 = V[:self.n]
		for i in xrange(1, self.m):
			d1 = d1 + [0]*self.m + V[i*self.n:(i+1)*self.n]
		# Computing the sum of the relevant colums to get the diagonals
		d1_n = len(d1)/self.m # Number of colums in d1
		for j in xrange(d1_n): 
			number_of_eggs = 0
			for i in xrange(self.m):
				number_of_eggs += d1[i*d1_n + j]

			if number_of_eggs > self.k:
				return 0.0001
			score += self.direction_score(number_of_eggs)

		# Diagonals 2
		# Shift to the left and pad the rows with 0s
		d2 = []
		for i in xrange(self.m):
			d2 = d2 + [0]*(self.m-1) + V[i*self.n:(i+1)*self.n]

		d2_n = len(d2)/self.m # Number of colums in d1
		for j in xrange(d2_n): 
			number_of_eggs = 0
			for i in xrange(self.m):
				number_of_eggs += d2[i*d1_n + j]

			if number_of_eggs > self.k:
				return 0.0001
			score += self.direction_score(number_of_eggs)

		# Test if solution is optimal
		if sum(V) == min(self.m, self.n)*self.k:
			return float('inf')
		return score

	# Help function for the objective function
	def direction_score(self, number_of_eggs):
		# Special score constants
		equal_k = 5 # Number of eggs equal to k (multiplies)
		equal_z = 1 # Number of eggs equal to zero (adds)
		equal_num = 2 # Number of eggs between 0 and k (multiplies)

		direction_score = 0
		if number_of_eggs == self.k:
			direction_score += equal_k*number_of_eggs
		elif number_of_eggs == 0:
			direction_score += equal_z
		else:
			direction_score += equal_num*number_of_eggs
		return direction_score


	# Generates n random neighbors
	def generate_neighbors(self, V, n):
		res = []
		for i in xrange(n):
			neighbor = copy(V)
			idx = random.randint(0, len(V) - 1)
			#neighbor[idx] = random.choice((0, 1))
			
			if neighbor[idx] == 1:
				neighbor[idx] = 0
			else:
				neighbor[idx] = 1
			
			#neighbor[idx] = (neighbor[idx] + 1)%2
			res.append(neighbor)
		return res



'''Main'''
def main():
	solver = Simulated_annealing_solver()

	# Variant 1
	p1 = Egg_carton_puzzle(5, 5, 2, [0]*5*5, 300)
	solver.set_problem(p1)
	solver.solve()
	display_solution(p1)
	
	# Variant 2
	p2 = Egg_carton_puzzle(6, 6, 2, [0]*6*6, 500)
	solver.set_problem(p2)
	solver.solve()
	display_solution(p2)
	'''
	# Variant 3
	p3 = Egg_carton_puzzle(8, 8, 1, [0]*8*8, 300)
	solver.set_problem(p3)
	solver.solve()
	solved_puzzles.append(p3)

	# Variant 4
	p4 = Egg_carton_puzzle(10, 10, 3, [0]*10*10, 300)
	solver.set_problem(p4)
	solver.solve()
	solved_puzzles.append(p4)
	'''

def display_solution(problem):
	print 'M=' + str(problem.m) + ', N=' + str(problem.n) + ', K=' + str(problem.k)
	for i in xrange(problem.m):
		row = ''
		for j in xrange(problem.n):
			row += str(problem.solution[problem.n*i + j]) + ' '
		print row
	print


main()
