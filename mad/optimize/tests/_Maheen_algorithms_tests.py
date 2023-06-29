import random
from typing import Dict, List, Tuple
import heapq

from mad.data_structures.Maheen_multi_agent_goal_nodes import GoalNode, level_order_transversal
from mad.optimize._maheen_optimize import maheen_random_cost, maheen_perform_auction, maheen_compare, maheen_shortest_path


def main():
    #"\n\nNodes cost assignment:\n"
    G1 = GoalNode("G1", maheen_random_cost(1, 20))  # Assigning random cost values between 1-20 to nodes
    G2 = GoalNode("G2", maheen_random_cost(1, 20))
    G3 = GoalNode("G3", maheen_random_cost(1, 20))
    G4 = GoalNode("G4", maheen_random_cost(1, 20))
    G5 = GoalNode("G5", maheen_random_cost(1, 20))
    G6 = GoalNode("G6", maheen_random_cost(1, 20))
    G7 = GoalNode("G7", maheen_random_cost(1, 20))

    print("\nAgents assignment to Goals:\n")
    # Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G3.add_child(G6)
    G3.add_child(G7)

    # Define agent resources and initial balances
    agent_resources = {"grace": 30, "remus": 50, "franklin": 40}

    # Iterate through each goal node and perform the auction
    nodes = [G1, G2, G3, G4, G5, G6, G7]
    for node in nodes:
        maheen_perform_auction(node, agent_resources)

        # Print the updated node information after each assignment
        level_order_transversal(G1)
        print("Updated Agent Resources:", agent_resources)
        print("\n")
    #shortest_cost, shortest_goals, shortest_agents = _optimize_tree(G1)
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(G1)

    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    print("\nList of Agents:", shortest_agents)
    maheen_compare(shortest_cost, G1.cost)

if __name__ == "__main__":
    main()

