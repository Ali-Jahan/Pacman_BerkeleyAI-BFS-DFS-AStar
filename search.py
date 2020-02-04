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

import util

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
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


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

    start = problem.getStartState()
    fringe = util.Stack()
    visited = []
    path = []
    fringe.push((start, visited, path))    # fringe stack
                                    # first attribute is the start state,
                                    # second is the visited nodes ([])
                                    # third is the path ([])
    while not fringe.isEmpty():
        state, visited, actions = fringe.pop()
        if problem.isGoalState(state):
            return path
        for x in problem.getSuccessors(state):
            successor, direction, cost = x
            if not successor in visited:
                fringe.push((successor, visited + [state], actions + [direction]))
                path = actions + [direction]
    return path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    fringe = util.Queue()
    visited = []
    path = []
    fringe.push((start, visited, path))
    while not fringe.isEmpty():
        state, costs, path = fringe.pop()
        if not state in visited:
            visited += [state]
            if problem.isGoalState(state):
                return path
            for x in problem.getSuccessors(state):
                successor, direction, cost = x
                fringe.push((successor, visited + [state], path + [direction]))
    return path

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    visited = []
    path = []
    fringe = util.PriorityQueue()
    fringe.push((start, path, 0), 0)
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if not state in visited:
            visited += [state]
            if problem.isGoalState(state):
                return path
            for x in problem.getSuccessors(state):
                successor, direction, sucCost = x
                fringe.push((successor, path + [direction],
                             cost + sucCost), cost + sucCost)
    return path
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    visited = []
    path = []
    initial_cost = 0
    initial_heuristic = heuristic(start, problem)
    fringe = util.PriorityQueue()
    fringe.push((start, path, initial_cost), initial_heuristic)
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if state not in visited:
            visited += [state]
            if problem.isGoalState(state):
                return path
            for x in problem.getSuccessors(state):
                successor, direction, sucCost = x
                total_cost = cost + sucCost
                total = total_cost + heuristic(successor, problem)
                fringe.push((successor, path + [direction], total_cost), total)
    return path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
