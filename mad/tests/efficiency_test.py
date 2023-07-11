#
#_____SCALABILITY TEST_____
#
from mad.data_structures import GoalNode, GoalNode2, print_goal_tree, level_order_transversal, level_order_transversal_two
from mad.optimize import optimized_goal_allocation,  dfs_goal_allocation
from typing import Dict
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
# Define the goal tree
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

level_order_transversal(goal_tree)
# Set the maximum resources for each agent (same resources)
max_resources = [40,40,40]

#__FAY'S ALGORITHM__
print("\n\n\nFay's Algorithm:\n")

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
level_order_transversal(goal_tree2)
fresult, fresources = optimized_goal_allocation(goal_tree2, max_resources)

f_remaining_resources = 0
f_agent_cost = [0,0,0]
f_agent_goals = [0,0,0]

for agent, goals in fresult.items():
    for goal in goals:
        if goal.agent == "grace":
            f_agent_cost[0] += goal.cost
            f_agent_goals[0] += 1
        elif goal.agent == "remus":
            f_agent_cost[1] += goal.cost
            f_agent_goals[1] += 1
        else:
            f_agent_cost[2] += goal.cost
            f_agent_goals[0] += 1

# Total goal cost for Fay's Algorithm
f_util_res = sum(f_agent_cost)

#__JONATHAN'S ALGORITHM__
goal_tree1 = copy.deepcopy(goal_tree)
print("Jonathan's Algorithm:\n")
jresult = dfs_goal_allocation(goal_tree1, max_resources[0],1)

j_agent_cost = [0,0,0]
j_agent_goals = [0,0,0]

# Get the number of goals each agent assigned and cost consumed
print(jresult)
for agent_goals in jresult:
    agent = agent_goals[0]
    goals = agent_goals[1]
    
    for goal in goals:
        if goal.agent == "grace":
            j_agent_cost[0] += goal.cost
            j_agent_goals[0] += 1
        elif goal.agent == "remus":
            j_agent_cost[1] += goal.cost
            j_agent_goals[1] += 1
        else:
            j_agent_cost[2] += goal.cost
            j_agent_goals[2] += 1
   
    j_util_res = sum(j_agent_cost)

#__PLOT__
# Define the algorithm names and total resource utilization values
algorithm_names = ['Fay\'s Algorithm', 'Jonathan\'s Algorithm']
total_utilization_values = [f_util_res, j_util_res]

# Define the agents
agents = ['grace', 'remus', 'franklin']

# Set the width of the bars
bar_width = 0.35

# Create the figure and axis
fig, ax = plt.subplots()

# Set the positions of the bars on the x-axis
x = np.arange(len(agents))

# Plot the bars for Jonathan's Algorithm
rects1 = ax.bar(x, j_agent_cost, width=bar_width, label="Jonathan's Algorithm", color='black')

# Plot the bars for Fay's Algorithm
rects2 = ax.bar(x + bar_width, f_agent_cost, width=bar_width, label="Fay's Algorithm", color='light blue')

# Add the total resources used as text annotations
ax.text(0, max(j_agent_cost) + 1, f"Total Resources: {j_util_res}", ha='center')
ax.text(1, max(f_agent_cost) + 1, f"Total Resources: {f_util_res}", ha='center')

# Set the labels and title
ax.set_xlabel('Agents')
ax.set_ylabel('Cost')
ax.set_title('Cost Comparison by Agent')
ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(agents)
ax.legend()

# Display the plot
plt.show()