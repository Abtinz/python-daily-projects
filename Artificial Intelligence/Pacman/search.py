# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import PriorityQueue, Queue, Stack , raiseNotDefined


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #we used Stack LIFO beacuse we need to proccess nodes in depth and its means that we will proccess the left node in each row and its childs
    fringe = Stack()
    visited = []
    fringe.push(
            ( 
                problem.getStartState() #the starting point state of he problem
                , [] #actions list
            )
    )
    while not fringe.isEmpty():
        state, actions = fringe.pop() #so we reached to the goal and code shuld stop here and return the actions
        if problem.isGoalState(state): return actions #we add this here beacuse we dont need to expand nodes again and avoiding from loops      
        if not state in visited: #now we expand it and visit it
            visited.append(state)  
            for successorState, successorAction , __ in problem.getSuccessors(state):
                fringe.push((successorState, actions + [successorAction])) #And now expanding the childrens by the lifo order ...
    return [] #we didnt find any goal node in this problem ...

def breadthFirstSearch(problem):
    #we used Queue FIFO beacuse we need to proccess nodes row by row from the left to the rigth
    fringe = Queue()
    visited = []
    fringe.push(
            ( 
                problem.getStartState() #the starting point state of he problem
                , [] #actions list
            )
    )
    while not fringe.isEmpty():
        state, actions = fringe.pop()   
        if problem.isGoalState(state): return actions #so we reached to the goal and code shuld stop here and return the actions
        if not state in visited: #we add this here beacuse we dont need to expand nodes again and avoiding from loops
            visited.append(state) #now we expand it and visit it
            for successorState, successorAction , __ in problem.getSuccessors(state):
                    fringe.push((successorState, actions + [successorAction])) #And now expanding the entire row
    return []

    
def uniformCostSearch(problem):
    fringe =  PriorityQueue()
    visited = {}
    fringe.push(( problem.getStartState(), [] , 0 ) , 0)
    while not fringe.isEmpty():
        state, actions , cost = fringe.pop() 
        if problem.isGoalState(state):  
            return actions
        if ( not state in visited) or (cost < visited[state]):
            visited[state] = cost
            for successorState, successorAction, successorCost in problem.getSuccessors(state):    
                newCost =  cost + successorCost 
                fringe.update(( successorState , actions + [successorAction] , newCost) , newCost ) 
        
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    fringe = PriorityQueue()
    visited = {}
    fringe.push(
            ( 
                problem.getStartState() #the starting point state of he problem
                , [] #actions list
                , 0 #cost
        ) , 0 #cost for priority for A* algorithm
    )
    #itration on the fringe queue
    while not fringe.isEmpty():
        #expansion of node
        state, actions, cost = fringe.pop()
        if problem.isGoalState(state):  return actions #so we reached to the goal and code shuld stop here and return the actions
        if state not in visited or cost < visited[state]: #its new or the newst cost for this stat is lower
            visited[state] = cost #updating visited
            for successorState, successorAction, successorCost in problem.getSuccessors(state):
                newCost = cost + successorCost
                totalCost = newCost + heuristic(successorState, problem)
                fringe.update((successorState, actions + [successorAction], newCost), totalCost)
    return []
               

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
