#!/usr/bin/env python3
import logging
import sys,os
import numpy as np
import xarray as xr
from multiprocessing import freeze_support
from test import callAsProcesses

# my own function based on PyRADS
from compute_reanalysis_olr import getolrgcm

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)



#### PUT MY FUNCTION HERE
def computeolr(average, date, lon, start_lat, end_lat, delta_lat):
    '''
    compute_olr takes ERA5 reanalysis data (specific humidity, surface temperature, and ozone profiles) as input and then computes the outgoing longwave radiation of the atmospheric column with PYRADS, a line-by-line model, see https://github.com/ddbkoll/PyRADS.

    average: bool
        If True, then zonally-, annually-averaged data will be chosen. If False, then 6-hourly data will be chosen.
    date: string
        Enter date, e.g. for 15 September 1981 at 12:00, enter (1981-09-15T12:00:00
    lon: float
        Enter longitude, e.g. for 50 deg E, enter (50)
    start_lat: float
        Enter starting latitude of calculation
    end_lat: float
        Enter ending latitude of calculation
    delta_lat: float
        Enter spacing between latitude bands

    '''
    print( "I'm a printer, I print the start- and end- latitude of the computation. {} and {}".format(start_lat, end_lat))



if __name__ == '__main__':


#### PUT ARGUMENTS HERE
    myInputs=[]
    lats = np.linspace(-90,90,181)
    for lat in lats:
    myInputs.append({ "args": (True, '1981-03-15T12:00:00', 0, lat, lat, 1)})

#### CALL MY FUNCTION
   callAsProcesses( computeolr, myInputs )
