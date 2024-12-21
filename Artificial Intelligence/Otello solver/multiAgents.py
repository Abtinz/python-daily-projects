from Agents import Agent
import util
import random

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """
    def __init__(self, *args, **kwargs) -> None:
        self.index = 0 # your agent always has index 0

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        It takes a GameState and returns a tuple representing a position on the game board.
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions(self.index)

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        The evaluation function takes in the current and proposed successor
        GameStates (Game.py) and returns a number, where higher numbers are better.
        You can try and change this evaluation function if you want but it is not necessary.
        """
        nextGameState = currentGameState.generateSuccessor(self.index, action)
        return nextGameState.getScore(self.index) - currentGameState.getScore(self.index)


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    Every player's score is the number of pieces they have placed on the board.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore(0)


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (Agents.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2', **kwargs):
        self.index = 0 # your agent always has index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent which extends MultiAgentSearchAgent and is supposed to be implementing a minimax tree with a certain depth.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)

    def getAction(self, state):
        """
        Returns the minimax action using self.depth and self.evaluationFunction

        But before getting your hands dirty, look at these functions:

        gameState.isGameFinished() -> bool
        gameState.getNumAgents() -> int
        gameState.generateSuccessor(agentIndex, action) -> GameState
        gameState.getLegalActions(agentIndex) -> list
        self.evaluationFunction(gameState) -> float
        """

        action , max_val = self.max_value(
            gameState=state, 
            depth=0, 
            agent_index=0
        )
        print(action, max_val)
        return action

    def min_value(self, gameState, depth, agent_index):

        if gameState.isGameFinished() or self.depth == depth:
            return None, self.evaluationFunction(gameState)
        
        action = None
        minimum_value = 1e14

        for current_action in gameState.getLegalActions(agent_index):

            current_index = (agent_index + 1) % gameState.getNumAgents()
            next_state = gameState.generateSuccessor(agent_index, current_action)
            #if current_index is zero it means that we are playing and its time for calling max nodes 
            if current_index == 0:

                _ , value = self.max_value(
                    gameState=next_state, 
                    depth=depth + 1, 
                    agent_index= current_index
                )

                if value < minimum_value:
                    minimum_value = value
                    action = current_action

            #if current_index is not zero it means that rivals are playing and its time for calling min nodes 
            else:
                
                _ , value = self.min_value(
                    gameState=next_state, 
                    depth=depth, 
                    agent_index= current_index
                )
                
                if value < minimum_value:
                    minimum_value = value
                    action = current_action

        return action, minimum_value

    
    def max_value(self, gameState, depth, agent_index):
        
        if gameState.isGameFinished() or depth == self.depth:
            return None, self.evaluationFunction(gameState)
        action = None
        maximum_val = -1e14
        for current_action in gameState.getLegalActions(agent_index):

            next_state = gameState.generateSuccessor(agent_index, current_action)
            _, value = self.min_value(
                gameState= next_state, 
                depth = depth, 
                agent_index= agent_index + 1
            )

            if value > maximum_val:
                action = current_action
                maximum_val = value
            
        return action, maximum_val
    
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning. It is very similar to the MinimaxAgent but you need to implement the alpha-beta pruning algorithm too.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        action , max_val = self.max_value(
            gameState =gameState, 
            depth=0, 
            agent_index=0, 
            alpha=-1e14, 
            beta=1e14
        )
        print(action, max_val)
        return action
        
    def min_value(self, gameState, depth, agent_index, alpha, beta):
        
        if gameState.isGameFinished() or depth == self.depth:
            return None, self.evaluationFunction(gameState)

        minimum = 1e14
        action = None
        for current_action in gameState.getLegalActions(agent_index):
            
            next_state = gameState.generateSuccessor(agent_index, current_action)
            current_index = (agent_index + 1) % gameState.getNumAgents()
            
            if current_index == 0:
                next_action, value = self.max_value(
                    gameState=next_state, 
                    depth=depth, 
                    agent_index=current_index, 
                    alpha= alpha, 
                    beta =beta
                )

            else:
                next_action, value = self.max_value(
                    gameState=next_state, 
                    depth=depth, 
                    agent_index=current_index + 1, 
                    alpha= alpha, 
                    beta =beta
                )
            

            if value < minimum:
                minimum = value
                action = minimum

            if minimum < alpha:
                return action, minimum

            if minimum < beta:
                beta = minimum

        return action, minimum
    
    def max_value(self, gameState, depth, agent_index, alpha, beta):
        
        if gameState.isGameFinished() or depth == self.depth:
            return None, self.evaluationFunction(gameState)

        maximum = -1e14
        action = None
        for current_action in gameState.getLegalActions(agent_index):
            next_state = gameState.generateSuccessor(agent_index, current_action)
            next_action, value = self.min_value(
                gameState= next_state,
                depth= depth + 1,
                agent_index= agent_index + 1,
                alpha= alpha, 
                beta=beta
            )

            if value > maximum:
                action = current_action
                maximum = value

            if maximum > beta:
                return action, maximum

            if maximum > alpha:
                alpha = maximum

        return action, maximum

    
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent which has a max node for your agent but every other node is a chance node.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All opponents should be modeled as choosing uniformly at random from their
        legal moves.
        """
        action , value = self.max_value(
            gameState=gameState, 
            depth=0, 
            agent_index=0
        )
        print(action, value)
        return action

    def average_value(self, gameState, depth, agent_index):
        if gameState.isGameFinished or self.depth == depth:
            return self.evaluationFunction(gameState)
        expected_sum = 0
        for current_action in gameState.getLegalActions(agent_index):
            next_action = gameState.generateSuccessor(agent_index, current_action)
            if (agent_index + 1) % gameState.getNumAgents() == 0:
                action, value = self.max_value(gameState=next_action,
                  depth= depth + 1, 
                  agent_index= 0
            )
            else:
                value = self.average_value(gameState=next_action,
                  depth= depth + 1, 
                  agent_index= (agent_index + 1) % gameState.getNumAgents()
            )
            

            expected_sum += value
        
        return expected_sum / len(gameState.getLegalActions(agent_index))

    def max_value(self, gameState, depth, agent_index):
        
        if depth == self.depth or gameState.isGameFinished():
            return None, self.evaluationFunction(gameState)
        maximum = -1e14
        action = None
        for current_action in gameState.getLegalActions(agent_index):
            next_state = gameState.generateSuccessor(agent_index, current_action)
            value = self.average_value(
                gameState=next_state, 
                depth=depth, 
                agent_index=agent_index + 1
            )
            if value > maximum:
                maximum = value
                action = current_action
        return action, maximum

        



def betterEvaluationFunction(currentGameState):
    """
    Your extreme evaluation function.

    You are asked to read the following paper on othello heuristics and extend it for two to four player rollit game.
    Implementing a good stability heuristic has extra points.
    Any other brilliant ideas are also accepted. Just try and be original.

    The paper: Sannidhanam, Vaishnavi, and Muthukaruppan Annamalai. "An analysis of heuristics in othello." (2015).

    Here are also some functions you will need to use:
    
    gameState.getPieces(index) -> list
    gameState.getCorners() -> 4-tuple
    gameState.getScore() -> list
    gameState.getScore(index) -> int

    """

    total_coin_value = 0
    maxCurrentPoints = 0
    minCurrentPoints = 1e14

    for number in currentGameState.getScore():
        if number < minCurrentPoints:
            minCurrentPoints = number
        if number > maxCurrentPoints :
           maxCurrentPoints = number 

    CoinParityHeuristicValue =  (maxCurrentPoints - minCurrentPoints)/(maxCurrentPoints + minCurrentPoints)
    CornerHeuristicValue = cornersHeuristic(currentGameState)
    
    MobilityHeuristicValue = mobilityHeuristic(currentGameState)
    StabilityHeuristicValue = staticHeuristic(currentGameState)

    evaluationValue = CoinParityHeuristicValue + CornerHeuristicValue + MobilityHeuristicValue + StabilityHeuristicValue
    
    return evaluationValue * 100
    
    

def cornersHeuristic(currentGameState):
    corners_owners_count = [ 0 for player in range(currentGameState.getNumAgents())]
    for corner in currentGameState.getCorners():
        if corner != -1:
            corners_owners_count[corner] += 1
    minimum_value = min(corners_owners_count)
    maximum_value = max(corners_owners_count)
    if minimum_value + maximum_value != 0 :
        return (maximum_value - minimum_value ) / (maximum_value + minimum_value )
    else :
        return 0
    
def staticHeuristic(currentGameState):
    minimum_value = 0
    maximum_value =  1e14
    for player in range(currentGameState.getNumAgents()):
        player_moves = 0
        for action in currentGameState.getLegalActions(player):
            if not currentGameState.placePiece(player, action) is None:
                player_moves += 1
                
        if player_moves > maximum_value : maximum_value = player_moves
        if player_moves < minimum_value : minimum_value = player_moves 
    
    if minimum_value + maximum_value != 0 :
        return (maximum_value - minimum_value ) / (maximum_value + minimum_value )
    else :
        return 0


def mobilityHeuristic(currentGameState):
    player_counts = currentGameState.getNumAgents()
   
    maximum_potential_len = 0
    minimum_potential_len= 1e14
    for index in range(player_counts):
        
        current_potential_moves = len(currentGameState.getPossibleActions(index))
        if current_potential_moves > maximum_potential_len :maximum_potential_len = current_potential_moves
        if current_potential_moves < minimum_potential_len :minimum_potential_len = current_potential_moves 
    
    if minimum_potential_len + maximum_potential_len != 0 :
        return (maximum_potential_len - minimum_potential_len ) / (maximum_potential_len + minimum_potential_len )
    else :
        return 0


# Abbreviation
better = betterEvaluationFunction