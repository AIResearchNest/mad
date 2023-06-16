# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158

from typing import Dict, List
from queue import Queue
import random

class GoalNode:

    """
    This class creates Multi Agent Goal Nodes

    Parameters
    ----------
    name : str
        Goal Name
    data : dict
        Dictonary containing key as agent and value as planning cost

    Variables
    ---------
    parents: List, default []
        List of Parent GoalNodes
    children: List, default []
        List of children GoalNodes
    chosen_agent: GoalNode
        Agent chosen to accomplish that task
    chosen_agent_cost = int
        Cost of the chosen_agent to accomplish that task
    """

    # Special
    def __init__(self,
                name: str, 
                data: Dict) -> None:
        
        self.name = name 
        self.data = data
        self.parents = []
        self.children = []
        self.chosen_agent = None
        self.chosen_agent_cost = None

    def __str__(self):
        return f"Goal Name: {self.name}\nData: {self.data}\nChosen Agent: {self.chosen_agent}"
    
    # Public
    def get_children(self):
        return self.children
    
    def get_parents(self):
        return self.parents


class GoalTree:
    '''
    This class creates a Hierarchical Goal Tree

    Parameters
    ----------
    root : GoalNode
        Root node

    Variables
    ---------
    size: int
        Number of nodes in the tree
    '''

    # Special
    def __init__(self, 
                root: GoalNode = None) -> None:
        
        self.root = root
        self.size = 1
    
    # Private
    def level_search(self):
        output = []
        Q = Queue()
        Q.put(self.root)
        while (not Q.empty()):
            node = Q.get()
            if node == None:
                continue
            output.append(node)
            for child in node.get_children():
                Q.put(child)
        return output
    
    # Public
    def add_node(self, parent, node):

        if self.root == None:
            self.root = node
        else:
            parent.children.append(node)
            for parent_parent in parent.get_parents():
                node.parents.append(parent_parent)
            node.parents.append(parent)
        self.size += 1

    def print_tree(self):
        for node in self.level_search():
            print(node.name)

    def random_agent(self):
        # Gives each goal node to a random agent that can accomplish it
        total_cost = 0
    
        for node in self.level_search():
            # Finding best agent and cost
            random_agent = random.choice(list(node.data.keys()))
            random_agent_cost = node.data[random_agent]

            # Updating node values
            node.chosen_agent = random_agent
            node.chosen_agent_cost = random_agent_cost

            # Output updating
            total_cost += random_agent_cost
            
            # print(f"[{random_agent}, {random_agent_cost}], ")
        return total_cost
    
    def best_fit_agent(self):
        # Gives each goal node to the agent that can accomplish it the easiest
        total_cost = 0

        for node in self.level_search():
            # Finding best agent and cost
            best_agent = min(node.data, key=lambda k: node.data[k])
            best_agent_cost = node.data[best_agent]

            # Updating node values
            node.chosen_agent = best_agent
            node.chosen_agent_cost = best_agent_cost

            # Output updating
            total_cost += best_agent_cost
        return total_cost

    # def dijkstras_algorithm(self):


def main():
    node0 = GoalNode("G0", {"grace": 9, "remus": 3, "franklin": 8})
    node1 = GoalNode("G1", {"grace": 7, "remus": 16, "franklin": 4})
    node2 = GoalNode("G2", {"grace": 5, "remus": 6, "franklin": 7})
    
    tree = GoalTree(node0)
    tree.add_node(node0, node1)
    tree.add_node(node0, node2)
    # tree.print_tree()

    # Solution 1: Random
    print("Random Agent: ", tree.random_agent())

    # Solution 2: Best fit
    print("Best Fit Agent: ", tree.best_fit_agent())
    

if __name__ == "__main__":
    main()
