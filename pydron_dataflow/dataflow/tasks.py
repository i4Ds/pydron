# Copyright (C) 2015 Stefan C. Mueller
import logging

logger = logging.getLogger(__name__)


class AbstractTask(object):
    
    # Input ports required for refining.
    # We won't refine if the attribute is missing.
    #refiner_ports = set()
    
    # Maps input port to a function that takes one
    # argument. If the attribute exists then
    # this function is invoked with the value
    # and the return value is passed to `refine`
    # instead of the actual value.
    # The function must be defined in a module
    # so that it can be pickled.
    # The idea of this is to reduce the amount
    # of data that has to be transferred back
    # to the scheduler for refinement.
    #refiner_reducer = {}
    
    def input_ports(self):
        raise NotImplementedError("abstract")
    
    def output_ports(self):
        raise NotImplementedError("abstract")
    
    def subgraphs(self):
        return tuple()
    
    def evaluate(self, inputs):
        raise NotImplementedError("abstract")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not self == other
    def __hash__(self):
        return 1