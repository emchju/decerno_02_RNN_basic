# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 04:55:10 2021

@author: Emelie Chandni
"""
# Import own modules
from main_functions import read_data_from_file
from parameters import glodbal_settings

agents = glodbal_settings['agents']

read_data_from_file(agents[0])