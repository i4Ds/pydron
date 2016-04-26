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


class ConstTask(AbstractTask):
    """
    Evaluates to a constant value.
    """

    def __init__(self, value):
        self.value = value

    def input_ports(self):
        return set()

    def output_ports(self):
        return {"value"}

    def evaluate(self, inputs):
        return {'value': self.value}

    def __repr__(self):
        return "ConstTask(" + repr(self.value) + ")"

    def __eq__(self, other):
        return self.value == other.value