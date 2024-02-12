import cython
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import shutil
import sys 
from configobj import ConfigObj
import json 
from distutils.util import strtobool
import h5py
from calfews_src.model_cy import Model
from calfews_src.inputter_cy import Inputter
from calfews_src.scenario import Scenario
from calfews_src.util import *
from calfews_src.plotter import *
from calfews_src.visualizer import Visualizer
from datetime import datetime


#output_folder = "/home/fs02/pmr82_0001/rg727/CALFEWS-main/results/baseline_ensemble/2/"+section_number+"/"
output_folder = "/home/fs02/pmr82_0001/rg727/baseline_calfews/CALFEWS_CDEC_millerton_change/results/millerton_change/"


if not os.path.exists(output_folder):
  os.makedirs(output_folder)

#base_inflow_filename = " /home/fs02/pmr82_0001/rg727/CALFEWS/2/"+section_number+"/base_inflows.json"
#base_inflow_filename = " /home/fs02/pmr82_0001/rg727/CALFEWS/"+ensemble_number+"/4/base_inflows.json"

command = "python run_main_cy.py " + output_folder + " 1 1" 
os.system(command)


# results hdf5 file location from CALFEWS simulations
output_file = output_folder + 'results.hdf5'


fig_folder = output_folder + 'figs/'

if not os.path.exists(fig_folder):
  os.makedirs(fig_folder)

# now load simulation output
datDaily = get_results_sensitivity_number_outside_model(output_file, '')
 

fig = plt.figure(figsize=(15,6))
ax = plt.subplot(121)
ax.plot(datDaily['shasta_SNPK'], label='Shasta')
ax.plot(datDaily['oroville_SNPK'], label='Oroville')
ax.plot(datDaily['millerton_SNPK'], label='Millerton')
ax.plot(datDaily['isabella_SNPK'], label='Isabella')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Snowpack (inch)')
t = plt.xticks(rotation=315)

ax = plt.subplot(122)
ax.plot(datDaily['shasta_Q'], label='Shasta')
ax.plot(datDaily['oroville_Q'], label='Oroville')
ax.plot(datDaily['millerton_Q'], label='Millerton')
ax.plot(datDaily['isabella_Q'], label='Isabella')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Inflow (taF/day)')
ax.set_yscale('log')
t = plt.xticks(rotation=315)
plt.savefig(fig_folder+'Figure1.png')

fig = plt.figure(figsize=(15,6))
ax = plt.subplot(121)
ax.plot(datDaily['shasta_S'], label='Shasta')
ax.plot(datDaily['oroville_S'], label='Oroville')
ax.plot(datDaily['millerton_S'], label='Millerton')
ax.plot(datDaily['isabella_S'], label='Isabella')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Storage (tAF)')
t = plt.xticks(rotation=315)

ax = plt.subplot(122)
ax.plot(datDaily['delta_HRO_pump'], label='Banks')
ax.plot(datDaily['delta_TRP_pump'], label='Tracy')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Pumping (taF/day)')
# ax.set_yscale('log')
t = plt.xticks(rotation=315)
plt.savefig(fig_folder+'Figure2.png')



fig = plt.figure(figsize=(15,6))
ax = plt.subplot(121)
ax.plot(datDaily['swpdelta_contract'], label='SWP Table A')
ax.plot(datDaily['friant1_contract'], label='CVP Friant')
ax.plot(datDaily['cvpexchange_contract'], label='CVP Exchange')
ax.plot(datDaily['kingsriver_contract'], label='Kings')
ax.plot(datDaily['kernriver_contract'], label='Kern')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Contract Deliveries (tAF)')
t = plt.xticks(rotation=315)

ax = plt.subplot(122)
ax.plot(datDaily['centralcoast_tableA_delivery'], label='Central Coast')
ax.plot(datDaily['losthills_tableA_delivery'], label='Lost Hills')
ax.plot(datDaily['semitropic_tableA_delivery'], label='Semitropic')
ax.plot(datDaily['wheeler_tableA_delivery'], label='Wheeler Ridge-Maricopa')
ax.plot(datDaily['socal_tableA_delivery'], label='SoCal')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Contract Deliveries (tAF)')
t = plt.xticks(rotation=315)
plt.savefig(fig_folder+'Figure3.png')



fig = plt.figure(figsize=(15,6))
ax = plt.subplot(121)
ax.plot(datDaily['kwb_DLR'], label='Dudley Ridge')
# ax.plot(datDaily['kwb_KCWA'], label='KCWA')
ax.plot(datDaily['kwb_ID4'], label='KCWA ID4')
ax.plot(datDaily['kwb_SMI'], label='Semitropic')
ax.plot(datDaily['kwb_TJC'], label='Tejon-Castac')
ax.plot(datDaily['kwb_WRM'], label='Wheeler Ridge-Maricopa')
ax.plot(datDaily['kwb_WON'], label='Wonderful Company')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Kern Water Bank balance (tAF)')
t = plt.xticks(rotation=315)
plt.savefig(fig_folder+'Figure4.png')


