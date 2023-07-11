import random as r
import copy
import matplotlib.pyplot as plt

from typing import Dict
from mad.data_structures import GoalNode, print_goal_tree
from mad.optimize import dfs_goal_allocation
from mad.optimize import optimized_goal_allocation

# Helper Functions
def _random_cost(m: int, n: int, agents: int) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        The starting point of the range
    n: int
        The ending point of the range
    
    Returns
    -------
    
    Dict[str,int]
        A dictionary with the agents as keys and corresponding costs as values
    
    """
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna"]

    d = {}
    for i in range(agents):
        d[AGENTS[i]] = r.randint(m,n)

    return d

def _random_agents(agents, m , n):
    chosen_agents = {}
    assigned_one = False

    for agent in agents:
        x = r.randint(0,1)
        if x == 1:
            chosen_agents[agent] = r.randrange(m, n)
            assigned_one = True

    if not assigned_one:
        agent = agents[r.randrange(0, len(agents))]
        chosen_agents[agent] = r.randrange(m, n)


    return chosen_agents

# Results Scraper
def get_results(agents_and_goals):

    best_case = 0
    total_cost = 0
    num_agents_used = 0
    agents_costs = []

    for agent in agents_and_goals.keys():
        
        if len(agents_and_goals[agent]) != 0:
            num_agents_used += 1

        curr_agent_cost = 0

        for goal in agents_and_goals[agent]:
            best_case += min(goal.data.values())
            curr_agent_cost += goal.cost
        
        agents_costs.append(curr_agent_cost)
        total_cost += curr_agent_cost

    discrepancy = abs(max(agents_costs) - min(agents_costs))
    skew = abs(best_case - total_cost)

    return [total_cost, skew, discrepancy, num_agents_used]

# Test Trees
def random_binary_symetric(num_agents):

    root = GoalNode("Main Goal", _random_cost(25, 45, num_agents))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20, num_agents))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 15, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 15, num_agents))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def random_binary_left():

    root = GoalNode("Main Goal", _random_cost(25, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    return root

def random_binary_right():

    root = GoalNode("Main Goal", _random_cost(25, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    return root

def random_root():

    root = root = GoalNode("Main Goal", _random_cost(25, 30))

    return root

def random_tree_symetric():

    root = GoalNode("Main Goal", _random_cost(30, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(5, 10))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(5, 10))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(5, 10))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)
    
    return root

def random_tree_left_right():

    root = GoalNode("Main Goal", _random_cost(30, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    return root

def random_large_binary_tree(num_agents):
    
    x = 40
    y = 60
    root = GoalNode("Main Goal", _random_cost(x, y, num_agents))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(x, y, num_agents))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(x, y, num_agents))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(x, y, num_agents))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(x, y, num_agents))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(x, y, num_agents))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(x, y, num_agents))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(x, y, num_agents))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(x, y, num_agents))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(x, y, num_agents))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(x, y, num_agents))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(x, y, num_agents))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(x, y, num_agents))
    subgoal13 = GoalNode("Sub Goal 13", _random_cost(x, y, num_agents))
    subgoal14 = GoalNode("Sub Goal 14", _random_cost(x, y, num_agents))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _random_cost(x, y, num_agents)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_cost(x, y, num_agents))
    subgoal17 = GoalNode("Sub Goal 17", _random_cost(x, y, num_agents))
    subgoal18 = GoalNode("Sub Goal 18", _random_cost(x, y, num_agents))
    subgoal19 = GoalNode("Sub Goal 19", _random_cost(x, y, num_agents))
    subgoal20 = GoalNode("Sub Goal 20", _random_cost(x, y, num_agents))
    subgoal21 = GoalNode("Sub Goal 21", _random_cost(x, y, num_agents))
    subgoal22 = GoalNode("Sub Goal 22", _random_cost(x, y, num_agents))
    subgoal23 = GoalNode("Sub Goal 23", _random_cost(x, y, num_agents))
    subgoal24 = GoalNode("Sub Goal 24", _random_cost(x, y, num_agents))
    subgoal25 = GoalNode("Sub Goal 25", _random_cost(x, y, num_agents))
    subgoal26 = GoalNode("Sub Goal 26", _random_cost(x, y, num_agents))
    subgoal27 = GoalNode("Sub Goal 27", _random_cost(x, y, num_agents))
    subgoal28 = GoalNode("Sub Goal 28", _random_cost(x, y, num_agents))
    subgoal29 = GoalNode("Sub Goal 29", _random_cost(x, y, num_agents))
    subgoal30 = GoalNode("Sub Goal 30", _random_cost(x, y, num_agents))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    return root

def random_binary_select_agents():

    AGENTS = ['grace', 'remus', 'franklin']

    root = GoalNode("Main Goal", _random_agents(AGENTS, 25, 40))
    subgoal1 = GoalNode("Sub Goal 1", _random_agents(AGENTS, 15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_agents(AGENTS, 15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_agents(AGENTS, 5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_agents(AGENTS, 5, 15))
    subgoal5 = GoalNode("Sub Goal 5", _random_agents(AGENTS, 5, 15))
    subgoal6 = GoalNode("Sub Goal 6", _random_agents(AGENTS, 5, 15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def random_tree_select_agents():

    AGENTS = ['grace', 'remus', 'franklin']

    root = GoalNode("Main Goal", _random_agents(AGENTS, 45, 80))
    subgoal1 = GoalNode("Sub Goal 1", _random_agents(AGENTS, 15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_agents(AGENTS, 15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_agents(AGENTS, 15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_agents(AGENTS, 5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_agents(AGENTS, 5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_agents(AGENTS, 5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_agents(AGENTS, 5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_agents(AGENTS, 5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_agents(AGENTS, 5, 10))
    subgoal10 = GoalNode("Sub Goal 10", _random_agents(AGENTS, 5, 10))
    subgoal11 = GoalNode("Sub Goal 11", _random_agents(AGENTS, 5, 10))
    subgoal12 = GoalNode("Sub Goal 12", _random_agents(AGENTS, 5, 10))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)

    return root

def random_large_binary_tree_select_agents():
    
    AGENTS = ['grace', 'remus', 'franklin']

    x = 40
    y = 60
    root = GoalNode("Main Goal", _random_agents(AGENTS, x, y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _random_agents(AGENTS, x, y))
    subgoal2 = GoalNode("Sub Goal 2", _random_agents(AGENTS, x, y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _random_agents(AGENTS, x, y))
    subgoal4 = GoalNode("Sub Goal 4", _random_agents(AGENTS, x, y))
    subgoal5 = GoalNode("Sub Goal 5", _random_agents(AGENTS, x, y))
    subgoal6 = GoalNode("Sub Goal 6", _random_agents(AGENTS, x, y))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _random_agents(AGENTS, x, y))
    subgoal8 = GoalNode("Sub Goal 8", _random_agents(AGENTS, x, y))
    subgoal9 = GoalNode("Sub Goal 9", _random_agents(AGENTS, x, y))
    subgoal10 = GoalNode("Sub Goal 10", _random_agents(AGENTS, x, y))
    subgoal11 = GoalNode("Sub Goal 11", _random_agents(AGENTS, x, y))
    subgoal12 = GoalNode("Sub Goal 12", _random_agents(AGENTS, x, y))
    subgoal13 = GoalNode("Sub Goal 13", _random_agents(AGENTS, x, y))
    subgoal14 = GoalNode("Sub Goal 14", _random_agents(AGENTS, x, y))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _random_agents(AGENTS, x, y)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_agents(AGENTS, x, y))
    subgoal17 = GoalNode("Sub Goal 17", _random_agents(AGENTS, x, y))
    subgoal18 = GoalNode("Sub Goal 18", _random_agents(AGENTS, x, y))
    subgoal19 = GoalNode("Sub Goal 19", _random_agents(AGENTS, x, y))
    subgoal20 = GoalNode("Sub Goal 20", _random_agents(AGENTS, x, y))
    subgoal21 = GoalNode("Sub Goal 21", _random_agents(AGENTS, x, y))
    subgoal22 = GoalNode("Sub Goal 22", _random_agents(AGENTS, x, y))
    subgoal23 = GoalNode("Sub Goal 23", _random_agents(AGENTS, x, y))
    subgoal24 = GoalNode("Sub Goal 24", _random_agents(AGENTS, x, y))
    subgoal25 = GoalNode("Sub Goal 25", _random_agents(AGENTS, x, y))
    subgoal26 = GoalNode("Sub Goal 26", _random_agents(AGENTS, x, y))
    subgoal27 = GoalNode("Sub Goal 27", _random_agents(AGENTS, x, y))
    subgoal28 = GoalNode("Sub Goal 28", _random_agents(AGENTS, x, y))
    subgoal29 = GoalNode("Sub Goal 29", _random_agents(AGENTS, x, y))
    subgoal30 = GoalNode("Sub Goal 30", _random_agents(AGENTS, x, y))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    return root

def main():

    # Jonathan Results
    test = []
    tree_score = []
    tree_skew = []
    tree_discrepancy = []
    tree_agents = []

    for i in range(5):
        
        # r.seed(1)

        print()
        print("---------------------")
        print(f"Test {i}:")
        print("---------------------")
        
        # Choose a tree
        root = random_binary_symetric(3)
        # root = random_binary_left()
        # root = random_binary_right()
        # root = random_root()
        # root = random_tree_symetric()
        # root = random_tree_left_right()
        # root = random_large_binary_tree(i)
        # root = random_binary_select_agents()
        # root = random_tree_select_agents()
        # root = random_large_binary_tree_select_agents()
        
        # ----- Jonathan Test -----
        root1 = copy.deepcopy(root)
        

        # Run algorithm
        agents_and_goals = dfs_goal_allocation(root1, 30, 1)

        # Get results
        total_cost, skew, discrepancy, num_agents_used = get_results(agents_and_goals)

        # Add data
        test.append(i)
        tree_score.append(total_cost)
        tree_skew.append(skew)
        tree_discrepancy.append(discrepancy)
        tree_agents.append(num_agents_used)


    
    # Create a figure and 3D axes
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Create the scatter plot
    # ax.scatter3D(tree_agents, tree_score, tree_descrepancy)
    ax.scatter3D(tree_agents, tree_skew, tree_discrepancy)

    # Add labels to the points
    for i in range(len(test)):
        ax.text(tree_agents[i], tree_skew[i], tree_discrepancy[i], f'{test[i]}', fontsize=8)

    # Set labels and title
    ax.set_xlabel('Number of Agents')
    ax.set_ylabel('Skew from Best Case')
    ax.set_zlabel('Descrepancy')
    ax.set_title('Algorithm Tests')

    # Show the plot
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    # Data for the bar graph
    # categories = test
    # values = tree_skew

    # # Create a figure and axis object
    # fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

    # # Create the bar graph

    # # Skew: I take the best case allocation (the sum of min possible cost of each selected goal) and find the difference in cost between the best case and my algorithm's total cost from its allcoation. Smaller is better
    # ax[0].bar(test, tree_skew)
    # # Discrepancy: Is the difference in total cost between the least assigned agent and the most assigned agent. Smaller is better
    # ax[1].bar(test, tree_discrepancy)

    # # Customize the graph
    # ax[0].set_xlabel('Agents')
    # ax[0].set_ylabel('Skew')
    # ax[0].set_title('Skew Tests')

    # ax[1].set_xlabel('Agents')
    # ax[1].set_ylabel('Discrepancy')
    # ax[1].set_title('Discrepancy Tests')

    # Display the graph
    # plt.show()

if __name__ == '__main__':
    main()
