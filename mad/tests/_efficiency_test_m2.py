import random
from typing import Dict, List, Tuple
import heapq
import matplotlib.pyplot as plt


from mad.data_structures._multi_agent_goal_node_two import GoalNode2, level_order_transversal_two
from mad.optimize._goal_allocation import random_cost_m, agent_goal_m, compare_m, shortest_path_m, perform_auction_m, extract_node_info_m, get_agent_resources_m
    
   


def calculate_resources_usage(root_node, max_resources):
    """
    Calculates the resources of each agent being used based on their assignments.

    Parameters:
    root_node (GoalNode2): The root node of the goal tree.
    max_resources (List[int]): List of maximum resources for each agent.

    Returns:
    Dict[str, int]: Dictionary containing the resources used by each agent.
    """
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root_node)
    agent_resources = get_agent_resources_m(max_resources)
    
    

    

    if root_node.cost <= shortest_cost or (len(root_node.get_children()) == 0 and root_node.agent is not None):
        # Only calculate the resources used by the root node agent
        if isinstance(root_node.agent, str):
            agent_resources[root_node.agent] -= root_node.cost
        elif isinstance(root_node.agent, list):
            for agent in root_node.agent:
                agent_resources[agent] -= root_node.cost
    else:
        remaining_nodes = extract_node_info_m(root_node, shortest_goals[1:])
        real_nodes = []

        for node_name in shortest_goals[1:]:
            for node in remaining_nodes.values():
                if node.name == node_name:
                    real_nodes.append(node)
                    break
        
        
        def calculate_resources(nodes):
            nonlocal agent_resources

            for node in nodes:
                if isinstance(node.agent, str):
                    agent_resources[node.agent] = node.cost
                elif isinstance(node.agent, list):
                     for agent in node.agent:
                         agent_resources[agent] = node.cost ##
                else:
                    calculate_resources(node.children)

            # Set resources to 0 for agents not present in the nodes' agents list
            for agent in agent_resources:
                if agent not in [node.agent for node in nodes]:
                    agent_resources[agent] = 0

        calculate_resources(real_nodes)

    return agent_resources




def plot(root_node, max_resources):
    """
    Draws a bar plot showing the resources used by each agent.

    The x-axis represents the agent names (grace, remus, franklin),
    and the y-axis represents the amount of resources used.

    
    """

    agent_resources = calculate_resources_usage(root_node,  max_resources)

    agents = list(agent_resources.keys())
    resources = list(agent_resources.values())

    plt.bar(agents, resources, color='mediumpurple')
    plt.xlabel("Agents")
    plt.ylabel("Resources Used")
    plt.title("Agent Resources Usage")
    
    # Add y-axis values on each bar
    for i, value in enumerate(resources):
        plt.annotate(str(value), xy=(i, value), ha='center', va='bottom')
    plt.show()


    
def random_tree_left_right():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(15,25))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(5,15))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(5,15))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    
    max_resources = [ 45, 60, 70]
     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6,subgoal7,subgoal8, subgoal9]
    agent_goal_m(nodes, max_resources)
    return root

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

    goal_tree = GoalNode2("A", random_cost_m (45,60))
    B = GoalNode2("B", random_cost_m (25,35))
    C = GoalNode2("C", random_cost_m (25,35))
    D = GoalNode2("D", random_cost_m (25,35))
    E = GoalNode2("E", random_cost_m (15,20))
    F = GoalNode2("F", random_cost_m (15,20))
    G = GoalNode2("G", random_cost_m (15,20))
    S = GoalNode2("S", random_cost_m (15,20))
    H = GoalNode2("H", random_cost_m (15,20))
    I = GoalNode2("I", random_cost_m (15,20))
    J = GoalNode2("J", random_cost_m (10,15))
    K = GoalNode2("K", random_cost_m (10,15))
    L = GoalNode2("L", random_cost_m (10,15))
    M = GoalNode2("M", random_cost_m (10,15))
    N = GoalNode2("N", random_cost_m (10,15))
    O = GoalNode2("O", random_cost_m (10,15))
    P = GoalNode2("P", random_cost_m (10,15))
    Q = GoalNode2("Q", random_cost_m (5,10))
    R = GoalNode2("R", random_cost_m (5,10))
    T = GoalNode2("T", random_cost_m (5,10))
    U = GoalNode2("U", random_cost_m (5,10))
    V = GoalNode2("V", random_cost_m (1,5))
    W = GoalNode2("W", random_cost_m (1,5))

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
    
      
    
    max_resources = [ 45, 60, 70]
     
 
    nodes = [goal_tree, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W]

    agent_goal_m(nodes, max_resources)



    return goal_tree



def main():
    root1 = _scalability_test_tree()
    max_resources1 = [45, 60, 70]
    root2 = random_tree_left_right()
    

    level_order_transversal_two(root1)
    agent_resources = calculate_resources_usage(root1, max_resources1)
    plot(root1, max_resources1)

if __name__ == '__main__':
    main()

