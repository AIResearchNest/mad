import random as r
from typing import Dict, List, Tuple
import heapq
from collections import deque

# Start of class

class GoalNode2:
    """
    This class creates Multi Agent Goal Nodes. 

    Attributes
    ----------
    name : str
        Goal Name
    cost : int
        Cost associated with the node
    agents : Dict[str, int]
        Dictionary of agents and their cost values
    children : List
        List of child GoalNode2s, initialized with an empty list
    assigned_agent : List
        Name of the agent assigned to the goal node
    """
    """
    Methods
    ----------
    
    """

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost
        self.agents = {}
        self.children = []
        self.assigned_agent = ""  
        self.parent = []

    

    
    def get_children(self) -> List['GoalNode2']:
        """
        Return the list of child Goals
        """
        return self.children


    def set_agents(self, agents: Dict[str, int]):
        """
        Set the agents dictionary for the node
        """
        self.agents = agents
    
    def get_parent(self) -> List:
        """
        Gives the lists with parents of the node
        """
        return self.parent
    
    
    def __lt__(self, other) -> bool:
        """
        Defines the less than (<) operator for comparing GoalNode2 objects. It compares the costs of the nodes for the priority queue.

        Parameters
        ----------
        other : GoalNode2
            The other GoalNode2 object to compare with.

        Returns
        -------
        bool
            True if the current node's cost is less than the other node's cost, False otherwise.
        """
        return self.cost < other.cost


    def add_child(self, child: 'GoalNode2') -> None:
        """
        Add Child Goal into the Children list and set the parent of the child.

        Parameters
        ----------
        child : GoalNode2
            The child node to be added.
        """
        self.children.append(child)
        child.set_parent(self)
        

    def set_parent(self, parent: 'GoalNode2'):
        """
        Set the parent of the node.

        Parameters
        ----------
        parent : GoalNode2
            The parent node of the current node.
        """
        if not isinstance(parent, list):
            parent = [parent]
        self.parent = parent

    def get_sibling_cost(self, sibling_name):
        """
        Get the cost of the sibling node with the given name.

        Parameters
        ----------
        sibling_name : str
            The name of the sibling node.

        Returns
        -------
        sibling.cost : int
            The cost of the sibling node.
        """
    
        for parent in self.parent:  # Iterate over the list of parent nodes
            for sibling in parent.get_children():
                if sibling.name == sibling_name:
                    return sibling.cost
        return 0

   

    def get_child_cost(self, child_name):
        """
        Get the cost of a child node with the given name.

        Parameters
        ----------
        child_name : str
            The name of the child node.

        Returns
        -------
        int
            The cost of the child node.
        """
        for child in self.children:
            if child.name == child_name:
                return child.cost
        return 0

    
    def get_parent_cost(self, node_name):
        """
        Get the cost of the parent node.

        Parameters
        ----------
        node_name : str
            The name of the current node.

        Returns
        -------
        int
            The cost of the parent node.
        """
        return self.parent.cost if self.parent and self.parent.name == node_name else 0
    





def level_order_transversal_two(root) -> None:
    """
    Traverses through the goal tree and prints out the goals (with the parent node and children node in the front if the node has a child)
    along with the assigned agent for each node and respective costs.
    
    Parameters
    ----------
    root: GoalNode2
        The root of the goal tree
    """
    if root is None:
        return

    q = []
    q.append((root, None))  # enqueue the root into the queue

    while len(q) != 0:
        level_size = len(q)

        while level_size > 0:
            node, parent = q.pop(0)
            if parent is not None:
                print(parent.name + "|", end="")  # Print branch symbol if the node has a parent
            print(node.name + " GoalCost:", node.cost, "Agents:", node.agents, "\nAssigned Agent:", node.assigned_agent,"\n",end="\n")

            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

            level_size -= 1

        print()  # Print a new line after traversing each level
        
        
