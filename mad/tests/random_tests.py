import random as r
import copy
import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d

from typing import Dict
from mad.data_structures import GoalNode
from mad.optimize import dfs_goal_allocation
from mad.optimize import optimized_goal_allocation

# Helper Functions
def _random_cost(m: int, n: int) -> Dict[str, int]:
    
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
    
    d = {}
    d["grace"] = r.randint(m,n)
    d["remus"] = r.randint(m,n)
    d["franklin"] = r.randint(m,n)
    #print(d)
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

# Functions
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
def random_binary_symetric():

    root = GoalNode("Main Goal", _random_cost(25, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 20))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 20))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 15))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 15))

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

def random_large_binary_tree():
    
    x = 30
    y = 60
    root = GoalNode("Main Goal", _random_cost(x, y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(x, y))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(x, y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(x, y))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(x, y))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(x, y))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(x, y))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(x, y))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(x, y))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(x, y))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(x, y))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(x, y))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(x, y))
    subgoal13 = GoalNode("Sub Goal 13", _random_cost(x, y))
    subgoal14 = GoalNode("Sub Goal 14", _random_cost(x, y))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _random_cost(x, y)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_cost(x, y))
    subgoal17 = GoalNode("Sub Goal 17", _random_cost(x, y))
    subgoal18 = GoalNode("Sub Goal 18", _random_cost(x, y))
    subgoal19 = GoalNode("Sub Goal 19", _random_cost(x, y))
    subgoal20 = GoalNode("Sub Goal 20", _random_cost(x, y))
    subgoal21 = GoalNode("Sub Goal 21", _random_cost(x, y))
    subgoal22 = GoalNode("Sub Goal 22", _random_cost(x, y))
    subgoal23 = GoalNode("Sub Goal 23", _random_cost(x, y))
    subgoal24 = GoalNode("Sub Goal 24", _random_cost(x, y))
    subgoal25 = GoalNode("Sub Goal 25", _random_cost(x, y))
    subgoal26 = GoalNode("Sub Goal 26", _random_cost(x, y))
    subgoal27 = GoalNode("Sub Goal 27", _random_cost(x, y))
    subgoal28 = GoalNode("Sub Goal 28", _random_cost(x, y))
    subgoal29 = GoalNode("Sub Goal 29", _random_cost(x, y))
    subgoal30 = GoalNode("Sub Goal 30", _random_cost(x, y))
    
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

    x = 30
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
    tree_descrepancy = []
    tree_agents = []

    # Fay Results
    test1 = []
    tree_score1 = []
    tree_skew1 = []
    tree_descrepancy1 = []
    tree_agents1 = []

    for i in range(10):
        
        print()
        print("---------------------")
        print(f"Test {i}:")
        print("---------------------")
        
        # Choose a tree
        root = random_binary_symetric()
        # root = random_binary_left()
        # root = random_binary_right()
        # root = random_root()
        # root = random_tree_symetric()
        # root = random_tree_left_right()
        # root = random_large_binary_tree()
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
        tree_descrepancy.append(discrepancy)
        tree_agents.append(num_agents_used)


        # ----- Fay Test -----
        # print('\n' * 4)
        # root2 = copy.deepcopy(root)

        # if root2 is None:
        #     return

        # q = []
        # q.append((root2, None)) 

        # while len(q) != 0:
        #     level_size = len(q)

        #     while len(q) > 0:  
        #         node, parent = q.pop(0)
        #         node.initial_agent_assign()
        #         children = node.get_children()
        #         for child in children:
        #             q.append((child, node)) 

        # agents_and_goals = optimized_goal_allocation(root2, [30,30,30])
        
        # Need a function similar to get_results that returns total_cost, skew, discrepancy, num_agents_used for graphing purposes



    # Print results
    # for i in range(len(test)):

    #     print('\n')
    #     print(f"\nJonathan Test: {test[i]}\n---------------")
    #     print(f"Cost: {tree_score[i]}\nSkew: {tree_skew[i]}\nDiscrepancy: {tree_descrepancy[i]}\nNumber of Agents: {tree_agents[i]}")

        # print(f"\nFay Test: {test1[i]}\n---------------")
        # print(f"Cost: {tree_score1[i]}\nSkew: {tree_skew1[i]}\nDiscrepancy: {tree_descrepancy1[i]}\nNumber of Agents: {tree_agents1[i]}")


    # Create a figure and 3D axes
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Create the scatter plot
    # ax.scatter3D(tree_agents, tree_score, tree_descrepancy)
    ax.scatter3D(tree_agents, tree_skew, tree_descrepancy)

    # Add labels to the points
    for i in range(len(test)):
        ax.text(tree_agents[i], tree_skew[i], tree_descrepancy[i], f'{test[i]}', fontsize=8)

    # Set labels and title
    ax.set_xlabel('Number of Agents')
    ax.set_ylabel('Skew from Best Case')
    ax.set_zlabel('Descrepancy')
    ax.set_title('Algorithm Tests')

    # Show the plot
    plt.show()

if __name__ == '__main__':
    main()
