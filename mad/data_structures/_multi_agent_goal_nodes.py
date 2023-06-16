_multi_agent_goal_nodes.py
# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158

from typing import Dict, List

def _suitable_agent(a:Dict) -> str:
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

    Parameters
    ----------
    name : str
        Goal Name
    data : dict
        Dictonary containing key as agent and value as planning cost
    children: List, default []
        List of children GoalNodes, initializing with an empty list
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
    name : str
        Goal Name
    data : dict
        Dictonary containing key as agent and value as planning cost
    children: List, default []
        List of children GoalNodes, initializing with an empty list

    Methods
    ----------

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
                print(p.name, end = "\t")
                
                l = p.get_children()

                for i in range (len(l)):
                    q.append(l[i])#add the children into the queue
                n = n - 1

            print("\n" * 2)


def main() -> None:
    t = GoalTree()
    

    G1 = GoalNode("G1",{"grace": 13, "franklin": 14, "remus": 12})
    G2 = GoalNode("G2",{"grace": 3, "franklin": 2, "remus": 5})
    G3 = GoalNode("G3",{"grace": 4, "franklin": 14, "remus": 15})
    
    G1.add_child(G2)
    G1.add_child(G3)
    """
    G4 = GoalNode("G4",{"grace": 10, "franklin": 12, "remus": 8})
    G5 = GoalNode("G5",{"grace": 3, "franklin": 12, "remus": 8})
    G6 = GoalNode("G6",{"grace": 14, "franklin": 4, "remus": 6})
    G7 = GoalNode("G7",{"grace": 11, "franklin": 2, "remus": 4})
    G8 = GoalNode("G8",{"grace": 3, "franklin": 2, "remus": 2})
    G9 = GoalNode("G9",{"grace": 5, "franklin": 6, "remus": 8})
    
    
    
    G2.add_child(G4)
    G2.add_child(G5)
    
    G4.add_child(G6)
    G4.add_child(G7)

    G3.add_child(G8)
    G3.add_child(G9)

    """
    t.set_root(G1)
    t.level_order_transversal()

if __name__ == "__main__":
    main()