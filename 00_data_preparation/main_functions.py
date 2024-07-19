# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 08:37:10 2022
@author: Emelie Chandni
"""
# Import libraries
import sys
sys.path.append('../')
import pandas as pd

# Import own modules
from data_preparation import DataPreparation

def read_data_from_file(agent):    
    dataset = pd.read_csv('../saved_data/bird_migration.csv') 
    prepModule = DataPreparation(agent, dataset)
    prepModule.select_agent()
    prepModule.plot_single_agent()