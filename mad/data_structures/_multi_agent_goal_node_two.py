import random
from typing import Dict, List, Tuple
import heapq

# Start of class

class GoalNode2:
    """
    This class creates Multi Agent Goal Nodes

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
    assigned_agent : str
        Name of the agent assigned to the goal node

    Methods
    ----------
    add_child(self, GoalNode2)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode2]
        Return the list of child Goals
    set_agents(self, agents: Dict[str, int])
        Set the agents dictionary for the node
    """

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost
        self.agents = {}
        self.children = []
        self.assigned_agent = ""  # New attribute for assigned agent

    def add_child(self, a):
        self.children.append(a)

    def get_children(self) -> List:
        return self.children

    def set_agents(self, agents: Dict[str, int]):
        self.agents = agents
    
    def __lt__(self, other):
        """
        Defines the less than (<) operator for comparing GoalNode2 objects.
        It compares the costs of the nodes for the priority queue.

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




def level_order_transversal_two(root) -> None:
    """
    Traverses through the goal tree and prints out the goals (with the parent node and children node in the front if the node has a child)
    along with the assigned agent for each node and costs
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
            print(node.name + " GoalCost:", node.cost, "Agents:", node.agents, "\nAssigned Agent:", node.assigned_agent,end="\n")

            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

            level_size -= 1

        print()  # Print a new line after traversing each level