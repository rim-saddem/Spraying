# -*- coding: utf-8 -*-
"""
Spyder Editor

pyliparam.py
PyLiCloud Parametric Studies
"""
import os # for handling directories and filenames
import pandas as pd # for reading point cloud csv file and processing it
import numpy as np
import matplotlib.pyplot as plt # plotting
import matplotlib.colors as mcolors
from matplotlib.backends.backend_pdf import PdfPages
from findrows import checkfirstmeters,locate_change_row # functions for finding rows
from scattercloud import *
from compag_scatter_check import *
from pyliparam import *

fileprefix="20190731_MasPiquet_Aglae_Lidar_plant_R_rows"
filesuffix=".csv"
#path_to_file_directory="D:\\190731_Aglae_PV_seuils_v2"
#path_to_work_directory=path_to_file_directory
#os.chdir(path_to_work_directory)
# filename = path_to_file_directory + "\\"+fileprefix+filesuffix
# pdffile = path_to_file_directory + "\\"+fileprefix+"_check"+".pdf"
# tablefile = path_to_file_directory + "\\"+fileprefix+"_blocks"+".csv"
# A=pd.read_csv(filename)
A=pd.read_csv("20190731_MasPiquet_Aglae_Lidar_plant_R_rows.csv")
# file mixes integers written as floats, float and strings
# should have been written better

w=windowXY()
# apply threshold for expected setting of sprayer: median of cordveg
# rounded value of median is 0.36
miniHeight=0.36
# rounded value for 60% above top trelissing wire each 5 m, 60th centile of these
# for all the field
maxiHeight=1.52
qs="Y>="+str(miniHeight)+" and Y<= "+str(maxiHeight)
A=A.query(qs)
A=A.astype({'scan_index': 'int32','row':'int32'},copy=False) # would not be necessary if no mistake in file or dataframe


step_X = 0.1 # resolution of a block along X
# division = 20000 ??
# we have 3 compartments in height: B(as), M(ilieu), H(aut) in French
# L(ow), M(iddle) and H(igh) in English
LtoM_threshold = 0.7
MtoH_threshold = 1.15
# trous_milieu = 30
# trous_haut = 15
# tailleBlocMin = 0.5
sprayer_speed = 1.4 # m per second

# create a dictionary with lists
# this dictionary will be converted to panda data frame for writing it to a file
blocks={'row':[],'rowminX':[],'rowmaxX':[],'minX':[],'maxX': [],'Lcounts':[]
        ,'Mcounts':[],'Hcounts':[],'Tcounts':[] } #XX added RIM

# LSDC, MSDC and HSDC stand respectively for Low, Middle and High Section Density Class
# these 'LSDC':[],'MSDC':[],'HSDC':[] cannot be included yet as will be calculated later

anglevalues=pd.unique(A['theta'])
rowvalues=pd.unique(A['row'])
rowvalues=rowvalues.astype(int) # for file with badly written columns
nbrows=len(rowvalues)
#for row in range(0,nbrows):
for row in rowvalues:
    B=A.query("row>"+str(row-1)+" and "+"row<="+str(row))
    # souci avec X min de row 1 TerresBlanches qui est de 195 quand Xmin total est de zero environ
    # ou alors OK c'est rang 2
    Xmin=min(B['X'])
    Xmax=max(B['X'])
    X=Xmin
    while X <= Xmax-step_X:
        w.xmin=X
        w.xmax=X+step_X
        w.ymin=miniHeight
        w.ymax=maxiHeight
        # store row and min and max of each row
        blocks['row'].append(row)
        blocks['rowminX'].append(Xmin)
        blocks['rowmaxX'].append(Xmax)
        # cut the window
        W=B.query("X>="+str(w.xmin)+" and " + "X<"+str(w.xmax))
        # store X range
        blocks['minX'].append(X)
        blocks['maxX'].append(X+step_X)
        # get the data for each height section
        WL=W.query("Y<"+str(LtoM_threshold))
        WM=W.query("Y>="+str(LtoM_threshold)+" and Y< "+str(MtoH_threshold))
        WH=W.query("Y>="+str(MtoH_threshold))

        blocks['Lcounts'].append(len(WL))
        blocks['Mcounts'].append(len(WM))
        blocks['Hcounts'].append(len(WH))
        blocks['Tcounts'].append(len(W)) #XX added Rim

        X=X+step_X

blocks_table=pd.DataFrame.from_dict(blocks) # default index is columns
# this dataframe has good dtypes
# now that we have counts, we can calculate medians for each height section
# medians=blocks_table.median(axis=0) # median along index for each column
# let's calculate only what we need:
medianL=blocks_table['Lcounts'].median()
medianM=blocks_table['Mcounts'].median()
medianH=blocks_table['Hcounts'].median()
medianT=blocks_table['Tcounts'].median() #XX added Rim
print("medianL ", medianL)
print("medianM ", medianM)
print("medianH ", medianH)
print("medianT ", medianT)
Lcounts=blocks_table['Lcounts'].values
Mcounts=blocks_table['Mcounts'].values
Hcounts=blocks_table['Hcounts'].values
Tcounts=blocks_table['Tcounts'].values #XX added Rim
# create an array that has code 1 for low density and code 2 for high density
# high density is above median for whole field and for this height section
Lcode=np.ones(len(Lcounts),dtype=int) # mandatory to state dtype to avoid array of floats
Lcode[Lcounts>=medianL]=2
Mcode=np.ones(len(Mcounts),dtype=int)
Mcode[Mcounts>=medianM]=2
Hcode=np.ones(len(Hcounts),dtype=int)
Hcode[Hcounts>=medianH]=2
Tcode=np.ones(len(Tcounts),dtype=int) #XX added Rim
Tcode[Tcounts>=medianT]=2 #XX added Rim

# now we need to set up a filter that puts 0 when no vegetation
# threshold is 10% of median for L and M sections and is 5 for High section
Lcode[Lcounts<0.1*medianL]=0 # seuil etudie confirme
Mcode[Mcounts<0.34*medianM]=0 # seuil etudie modifie
Hcode[Hcounts<=5]=0 # seuil passe de strict a <=
#XX added Rim pas de 0 pour T

# now make these arrays a dataframe
codes={'LSDC':Lcode,'MSDC':Mcode,'HSDC':Hcode, 'TSDC':Tcode} #XX added Rim

codes_table=pd.DataFrame.from_dict(codes) # default index is columns
# provided the numpy arrays have proper type, the columns of dataframe also have

# now concatenate/merge blocks_table and codes_table
# table=pd.concat([blocks_table,codes_table],axis=1)
# # NB: line indexes of both dataframes should start at 0 and be identical
# table.to_csv(tablefile,index=False) # ! codes written as integers if dtypes are correct
#
# winsize=5 # in meters
# with PdfPages(pdffile) as pdf:
#     for row in rowvalues:
#         B=A.query("row>"+str(row-1)+" and "+"row<="+str(row))
#         # souci avec X min de row 1 TerresBlanches qui est de 195 quand Xmin total est de zero environ
#         # ou alors OK c'est rang 2
#         Xmin=min(B['X'])
#         Xmax=max(B['X'])
#         X=Xmin
#         while X <= Xmax-winsize:
#             w.xmin=X
#             w.xmax=X+winsize
#             w.ymin=miniHeight
#             w.ymax=maxiHeight
#             fig,W=window_2Dscattercodeplot(B,table,LtoM_threshold,MtoH_threshold,w.xmin,w.xmax)
#             pdf.savefig(fig)
#             X=X+winsize
