import math
import time


def max_val(state, alpha=None, beta=None):
    # TODO Q2 (b): implement, Q2 (c): extend
    # goal state?
    if state == 0:
        return 1 
    
    value = float('-inf')
    for i in [1,2]:
        new_state = state - i
        if new_state >= 0:
            value = max(value, min_val(new_state,alpha,beta))
            
            if alpha != None and beta != None:
                if value >= beta:
                    return value
                alpha = max(alpha,value)  
    return value


def min_val(state, alpha=None, beta=None):
    # TODO Q2 (b), Q2 (c)
    if state == 0:
        return -1
    value = float("inf")
    for i in [1,2]:
        new_state = state - i
        if new_state >= 0:
            value = min(value, max_val(new_state,alpha,beta))
            
            if alpha != None and beta != None:
                if value <= alpha:
                    return value
                beta = min(beta,value)    
    return value

def possible_actions(state):
    return [1,2] if state >=2 else [1]


def minimax(state):
    return max(possible_actions(state),key= lambda action: min_val(state-action))
    
    


def alphabeta_pruning(state):
    # TODO Q2 (c)
    return max([1,2],key= lambda action: min_val(state-action, alpha=float('-inf'), beta=float('inf')))
    


def measure_time(function, state):
    start_time = time.time()
    function(state)
    duration = time.time() - start_time
    return duration

if __name__ == "__main__":
    # TODO Q2 (d)
    for i in [3,  6, 20, 35]:
        print("\nNum. coins:", i)

        # Minimax
        print("Minimax:", 
                "MAX" if minimax(i) == 1 else "MIN")
        duration = measure_time(minimax,i)
        print("Time needed for Minimax " + str(duration) + " seconds")

        # Alpha-beta pruning
        print("Alpha-beta pruning:", 
                "MAX" if alphabeta_pruning(i) == 1 else "MIN")
        duration = measure_time(alphabeta_pruning,i)
        print("Time needed for Minimax " + str(duration) + " seconds")


