#!/usr/bin/env python
'''
Created on 18.04.2018

@author: trevaz (tristan.revaz@epfl.ch)

---------------------------------------------------------------------------------
app: edit
---------------------------------------------------------------------------------
'''

#################################################################################
# IMPORTS
#################################################################################
import os
from fctlib import get_case_path

#################################################################################
# CONSTANTS
#################################################################################
EDITOR_NAME = 'nano'

#################################################################################
# MAIN FUNCTION
#################################################################################
def edit(PATH, case_name):
    '''
    DEF:    edit case.
    INPUT:  - case_name: name of the case, type=string
    OUTPUT: - ()
    '''
    case_path = get_case_path(PATH, case_name)
    os.system(EDITOR_NAME + ' ' + str(os.path.join(case_path, 'input','config')))
