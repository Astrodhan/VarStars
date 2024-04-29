"""
Tool for creating data for plotting periodograms with SAI web tool from SNAD ZTF data
Web tool: http://scan.sai.msu.ru/lk/
SNAD database: https://ztf.snad.space/
Author: Yashodhan M, April 2024
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

#Stage 1: Reading data off the csv files

def read_data(path,fileName):
    
    lcdata = pd.read_csv(path+fileName+".csv")

    mjd = lcdata['mjd'].to_numpy() #Modified Julian Date
    mag = lcdata['mag'].to_numpy() #Magnitude values, irrespective of the filter
    mag_err = lcdata['magerr'].to_numpy() #Error in magnitude
    filter = lcdata['filter'].to_numpy() #Name of the filter

    jd = mjd+2400000.5 #Converting to Julian Date

    return jd, filter, mag, mag_err

#Stage 2: Separating magnitude data from different filters into different csv files usable by the SAI periodogram web tool

def separator(jd,filter,mag,mag_err):
    
    length = len(jd)
    jd_zg = []
    jd_zr = []
    jd_zi = []
    mag_zg = []
    mag_zr = []
    mag_zi = []
    mag_err_zg = []
    mag_err_zr = []
    mag_err_zi = [] #Just initialising
    for i in range(length):
        if filter[i]=="zg":
            jd_zg.append(jd[i])
            mag_zg.append(mag[i])
            mag_err_zg.append(mag_err[i])
        if filter[i]=="zr":
            jd_zr.append(jd[i])
            mag_zr.append(mag[i])
            mag_err_zr.append(mag_err[i])
        if filter[i]=="zi":
            jd_zi.append(jd[i])
            mag_zi.append(mag[i])
            mag_err_zi.append(mag_err[i])
    
    return jd_zg, jd_zr, jd_zi, mag_zg, mag_zr, mag_zi, mag_err_zg, mag_err_zr, mag_err_zi

#Stage 3: Saving them as different csv files with just the jd, mag and mag_err (as needed by the web tool at )

def save_files(path, fileName, jd_zg, jd_zr, jd_zi, mag_zg, mag_zr, mag_zi, mag_err_zg, mag_err_zr, mag_err_zi):
    data_zg = {'JD':jd_zg, 'mag':mag_zg, 'mag_err':mag_err_zg}
    data_zr = {'JD':jd_zr, 'mag':mag_zr, 'mag_err':mag_err_zr}
    data_zi = {'JD':jd_zi, 'mag':mag_zi, 'mag_err':mag_err_zi}

    data_zg_df = pd.DataFrame(data_zg)
    data_zr_df = pd.DataFrame(data_zr)
    data_zi_df = pd.DataFrame(data_zi)

    data_zg_df.to_csv(path+"zg/"+fileName+"_zg"+".txt", sep='\t', index=False)
    data_zr_df.to_csv(path+"zr/"+fileName+"_zr"+".csv", sep='\t', index=False)
    data_zi_df.to_csv(path+"zi/"+fileName+"_zi"+".csv", sep='\t', index=False)

#Stage 4: Running a loop over all the files in the data folder
def generate_split_lc_csvs(path_input, path):
    
    files = os.listdir(path_input)
    fileNames = [os.path.splitext(file)[0] for file in files] #Removing the .csv extensions, will add them in save_files function
    os.makedirs(path+"zg/", exist_ok=True)
    os.makedirs(path+"zr/", exist_ok=True)
    os.makedirs(path+"zi/", exist_ok=True)

    for fileName in fileNames:
        jd,filter,mag,mag_err = read_data(path_input, fileName)
        jd_zg, jd_zr, jd_zi, mag_zg, mag_zr, mag_zi, mag_err_zg, mag_err_zr, mag_err_zi = separator(jd,filter,mag,mag_err)
        save_files(path, fileName, jd_zg, jd_zr, jd_zi, mag_zg, mag_zr, mag_zi, mag_err_zg, mag_err_zr, mag_err_zi)

#Now the main function:
def main():
    path_input = "data/original/"
    path = "data/"
    generate_split_lc_csvs(path_input, path)

#Run the main function
main()
