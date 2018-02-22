# Copyright (C) 2015 Stefan C. Mueller

import ast

def contains_sideeffects(g):
    """
    Checks if the graph contains at least one task with
    a task property `syncpoint` which is `True`.
    
    It also checks subgraphs stored within tasks, given
    that the task objects have a `subgraphs()` method.
    """
    
    visited_graphs = set()
    
    def visit(g):
        
        # avoid infinite loops if subgraphs are cyclic.
        if id(g) in visited_graphs:
            return False
        visited_graphs.add(id(g))
        
        for tick in g.get_all_ticks():
            if g.get_task_properties(tick).get('syncpoint', False):
                return True
            
            task = g.get_task(tick)
            for subgraph in task.subgraphs():
                if visit(subgraph):
                    return True
        return False
    return visit(g)
    

def assert_graph_equal(expected, actual):
    
    def trim(lines):
        for line in lines:
            line = line.strip()
            if line:
                yield line
                
                
    if expected != actual:
        expected_clean = "\n".join(trim(repr(expected).splitlines()))
        actual_clean = "\n".join(trim(repr(actual).splitlines()))
    
        
        for i, (e, a) in enumerate(zip(expected_clean.splitlines(), actual_clean.splitlines())):
            if e != a:
                msg = "Difference on line %s: Expected %s got %s" % (i, repr(e), repr(a))
                break
        else:
            msg = "No difference in string representation."
        
        print(repr(expected))
        print(repr(actual))
        raise AssertionError("Graphs differ: %s" % msg)
