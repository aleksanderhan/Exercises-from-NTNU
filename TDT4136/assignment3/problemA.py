from Tkinter import *

'''
Board class that contains all the nodes in a two dimensional array.

'''
class Board:
    def __init__(self, gui, algorithm):
        self.gui = gui   
        self.board = []
        self.open = []
        self.closed = []
        self.goal = None
        self.dimX = None
        self.dimY = None
        self.algorithm = algorithm
    
    # taxicab metric function
    def heuristicCost(self, node):
        return abs(self.goal.x - node.x) + abs(self.goal.y - node.y)
    
    # returns cost of node type for a given node
    @staticmethod
    def cellCost(node):
        cost = {'w': 100, 'm': 50, 'f': 10, 'g': 5, 'r': 1}
        return cost.get(node.type_, 0)
    
    # initializes the board with lines from file
    def addBoard(self, lines):
        for y in xrange(len(lines)):
            tempLine = []
            for x in xrange(len(lines[y])):
                if lines[y][x] != '\n':
                    tempNode = Node(self, y, x, lines[y][x])

                    if lines[y][x] == 'B':
                        self.goal = tempNode
                    elif lines[y][x] == 'A':
                        self.open.append(tempNode)
                    elif lines[y][x] == '#':
                        self.closed.append(tempNode)

                    tempLine.append(tempNode)
                    
            if self.dimX == None:
                self.dimX = len(tempLine) - 1

            self.board.append(tempLine)
        
        if self.dimY == None:
            self.dimY = len(self.board) - 1
        
        if len(self.open) > 0:
            self.open[0].g = 0
            self.open[0].f = self.heuristicCost(self.open[0]) + self.cellCost(self.open[0])
            self.open[0].onPath = True
    
    # sorts open nodes based on algorithm   
    def sortOpenNodes(self):
        if self.algorithm == 0: # A*
            self.open = sorted(self.open, key=lambda x: float(x.f))
        elif self.algorithm == 1: # BFS
            self.open = self.open 
        elif self.algorithm == 2: # Dijkstra
            self.open = sorted(self.open, key=lambda x: float(x.g))


    # produces children of the node
    def getChildren(self, node):
        children = []
        # gets children that are adjacent and in the map
        if node.y > 0: # up
            children.append(self.board[node.y - 1][node.x])
        if node.y < self.dimY: # down
            children.append(self.board[node.y + 1][node.x])
        if node.x > 0: # left
            children.append(self.board[node.y][node.x - 1])
        if node.x < self.dimX: # right
            children.append(self.board[node.y][node.x + 1])
        return children
    
    # construct path from current (goal) to start node
    def constructPath(self, current):
        if current.parent != None:
            current.onPath = True
            self.constructPath(current.parent)

    # agenda loop
    def run(self):
        # are there any open nodes left?
        if len(self.open) == 0:
            self.gui.draw([], True)
            return;
        
        self.sortOpenNodes() #sort nodes after priority
        current = self.open[0] 
        
        # is the current node the goal?
        if current.type_ == 'B':
            self.constructPath(self.goal)
            self.gui.draw(self.board, True)
            return;
        
        # remove from open list and add to closed lsit
        self.open.pop(0)
        self.closed.append(current)
        current.closed = True
        
        # get children of current node
        tempChildren = self.getChildren(current)

        # loop over all children of current node
        for child in tempChildren:
            # go to next iteration of loop if the child is closed
            if child in self.closed:
                continue
            
            # new g cost for this node
            newG = current.g + 0 + self.cellCost(child)
            
            # check if we should evaluate the child node
            if child not in self.open or newG < child.g:
                child.parent = current

                # set new values
                child.g = newG
                child.f = child.g + self.heuristicCost(child)
                
                # if not in open list, add to list
                if child not in self.open:
                    self.open.append(child)
        
        # draw board
        self.gui.draw(self.board, False)


'''
Node class containing relevant data for each node.
'''
class Node:
    def __init__(self, board, y, x, type_):
        self.board = board
        
        self.x = x # x-coordinate
        self.y = y # y-coordinate
        self.type_ = type_ # cell-type
        self.g = 0 # g cost
        self.f = 0 # f cost
        
        self.parent = None
        self.onPath = False
        self.closed = False
  
'''
Run class for reading in board from file and starting the algorithms
'''
class Run:
    def __init__(self, gui):
        self.file = None
        self.board = None
        self.gui = gui
        self.algorithm = 0 # 0 : A*, 1: BFS, 2 : Dijkstra
    
    # open a board from file
    def openFile(self, file_name):
        self.board = None
        self.board = Board(self.gui, self.algorithm)
        with open('boards/' + file_name) as f:
            lines = []
            for i in f.readlines():
                lines.append(list(i))
            self.board.addBoard(lines)
    
    # run algorithm
    def run(self):
        self.board.run()


'''
GUI class that vizualizes the board and the algorithm steps and the final path
'''
class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.canvas = None
        self.run = Run(self)
        self.sqsize = 30 # square size [bits]
        self.delay = 10 # delay between each step in the algorithm
        
        # colors for the different node types
        self.color = {
            ".": "#808080", 
            "#": "#000000", 
            "A": "#ff0000",
            "B": "#00ff00", 
            "w": "#0000ff", 
            "m": "#808080", 
            "f": "#336600", 
            "g": "#00cc66", 
            "r": "#ff8000"}
        
    # drawing the board
    def draw(self, grid, finished):
        # if the grid are empty and we are finished, end procedure
        if len(grid) == 0 and finished:
            return

        # make new canvas
        if self.canvas != None:
            self.canvas.pack_forget()
        self.canvas = Canvas(self, bg='black')
        # set geometry of window to match grid size
        self.geometry(str(len(grid[0])*self.sqsize)+'x'+str(len(grid)*self.sqsize))
           
        # loop over the grid
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                top = y * self.sqsize
                left = x * self.sqsize
                bottom = y * self.sqsize + self.sqsize - 2
                right = x * self.sqsize + self.sqsize - 2
                
                # color nodes on grid depending on their states
                current_node = grid[y][x]
                if current_node.closed == False:  
                    self.canvas.create_rectangle(left, top, right, bottom,
                                outline="#ffffff",
                                fill=self.color.get(current_node.type_))
                else:
                    self.canvas.create_rectangle(left, top, right, bottom,
                                outline=self.color.get(current_node.type_),
                                fill=self.color.get(current_node.type_))
                
                # make circles where the path goes
                if grid[y][x].onPath:
                    self.canvas.create_oval(left+10, top+10, right-10, bottom-10, fill="#000", width = 0.1)
        
        self.canvas.pack(fill=BOTH, expand=1)

        # redraw if not finished
        if finished == False:
            self.after(self.delay, self.run.run)

    # start the algorithm
    def playLevel(self, level):
        self.run.openFile(level)
        self.run.run()
    
    # select algorithm
    def setAlgorithm(self, alg):
        self.run.algorithm = alg
    

# main
def main():
    #boards = ['1-1', '1-2', '1-3', '1-4', '2-1', '2-2', '2-3', '2-4']
    #algorithms = [0, 1, 2]
    boards = ['2-1']
    algorithms = [0]
    # solve all the boards for all the algorithms
    for a in algorithms:
        for b in boards:
            app = GUI()
            app.setAlgorithm(a)
            app.playLevel('board-'+b+'.txt')
            app.mainloop()

# start program with call to main
main()
