# Copyright (C) 2015 Stefan C. Mueller

from pydron_dataflow.translation import translator
from pydron_dataflow.interpreter import blocking
from pydron_dataflow import picklesupport

import logging
import functools

logger = logging.getLogger(__name__)


def schedule(f):
    
    @functools.wraps(f)
    def call(*args, **kwargs):
        dataflowcallable = translator.translate_function(f, blocking.BlockingScheduler())
        return dataflowcallable(*args, **kwargs)
    
    return call
    


def functional(func):
    func.functional = True
    return func
    
