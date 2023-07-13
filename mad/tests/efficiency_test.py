from mad.data_structures import GoalNode, GoalNode2, print_goal_tree, level_order_transversal, level_order_transversal_two
from mad.optimize import optimized_goal_allocation,  dfs_goal_allocation
from typing import Dict
import random
import copy
import numpy as np
import matplotlib.pyplot as plt

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
    d["grace"] = random.randint(m,n)
    d["remus"] = random.randint(m,n)
    d["franklin"] = random.randint(m,n)
    return d


#
#____SCALABILITY TEST_____
#
def _scalability_test_tree():

    """

                    A
                    / | \
                B  C  D
                / |  /\  | \
                E  F  G S H  I
            /|    / \   /| \ 
            J K   L  M  N O  P
            / \           / \
            Q   R         T   U
        / \         
        V   W
    """

    goal_tree = GoalNode("A", _random_cost (45,60))
    B = GoalNode("B", _random_cost (25,35))
    C = GoalNode("C", _random_cost (25,35))
    D = GoalNode("D", _random_cost (25,35))
    E = GoalNode("E", _random_cost (15,20))
    F = GoalNode("F", _random_cost (15,20))
    G = GoalNode("G", _random_cost (15,20))
    S = GoalNode("S", _random_cost (15,20))
    H = GoalNode("H", _random_cost (15,20))
    I = GoalNode("I", _random_cost (15,20))
    J = GoalNode("J", _random_cost (10,15))
    K = GoalNode("K", _random_cost (10,15))
    L = GoalNode("L", _random_cost (10,15))
    M = GoalNode("M", _random_cost (10,15))
    N = GoalNode("N", _random_cost (10,15))
    O = GoalNode("O", _random_cost (10,15))
    P = GoalNode("P", _random_cost (10,15))
    Q = GoalNode("Q", _random_cost (5,10))
    R = GoalNode("R", _random_cost (5,10))
    T = GoalNode("T", _random_cost (5,10))
    U = GoalNode("U", _random_cost (5,10))
    V = GoalNode("V", _random_cost (1,5))
    W = GoalNode("W", _random_cost (1,5))

    goal_tree.add_child(B)
    goal_tree.add_child(C)
    goal_tree.add_child(D)

    B.add_child(E)
    B.add_child(F)
    C.add_child(G)
    C.add_child(S)
    D.add_child(H)
    D.add_child(I)

    E.add_child(J)
    E.add_child(K)
    G.add_child(L)
    G.add_child(M)
    I.add_child(N)
    I.add_child(O)
    I.add_child(P)

    J.add_child(Q)
    J.add_child(R)
    Q.add_child(V)
    Q.add_child(W)
    O.add_child(T)
    O.add_child(U)

    return goal_tree


#
#____BINARY SYMMETRIC TREE_____
#
def _binary_symmetric():
    
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

#
#____BINARY LEFT TREE_____
# 

def _binary_left():

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
#
#____BINARY RIGHT TREE_____
# 

def _binary_right():

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

#
#____ROOT-ONLY TREE_____
# 

def _root():

    root = root = GoalNode("Main Goal", _random_cost(25, 30))

    return root

#
#____SYMMETRIC TREE_____
#

def _symmetric():

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

#
#____LEFT RIGHT TREE_____
#

def _left_right():

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

#
#____LARGE BINARY TREE_____
#

def _large_binary():
    
    x = 40
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



#__RUNNING THE ALGO AND PLOTTING
def effiency_test_and_plotting(goal_tree, title, max_res):
    
    level_order_transversal(goal_tree)

    # Set the maximum resources for each agent (same resources)
    max_resources = [max_res] * 3
    #__FAY'S ALGORITHM__
    print("\nFay's Algorithm:\n")

    goal_tree2 = copy.deepcopy(goal_tree)

    q = []
    q.append((goal_tree2, None)) 

    while len(q) != 0:
        level_size = len(q)

        while len(q) > 0:  
            node, parent = q.pop(0)
            node.initial_agent_assign()
            children = node.get_children()
            for child in children:
                q.append((child, node)) 
    fresult, fresources = optimized_goal_allocation(goal_tree2, max_resources)

    f_remaining_resources = 0
    f_agent_cost = [0,0,0]
    f_agent_goals = [0,0,0]

    for agent, goals in fresult.items():
        for goal in goals:
            print(goal.name + ": " + agent + " " + str(goal.cost))

            if goal.agent == "grace":
                f_agent_cost[0] += goal.cost
                f_agent_goals[0] += 1
            elif goal.agent == "remus":
                f_agent_cost[1] += goal.cost
                f_agent_goals[1] += 1
            else:
                f_agent_cost[2] += goal.cost
                f_agent_goals[2] += 1

    # Total goal cost for Fay's Algorithm
    f_util_res = sum(f_agent_cost)
    f_agent_cost.append(f_util_res)
    f_agent_goals.append(sum(f_agent_goals))


    #__JONATHAN'S ALGORITHM__
    goal_tree1 = copy.deepcopy(goal_tree)
    print("\n\nJonathan's Algorithm:")
    jresult = dfs_goal_allocation(goal_tree1, max_resources[0],0)

    j_agent_cost = [0,0,0]
    j_agent_goals = [0,0,0]

    # Get the number of goals each agent assigned and cost consumed
    for agent, goals in jresult.items():
        for goal in goals:
            print(goal.name + ": " + agent + " " + str(goal.cost))
            if agent == "grace":
                j_agent_cost[0] += goal.cost
                j_agent_goals[0] += 1
            elif agent == "remus":
                j_agent_cost[1] += goal.cost
                j_agent_goals[1] += 1
            else:
                j_agent_cost[2] += goal.cost
                j_agent_goals[2] += 1
        
    j_util_res = sum(j_agent_cost)
    j_agent_cost.append(j_util_res)
    j_agent_goals.append(sum(j_agent_goals))

    #__PLOT__
    # Define the algorithm names and total resource utilization values
    algorithm_names = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm']

    # Define the agents
    agents = ['grace', 'remus', 'franklin', 'total']

    # Set the width of the bars
    bar_width = 0.35

    # Create the figure and axis
    # Create the figure and axes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    # Plot 1: Resource Cost Comparison
    # Set the positions of the bars on the x-axis
    x = np.arange(len(agents))

    # Plot the bars for Jonathan's Algorithm
    rects1 = ax1.bar(x, j_agent_cost, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects2 = ax1.bar(x + bar_width, f_agent_cost, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    #Increase the length of the y-axis
    ax1.set_ylim(0, max(max(j_agent_cost), max(f_agent_cost)) + 20)

    # Set the labels and title
    ax1.set_xlabel('Agents')
    ax1.set_ylabel('Resource Cost')
    ax1.set_title(f'{title} - COST COMPARISON BY AGENT')
    ax1.set_xticks(x + bar_width / 2)
    ax1.set_xticklabels(agents)
    ax1.legend()

    # Add annotations for the resource cost
    for rect in rects1:
        height = rect.get_height()
        ax1.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        
    for rect in rects2:
        height = rect.get_height()
        ax1.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        

    # Plot 2: Goal Count Comparison

    rects3 = ax2.bar(x, j_agent_goals, width=bar_width, label="Jonathan's Algorithm", color='lightblue')

    # Plot the bars for Fay's Algorithm
    rects4 = ax2.bar(x + bar_width, f_agent_goals, width=bar_width, label="Fay's Algorithm", color='peachpuff')

    ax2.set_ylim(0, max(max(j_agent_goals), max(f_agent_goals)) + 5)
    # Set the labels and title
    ax2.set_xlabel('Agents')
    ax2.set_ylabel('Number of Goals')
    ax2.set_title(f'{title} - COST COMPARISON BY AGENT')
    ax2.set_xticks(x + bar_width / 2)
    ax2.set_xticklabels(agents)
    ax2.legend()

    # Add annotations for the resource cost
    for rect in rects3:
        height = rect.get_height()
        ax2.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        
    for rect in rects4:
        height = rect.get_height()
        ax2.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        
    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=1)  # Increase the hspace value to increase spacing between subplots
    plt.show()
    return f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals

   

import matplotlib.pyplot as plt

def main():
    test_cases = [(_scalability_test_tree, "SCALABILITY TEST", 40), (_binary_symmetric, "BINARY SYMMETRIC TREE", 20), (_binary_left, "BINARY LEFT TREE", 20), (_binary_right, "BINARY RIGHT TREE", 20), (_symmetric, "SYMMETRIC TREE", 25), (_root, "ROOT-ONLY TREE", 35), (_left_right, "LEFT RIGHT TREE", 20), (_large_binary, "LARGE BINARY TREE", 30)]

    markers = ['^', 'D']
    colors = ['peachpuff', 'lightblue']
    agents = ['grace', 'remus', 'franklin', 'total']
    algorithms = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm']
    

    for i, (generate_tree, title, max_res) in enumerate(test_cases):

        algo_results_fay = []
        algo_results_jonathan = []
        agents_fay = []
        agents_jonathan = []
        results = []
        # Run each goal tree
        for _ in range(5):
            tree = generate_tree()
            print(title)
            f_agent_cost, f_agent_goals, j_agent_cost, j_agent_goals = effiency_test_and_plotting(tree, title, max_res)
            f_agents = sum([1 for agent in f_agent_goals[:3] if agent != 0])
            j_agents = sum([1 for agent in j_agent_goals[:3] if agent != 0])

            algo_results_fay.append(sum(f_agent_cost[:3]))
            algo_results_jonathan.append(sum(j_agent_cost[:3]))

            agents_fay.append(f_agents)
            agents_jonathan.append(j_agents)

        results.append((algo_results_fay, algo_results_jonathan))
        fig, ax = plt.subplots(figsize=(8, 6))

        # Scatter plot for Fay's Algorithm
        ax.scatter(agents_fay, algo_results_fay, c=[colors[0]] * len(algo_results_fay), s=50, label=f'{algorithms[0]}', marker='D')

        # Scatter plot for Jonathan's Algorithm
        ax.scatter(agents_jonathan, algo_results_jonathan, c=[colors[1]] * len(algo_results_jonathan), s=50, label=f'{algorithms[1]}')

        ax.set_ylim(0, max(max(algo_results_fay), max(algo_results_jonathan)) +20)

        ax.set_xlabel('Number of Agents Used')
        ax.set_ylabel('Total Cost')
        ax.set_title(f'{title} - RESOURCES AND GOALS SCATTERPLOT')
        ax.legend()

        plt.xticks(ticks=np.arange(1, len(agents) + 1))  # Set x-axis ticks as agent names
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

main()


