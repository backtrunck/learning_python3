# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 08:32:27 2018

@author: luiscar
"""


import logging

import auxiliary_module

#create logger with 'spam_application
logger= logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

#create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

#create console handler with higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#add handler to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creatting an instance of Auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxilary_module.Auxiliary.do_something')

logger.info('calling auxiliary_module.some_function')
auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')

fh.close()
