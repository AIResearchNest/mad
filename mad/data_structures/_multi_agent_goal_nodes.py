from typing import Dict, List

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
    
    Variables
    ---------
    assigned_agent : str
        Name of the agent goal is assigned to
    """

    def __init__(self, 
                name: str,
                data: Dict,
                parents: List = [],
                children: List = []) -> None:
        
        self.name = name
        self.data = data or {}
        self.parents = parents or []
        self.children = children or []
        self.assigned_agent = None

    # Adds a parent GoalNode to current GoalNode
    def add_parent(self, parent_node):
        self.parents.append(parent_node)

    # Adds a child GoalNode to current GoalNode
    def add_child(self, child_node):
        self.children.append(child_node)

    # Prints tree visibly
    def print_tree(self, indent=0):
        prefix = "  " * indent
        print(f"{prefix}- {self.name}")
        for child in self.children:
            child.print_tree(indent + 1)
