# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158
from typing import Dict, List

def _suitable_agent(a:Dict) -> str:

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

    """

    def __init__(self,
                 name: str, 
                 data: Dict) -> None:
        
        self.name = name 
        self.data = data
        self.children = []
        self.agent = _suitable_agent(data)
        self.cost = self.data[self.agent]


    def add_child(self, a) -> None:
        self.children.append(a)

    def get_children(self) -> List:
        return self.children

class GoalTree:

    """
    This class creates Multi Agent Goal Generic Tree

    Parameters
    ----------
    root: GoalNode
        the root node of the tree

    Methods
    ----------
    set_root(self,GoalNode)
        set the root of the tree 
    
    level_order_tranversal(self)
        Tranverse through the tree in the level-by-level order
    
    """

    def __init__(self) -> None:
        self.root = None

    def set_root(self,a) -> None:
        self.root = a

    def level_order_transversal(self) -> None:
        if (self.root == None):
            return

        q = []
        q.append(self.root) #enqueue the root into the queue
        
        while len(q) != 0:
            n = len(q) #n = 1

            while (n > 0):
                p = q[0]
                q.pop(0)
                print(p.name + " " + p.agent, end = "\t")
                
                l = p.get_children()

                for i in range (len(l)):
                    q.append(l[i])#add the children into the queue
                n = n - 1

            print("\n" * 2)


def main() -> None:
    pass

if __name__ == "__main__":
    main()