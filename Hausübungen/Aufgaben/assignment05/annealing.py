import numpy as np
import random
# (a)
def simulated_anneling(start_state, schedule, find_conflicts):
    """Implements the simulated annealing algorithm with the given schedule"""

    # schedule should be a function that takes an integer time parameter, i.e.:
    num_steps = 0
    # temperature = schedule(num_steps)
    
    
    solution = start_state
    
    current_state = start_state
    while True:

        temperature = schedule(num_steps)
        current_state_conflicts = find_conflicts(current_state)
        if temperature == 0:
            solution = current_state
            return solution,num_steps
        if current_state_conflicts == 0:
            solution = current_state
            return solution,num_steps
        next_state = find_random_successor(current_state)
        next_state_conflicts = find_conflicts(next_state)
        delta_energy = (-next_state_conflicts) - (-current_state_conflicts)
        if delta_energy > 0:
            current_state = next_state
        
        else:
            probability = np.exp(delta_energy/ temperature)
            random_number = np.random.rand()
            if (probability > random_number):
                current_state = next_state
            
        num_steps += 1

    return solution, num_steps

def find_random_successor(state):
    """Finds new random variation of the given state

    Args:
        state (List): current State of the 8-Queens

    Returns:
        List: new random variation of a possible 8-Queens State
    """
    
    new_state = state.copy()
    i,j = random.sample(range(len(new_state)),2)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    
    return new_state

def find_conflicts(state):
    """finds conflicst in row or diagonal of a 8-Queens problem

    Args:
        state (List): state of a 8-Queens problem

    Returns:
        int: Number of conflicts 
    """
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1,n):
            
            # checks for horizontal conflicts
            if state[i] == state[j]:
                conflicts += 1
            
            # checks for diagonal conflicts
            deltaRow = abs(state[i]-state[j])
            deltaCol = abs(i-j)
            
            if deltaRow == deltaCol:
                conflicts+=1
    return conflicts

def schedule(t):
    """reduces temperature for simmulated annealing

    Args:
        t (int): amount of steps needed for the current state
    Returns:
        int: new temperature
    """
    
    return 1/(t+1)

def logarithmic_schedule(t):
    """implementation of logarithmic schedule

    Args:
        t (int): amount of steps needed for the current state

    Returns:
        int: new temperature according to schedular
    """
    initial_temperature = 1
    return initial_temperature/np.log(1+t)

def boltzmann_schedule(t):
    """implementation of Boltzmann schedule

    Args:
        t (int): amount of steps needed for the current state

    Returns:
        int: new temperature according to schedualr
    """
    initial_temperature = 1
    return initial_temperature/(1+np.log(1+t))

def exponential_schedule(t):
    """implementation of an exponential schedule

    Args:
        t (int): amount of steps needed for the current state

    Returns:
        int: new temperature according to schedualr
    """
    initial_temperature = 1
    alpha = np.random.rand()#
    return initial_temperature * (alpha**t)



# (b)
def measure_schedule(schedule, num_runs=100):
    """Execute the simulated annealing multiple times with the given schedule
       and average the results"""
    start_state = [1,2,3,4,5,6,7,8]
    steps=[]
    for i in range(num_runs):
        state = start_state.copy()
        solution, num_steps = simulated_anneling(state,schedule,find_conflicts)
        steps.append(num_steps)
    
    return np.sum(steps, axis=0)/num_runs


def get_name_of_scheduler(scheduler):
    """Returns String identifier for scheduler

    Args:
        scheduler (Function): Fucntion which describes a scheduler

    Returns:
        String: name of scheduler
    """
    name = ""
    if scheduler == schedule:
        name= "1/t"
    elif scheduler == logarithmic_schedule:
        name= "Logarithmic Scheduler"
    elif scheduler == boltzmann_schedule:
        name= "Exponential Scheduler"
    elif scheduler == exponential_schedule:
        name= "Exponential scheduler"
    return name

def run_for_mulltiple_schedulers():
    """Utility function for running measure_schedule with multiple schedulers
    """
    schedulers = [schedule, logarithmic_schedule, boltzmann_schedule, exponential_schedule]
    
    
    for scheduler in schedulers:
        num_runs = 100
        mean_steps = measure_schedule(scheduler, num_runs)
        name = get_name_of_scheduler(scheduler)
        print("###########################################################################")
        print(f"Scheduler {name}")
        print(f"Mean of steps for {num_runs} runs: {mean_steps}")

if __name__ == "__main__":
    start_state = [1,2,3,4,5,6,7,8]
    run_for_mulltiple_schedulers()
    
    
    
