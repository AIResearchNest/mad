# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158
from typing import Dict, List


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
        self.agent = None
        self.cost = None

    def set_agent(self, name, cost) -> None:
        self.agent = name
        self.cost = cost

    def add_child(self, a) -> None:
        self.children.append(a)

    def get_children(self) -> List:
        return self.children

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
                print(node.name + " " + node.agent, end="\t")

                children = node.get_children()
                for child in children:
                    q.append((child, node))  # Add the children into the queue along with their parent

                level_size -= 1

            print("\n" * 2)


def main() -> None:
    pass

if __name__ == "__main__":
    main()
