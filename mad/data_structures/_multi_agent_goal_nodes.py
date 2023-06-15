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
    parents: List, default []
        List of Parent GoalNodes
    children: List, default []
        List of children GoalNodes
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
    '''

    # Special
    def __init__(self, 
                root: GoalNode = None) -> None:
        
        self.root = root
    
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

    def print_tree(self):
        for node in self.level_search():
            print(node.name)

    def random_solution(self):
        solution_cost = 0
        solution_path = []
        for node in self.level_search():
            random_agent = random.choice(list(node.data.keys()))
            random_agent_cost = node.data[random_agent]
            solution_cost += random_agent_cost
            solution_path.append(node.name)
            # print(f"[{random_agent}, {random_agent_cost}], ")
        return [solution_cost, solution_path]
    
    def best_fit_solution(self):
        solution_cost = 0
        solution_path = []
        for node in self.level_search():
            best_agent = min(node.data, key=lambda k: node.data[k])
            best_agent_cost = node.data[best_agent]
            solution_cost += best_agent_cost
            solution_path.append(node.name)
            # print(f"[{best_agent}, {best_agent_cost}], ")
        return [solution_cost, solution_path]



def main():
    node0 = GoalNode("G0", {"grace": 9, "remus": 3, "franklin": 8})
    node1 = GoalNode("G1", {"grace": 7, "remus": 16, "franklin": 4})
    node2 = GoalNode("G2", {"grace": 5, "remus": 6, "franklin": 7})
    
    tree = GoalTree(node0)
    tree.add_node(node0, node1)
    tree.add_node(node0, node2)
    # tree.print_tree()

    # Solution 1: Random
    print("Random Solution: ", tree.random_solution())

    # Solution 2: Best fit
    print("Best Fit Solution: ", tree.best_fit_solution())
    


if __name__ == "__main__":
    main()