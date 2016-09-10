import random
from math import exp


''' Solver class, implements the simulated annealing algorithm'''
class Simulated_annealing_solver(object):
	def __init__(self, T_max = 10000, dT = 0.5, n = 40):
		self.n = n # number of neighbors created
		self.T_max = T_max # Maximum temperature
		self.dT = dT # temperature step
		random.seed() #initializes the rng with a new seed

	# set problem to solve
	def set_problem(self, problem):
		self.problem = problem

	# Simulated annealing algorithm from the problem description
	def solve(self):
		P = self.problem.initial_condition
		T = self.T_max
		F = self.problem.objective_function
		threshold = self.problem.threshold
		F_P = F(P)
		generate_neighbors = self.problem.generate_neighbors
		# while optimal solution is not found:
		while F_P > threshold:
			if T <= 0:
				print 'Threshold not reached, solution might not be optimal and/or violates one of the constraints'
				break;
			
			neighbors = generate_neighbors(P, self.n) # generates neighbors			
			F_neighbors = map(F, neighbors) # computes F(neighbor) for all generated neighbors

			min_idx = F_neighbors.index(min(F_neighbors)) # finds the most promising neighbor
			P_min = neighbors[min_idx]

			q = (F_neighbors[min_idx] - F_P)/F_P
			p = min(1, exp(-q/T))
			if random.random() > p:
				P = P_min
			else:				
				P = neighbors[random.randint(0, len(neighbors) - 1)]

			T -= self.dT
			F_P = F(P)

		self.problem.solution = P		
	

''' Simulated annealing problem class '''
class SA_problem(object):

	def __init__(self, initial_condition, threshold):
		self.initial_condition = initial_condition
		self.solution = None
		self.threshold = threshold


''' Egg carton puzzle class inherits from SA_problem class'''
class Egg_carton_puzzle(SA_problem):

	def __init__(self, m, n, k, initial_condition, threshold):
		SA_problem.__init__(self, initial_condition, threshold)
		self.m = m # amount of rows
		self.n = n # amount of columns
		self.k = k # maximal amount of eggs in any direction

	#objective function that evaluates solution
	def objective_function(self, V):
		'''
		evaluates the sum of the eggs in each direction and subtracts k. 
		Then takes the absolute value of the result. 
		This ensures that only a optimal solution will give a perfect score. 
		If any of the rows have more than k eggs it adds a fixed amount to the score.
		'''
		score = 0.0001 # Has to be != 0 to avoid zero division

		# Rows
		for i in xrange(self.m):
			number_of_eggs = 0
			for j in xrange(self.n):
				number_of_eggs += V[i*self.n + j]
			# Violation of the constraints, i.e. solution is garbage
			if number_of_eggs > self.k:
				score += 1000
			score += abs(number_of_eggs - self.k)
		
		# Colums
		for j in xrange(self.n):
			number_of_eggs = 0
			for i in xrange(self.m):
				number_of_eggs += V[i*self.n + j]

			if number_of_eggs > self.k:
				score += 1000
			score += abs(number_of_eggs - self.k)
		
		# Diagonals 1
		# Shift to the right and pad the rows with 0s
		d1 = V[:self.n]
		for i in xrange(1, self.m):
			d1 = d1 + [0]*self.m + V[i*self.n:(i+1)*self.n]
		# Computing the sum of the relevant colums to get the diagonals
		d1_n = len(d1)/self.m # Number of colums in d1
		for j in xrange(d1_n -2*self.k): 
			number_of_eggs = 0
			for i in xrange(self.m):
				number_of_eggs += d1[i*d1_n + j + self.k]

			if number_of_eggs > self.k:
				score += 1000
			score += abs(number_of_eggs - self.k)

		# Diagonals 2
		# Shift to the left and pad the rows with 0s
		d2 = []
		for i in xrange(self.m):
			d2 = d2 + [0]*(self.m-1) + V[i*self.n:(i+1)*self.n]

		d2_n = len(d2)/self.m # Number of colums in d1
		for j in xrange(d2_n -2*self.k): 
			number_of_eggs = 0
			for i in xrange(self.m):
				number_of_eggs += d2[i*d1_n + j + self.k]

			if number_of_eggs > self.k:
				score += 1000
			score += abs(number_of_eggs - self.k)

		return score



	# Generates n random neighbors
	def generate_neighbors(self, V, n):
		res = []
		for i in xrange(n):
			neighbor = V[:] # makes a copy of V
			idx = random.randint(0, len(V) - 1) # picks a random index
			if neighbor[idx] == 1:
				neighbor[idx] = 0
			else:
				neighbor[idx] = 1
			res.append(neighbor)
		return res



'''Main'''
def main():
	solver = Simulated_annealing_solver() # create a solver object
	
	# Variant 1
	p1 = Egg_carton_puzzle(5, 5, 2, [0]*5*5, 12) # make a egg carton puzzle object
	solver.set_problem(p1) # sets the problem in the solver
	solver.solve() # solve problem
	display_solution(p1) # print solution
	'''
	# Variant 2
	p2 = Egg_carton_puzzle(6, 6, 2, [0]*6*6, 29)
	solver.set_problem(p2)
	solver.solve()
	display_solution(p2)
	
	# Variant 3
	p3 = Egg_carton_puzzle(8, 8, 1, [0]*8*8, 37)
	solver.set_problem(p3)
	solver.solve()
	display_solution(p3)
	
	# Variant 4
	p4 = Egg_carton_puzzle(10, 10, 3, [0]*10*10, 88)
	solver.set_problem(p4)
	solver.solve()
	display_solution(p4)
	'''

# Prints a representation of the solved puzzle to console
def display_solution(problem):
	print 'M=' + str(problem.m) + ', N=' + str(problem.n) + ', K=' + str(problem.k)
	for i in xrange(problem.m):
		row = ''
		for j in xrange(problem.n):
			row += str(problem.solution[problem.n*i + j]) + ' '
		print row
	print


main()
