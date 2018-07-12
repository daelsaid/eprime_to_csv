#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 23:22:57 2018

@author: dawlat_local
"""

from os.path import join
import pandas
import os
from eprime_txt_to_csv import eprimetxt_todf, remove_unicode

files=[f for f in os.listdir('.') if os.path.isfile(f)]
data_dir = os.getcwd() #current directory

for f in files:
    filename, ext = os.path.splitext(f)
    if ext=='.txt':
        text_file = join(data_dir,f)
        subj=filename.split('-')[1]
        tp=filename.split('-')[2]
        new_subj=filename+'.csv'
        out_file=new_subj
        convert_eprime(text_file,outfile)