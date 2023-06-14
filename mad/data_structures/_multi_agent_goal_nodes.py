# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158

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
    """

    def __init__(self,
                 name: str, 
                 data: Dict, 
                 parents: List = [],
                 children: List = []) -> None:
        
        self.name = name 
        self.data = data

        self.parents = parents
        self.children = children
