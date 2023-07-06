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
    agent: str
        Agent assigned to the node
    children: List
        List of child GoalNodes, initialized with an empty list
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of child Goals
    level_order_transversal(self)
        Traverse through the tree in the level-by-level order
    """

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost
        self.agent = None
        self.children = []

    def add_child(self, a):
        self.children.append(a)

    def get_children(self) -> List:
        return self.children
    
    def __lt__(self, other):
        # Compare based on the cost attribute
        return self.cost < other.cost


def level_order_transversal_two(root) -> None:
    """
    Traverses through the goal tree and prints out the goals (with the parent node in the front if the node has a parent)
    along with the assigned agent for each node.

    Parameters
    ----------
    root: GoalNode
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
            print(node.name + "Cost:", node.cost, "Assigned Agent:", node.agent, end="\n")

            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

            level_size -= 1

        print()  # Print a new line after traversing each level
