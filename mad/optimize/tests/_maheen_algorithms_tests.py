import random
from typing import Dict, List, Tuple
import heapq

from mad.data_structures.Maheen_multi_agent_goal_nodes import GoalNode, level_order_transversal
from mad.optimize._maheen_optimize import maheen_random_cost, maheen_perform_auction, maheen_compare, maheen_shortest_path, maheen_agent_goal, maheen_extract_node_info


def main():
    #"\n\nNodes cost assignment:\n"
    G1 = GoalNode("G1", maheen_random_cost(1, 30))  # Assigning random cost values between 1-20 to nodes
    G2 = GoalNode("G2", maheen_random_cost(1, 20))
    G3 = GoalNode("G3", maheen_random_cost(1, 20))
    G4 = GoalNode("G4", maheen_random_cost(1, 20))
    G5 = GoalNode("G5", maheen_random_cost(1, 20))
    G6 = GoalNode("G5", maheen_random_cost(1, 20))

    # Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G3.add_child(G6)

    # Define agent resources and initial balances
    agent_resources = {"grace": 40, "remus": 50, "franklin": 30}

    # Iterate through each goal node and perform the auction
    nodes = [G1, G2, G3, G4, G5,G6]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(G1)
    print("\nInitial cost allocation:")
    level_order_transversal(G1)
    maheen_compare(shortest_cost, G1.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(G1, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    for name, cost in node_info.items():
        if G1.cost < shortest_cost:
            print(f"Node: {G1.name}\tCost: {G1.cost}")
            maheen_perform_auction(G1, agent_resources)
        else:
            print(f"Node: {name}\tCost: {cost}")
            node = next((n for n in nodes if n.name == name), None)
            if node:
                maheen_perform_auction(node, agent_resources)
        level_order_transversal(G1)
        print("Updated Agent Resources:", agent_resources)
        print("\n")

    
if __name__ == "__main__":
    main()
