# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158
from typing import Dict, List

def _suitable_agent(a: Dict) -> str:

    """
    Decides which agent will conduct the current goal based on cost

    Parameters
    ----------
    a : Dict[str: int]
        Dictionary containing the cost values for each agent

    Returns
    -------
    name: str
        Name of the agent with the minimum cost.
    """    
    if not a:
        return None
    min_cost = list(a.values())[0]
    name = list(a.keys())[0]
    for key, value in a.items():
        if value < min_cost:
            min_cost = value
            name = key
    
    return name


class GoalNode:

    """
    This class creates Multi Agent Goal Nodes

    Attributes
    ----------
    name : str
        Goal Name
    data : dict
        Dictonary containing key as agent and value as planning cost
    children: List
        List of children GoalNodes, initializing with an empty list
    agent: str
        Agent that costs the least
    cost: int
        Most optimized cost
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of the Child Goals

    level_order_tranversal(self)
        Tranverse through the tree in the level-by-level order
    """

    def __init__(self,
                 name: str, 
                 data: Dict) -> None:
        
        self.name = name 
        self.data = data
        self.children = []
        self.agent = _suitable_agent(self.data)
        self.cost = self.data[self.agent]
        self.d = self.data.copy()

    def switch_agent(self) -> bool:
        if len(self.d) == 1:
            print("No agent is capable to complete " + self.name)
            self.agent = None
            self.cost = None
            return False
        self.d.pop(self.agent)
        print(self.d)
        self.agent = _suitable_agent(self.d)
        self.cost = self.d[self.agent]
        return True

    def add_child(self, a) -> None:
        self.children.append(a)

    def get_children(self) -> List:
        return self.children
"""
class Agent:

    def __init__(self, name, maximum_resources):
        self.name = name
        self.max = maximum_resources

    def conduct_goal(self, cost):
        self.max -= cost
    
    def cancel_goal(self, cost):
        self.max += cost

    def maximum_resource(self):
        return self.maximum_resource

"""
    
def level_order_transversal(root) -> None:
        
        """
        Transverses through the goal tree and prints out the goals (with the parent node in the front if the node has a parent)

        Parameters
        ----------
        root : GoalNode
            The root of the goal tree

        """
        if root is None:
            return

        q = []
        q.append((root, None)) # enqueue the root into the queue

        while len(q) != 0:
            level_size = len(q)

            while level_size > 0:
                node, parent = q.pop(0)
                if parent is not None:
                    print(parent.name + "|", end="")  # Print branch symbol if the node has a parent
                if (node.agent != None):
                    print(node.name + " " + node.agent + " " + str(node.cost), end="\t")
                else:
                       print(node.name, end="\t")

                children = node.get_children()
                for child in children:
                    q.append((child, node))  # Add the children into the queue along with their parent

                level_size -= 1

            print("\n" * 2)


