# -*- coding: utf-8 -*-
"""
@author: rim.saddem
"""
import os.path
import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import scipy.signal
import scipy.io

#Fonction Cbest en fonction de total, haut, bas, milieu avec MB sélectionnée 1, MC sélectionnée 2 et MH sélectionnée 3
def CommandeCbest (total, haut, milieu, bas) :
    if milieu == 0:
        return 0
    if total == 1: # on a beoin d'une seule main : MB ou MC ou MH
        if haut==0 and milieu==1 and bas ==0:
            return 1 #MB
        if haut==0 and milieu==1 and bas ==1:
           return 1 #MB
        if haut==0 and milieu==1 and bas ==2:
           return 1 #MB
        if haut==0 and milieu==2 and bas ==1:
           return 1 #MB
        if haut==0 and milieu==2 and bas ==2:
           return 3 #MB + MC
        if haut==1 and milieu==1 and bas ==0:
           return 4 #MH
        if haut==1 and milieu==1 and bas ==1:
           return 2 #MC
        if haut==1 and milieu==1 and bas ==2: #to be verified
           return 3 #MB + MC
        if haut==1 and milieu==2 and bas ==0: #ADDED x
           return 2 #MC 
        if haut==1 and milieu==2 and bas ==1:
           return 2 #MC        
        if haut==1 and milieu==2 and bas ==2:
           return 3 #MB + MC
        if haut==2 and milieu==1 and bas ==0: #ADDED x
           return 4 #MH
        if haut==2 and milieu==1 and bas ==1:
           return 2 #MC
        if haut==2 and milieu==1 and bas ==2:
           return 5 #MB + MH
        if haut==2 and milieu==2 and bas ==0:#ADDED x
           return 6 #MC + MH
        if haut==2 and milieu==2 and bas ==1:
           return 2 #MC
        return -1
                                                                     
    else :                             #sinon on regarde la végétation
        if total == 2 :

            if haut==0 and milieu==1 and bas ==2:
               return 1 #MB
            if haut==0 and milieu==2 and bas ==1:
               return 3 #MB + MC
            if haut==0 and milieu==2 and bas ==2:
               return 3 #MB + MC
            if haut==1 and milieu==1 and bas ==2:
               return 3 #MB + MC
            if haut==1 and milieu==2 and bas ==0: #ADDED
               return 6 #MC + MH
            if haut==1 and milieu==2 and bas ==1:
               return 5 #MB + MH
            if haut==1 and milieu==2 and bas ==2:
               return 3 #MB + MC
            if haut==2 and milieu==1 and bas ==0: #ADDED
               return 6 #MC + MH       
            if haut==2 and milieu==1 and bas ==1:
               return 6 #MC + MH
            if haut==2 and milieu==1 and bas ==2:
               return 5 #MB + MH
            if haut==2 and milieu==2 and bas ==0: #ADDED
               return 6 #MC + MH 
            if haut==2 and milieu==2 and bas ==1:
               return 6 #MC + MH      
            if haut==2 and milieu==2 and bas ==2:
               return 5 #MB + MH  
            return -1
    

def CommandeCalt (total, haut, milieu, bas) :
    if milieu == 0:
        return 0
    if total == 1: # on a beoin d'une seule main : MB ou MC ou MH
        if haut==0 and milieu==1 and bas ==0:
           return 4 #MH
        if haut==0 and milieu==1 and bas ==1:
           return 2 #MC
        if haut==0 and milieu==1 and bas ==2:
           return 1 #MB
        if haut==0 and milieu==2 and bas ==1:
           return 2 #MC
        if haut==0 and milieu==2 and bas ==2:
           return 3 #MB + MC
        if haut==1 and milieu==1 and bas ==0:
           return 2 #MC
        if haut==1 and milieu==1 and bas ==1:
           return 2 #MC
        if haut==1 and milieu==1 and bas ==2:
           return 2 #MC
        if haut==1 and milieu==2 and bas ==0: #ADDED
           return 2 #MC
        if haut==1 and milieu==2 and bas ==1:
           return 5 #MB + MH     
        if haut==1 and milieu==2 and bas ==2:
           return 3 #MB + MC   
        if haut==2 and milieu==1 and bas ==0: #ADDED
           return 6 #MH + MC 
        if haut==2 and milieu==1 and bas ==1:
           return 6 #MC + MH 
        if haut==2 and milieu==1 and bas ==2:
           return 3 #MB + MC
        if haut==2 and milieu==2 and bas ==0:#ADDED
           return 6 #MC + MH
        if haut==2 and milieu==2 and bas ==1:
           return 6 #MC + MH 
        return -1                                                                        
    else :                             #sinon on regarde la végétation
        if total == 2 :

            if haut==0 and milieu==1 and bas ==2:
               return 3 #MB + MC
            if haut==0 and milieu==2 and bas ==1:
               return 5 #MB + MH
            if haut==0 and milieu==2 and bas ==2:    
               return 5 #MB + MH
            if haut==1 and milieu==1 and bas ==2:         
               return 3 #MB + MC
            if haut==1 and milieu==2 and bas ==0: #ADDED
               return 6 #MC + MH
            if haut==1 and milieu==2 and bas ==1:           
               return 5 #MB + MH
            if haut==1 and milieu==2 and bas ==2:              
               return 3 #MB + MC  
            if haut==2 and milieu==1 and bas ==0: #ADDED
               return 5 #MB + MH       
            if haut==2 and milieu==1 and bas ==1:             
               return 6 #MC + MH 
            if haut==2 and milieu==1 and bas ==2:              
               return 3 #MB + MC
            if haut==2 and milieu==2 and bas ==0:#ADDED
                return 5 #MC + MH
            if haut==2 and milieu==2 and bas ==1:            
               return 6 #MC + MH       
            if haut==2 and milieu==2 and bas ==2:
               return 5 #MB + MH 
            return -1
#RAF1 resolution 10 cm vegState(X, i -1) = vegState(X, i+1) -> vegState(X, i) = vegState(X, i+1)
# 
def RAF1(porosity_bas, porosity_milieu, porosity_haut, porosity_total ):
    i=1
    while (i< len(porosity_bas)-1):
        if (porosity_bas[i-1] == porosity_bas[i+1]):
            porosity_bas[i] = porosity_bas[i+1]
            i = i + 2
        else :    
            i = i + 1
    
    i=1
    while (i< len(porosity_milieu)-1):
        if (porosity_milieu[i-1] == porosity_milieu[i+1]):
            porosity_milieu[i] = porosity_milieu[i+1]
            i = i + 2
        else :    
            i = i + 1
    
    i=1
    while (i< len(porosity_haut)-1):
        if (porosity_haut[i-1] == porosity_haut[i+1]):
            porosity_haut[i] = porosity_haut[i+1]
            i = i + 2
        else :    
            i = i + 1
            
    i=1
    while (i< len(porosity_total)-1):
        if (porosity_total[i-1] == porosity_total[i+1]):
            porosity_total[i] = porosity_total[i+1]
            i = i + 2
        else :    
            i = i + 1

#new_version
    i=0
    while (i< len(porosity_total)):
        if (porosity_haut[i] + porosity_milieu[i] + porosity_bas[i]) >= 5:
            porosity_total[i] = 2
        if (porosity_haut[i] + porosity_milieu[i] + porosity_bas[i]) <= 3:
            porosity_total[i] = 1
        i = i + 1


#regarder la distribution des états de végétation                                      
def VisualisationVegStateRow(row, porosity_bas_1, porosity_milieu_1, porosity_haut_1, porosity_total_1):
    j=0
    liste = list()
    while (j<len(porosity_total_1)):
        element = "{} {} {} {} ".format(str (porosity_total_1[j]), str (porosity_haut_1[j]),str (porosity_milieu_1[j]),  str (porosity_bas_1[j]))
        if element not in liste:
            liste.append(element)            
        j=j+1      
    print("row = ", row)
    liste.sort()    
    print(liste)
 
    
def computeCbestCalt(Cbest, Calt, Taille, porosity_bas, porosity_milieu, porosity_haut, porosity_total,notFound):  

    j=0
    while (j<len(porosity_total)):
    
        Cbest.append(CommandeCbest(porosity_total[j],porosity_haut[j],porosity_milieu[j], porosity_bas[j] )) 
        Calt.append(CommandeCalt(porosity_total[j],porosity_haut[j],porosity_milieu[j], porosity_bas[j] ))
        Taille.append(resolution_x)
        
        if Cbest[j] == -1 or Calt[j] == -1: # on a beoin d'une seule main : MB ou MC ou MH
            element = "{} {} {} {} ".format(str (porosity_total[j]),str (porosity_haut[j]),str (porosity_milieu[j]),  str (porosity_bas[j]))
            if element not in notFound:
                notFound.append(element)
        j = j + 1

#RAF2 : resolution 10 cm (C_{best}[i - 1] = C_{best}[i + 1]) ->  C_{best}[i] = C_{best}[i + 1]
def RAF2(row, Cbest, Calt, Taille):
    i=1
    while (i< len(Cbest)-1):
        if (Cbest[i-1] == Cbest[i+1]) :
            Cbest[i] = Cbest[i+1]
            i = i + 2
        else :    
            i = i + 1
    
    i=1
    while (i< len(Calt)-1):
        if (Calt[i-1] == Calt[i+1]) :
            Calt[i] = Calt[i+1]
            i = i + 2
        else :    
            i = i + 1  
            
    print("RAF2 row ", row, " verif nb bloc ",len(Taille), "somme taille",np.sum(Taille[0:len(Taille)]), "\n")

#RAF3 AGREGATION DE CBEST = 0:  C_{best} [i-1] = 0 && C_{best} [i + 1] = 0 && C_{best} [i] \in \{LH, HH, CH \} -> merge(i, i  -1) && merge(i, i + 1 )
      
def RAF3(row, Cbest, Calt, tailleBloc, Xmin, Xmax):      
    i=0   
    print ("In RAF3 ", len(Cbest), " len max X ", len(Xmax))
    while ( i < len(Cbest)-2):
        if Cbest[i]==0 and Cbest[i+2]==0 and Cbest [i+1] <= 4 and  Cbest [i+1] != 3:
            
            tailleBloc[i] = tailleBloc[i] + tailleBloc[i+1]
            tailleBloc[i] = tailleBloc[i] + tailleBloc[i+2]
            Xmax[i] = Xmax[i+2]
            del(tailleBloc[i+1]) #if 0 et 2 : 1
            del(tailleBloc[i+1]) # 2
            del(Cbest[i+1])
            del(Cbest[i+1])
            del(Calt[i+1])
            del(Calt[i+1])
            del(Xmax[i+1])
            del(Xmax[i+1])
            del(Xmin[i+1])
            del(Xmin[i+1])
        else:
            i = i+ 1
    print("row", row, "verif RAF3",np.sum(tailleBloc[0:len(tailleBloc)]), "\n")
    print("le nombre de trou apres appliquer RAF3 ", Cbest.count(0))
    
#Afficher liste des trous      
def AfficheTrou (row, Cbest, Taille,minX, maxX) :   
    i = 0
    while ( i < len(Cbest)):
        if Cbest[i]==0 :
            print("row " , row, " trou numero ",i, "de taille", Taille[i], "de position min ", minX[i], " et position  max ", maxX[i])
            
        i = i+ 1

#affiche max taille
def AfficheMaxTaille (row, Taille ):    
    print ("row ", row, " max taille ", max(Taille))   

    
#aggregate same command
def RAFAgregate (row, Cbest, Calt, Taille, minX, maxX):    
    i=0
    while ( i < len(Cbest)-1):
        if Cbest[i]==Cbest[i+1] and Calt[i]==Calt[i+1] :
            Taille[i] = Taille[i] + Taille[i+1] 
            maxX[i] = maxX[i+1]     
            del(Taille[i+1]) #if 0 et 2 : 1      
            del(Cbest[i+1])  
            del(Calt[i+1])
            del(maxX[i+1])  
            del(minX[i+1])
        else:
            i = i+ 1
    
    print("row ", row, " RAFAgregateSameComand verif nb bloc ",len(Taille), "somme taille ",np.sum(Taille[0:len(Taille)]), "\n")

#RAF4: (sizeBlock[i] < resolution)  && (C_{best} [max(i-1,i+1)] != 0) -> merge(i,max(i-1,i+1)), sizeBlock[i] < resolution && C_{best} [max(i-1,i+1)] = 0 -> merge(i,min(i-1,i+1))
def RAF4(row, Cbest, Calt, Taille, minX, maxX ): 
    while (min(Taille[1:len(Taille)-1]) < tailleBlocMin):
        i = 1
        while (i < len(Taille)-1):
            if Taille[i] < tailleBlocMin:
                if Taille[i-1]>= Taille[i+1]:
                    if Taille[i-1]>= Taille[i] :
                        if Cbest[i-1] != 0 : #1
                            Taille[i-1] = Taille[i] + Taille[i-1]
                            maxX[i-1] = maxX[i]
                            del(Taille[i]) 
                            del(Cbest[i])
                            del(Calt[i])  
                            del(maxX[i])  
                            del(minX[i])                     
                        else:
                            if Taille[i+1]>= Taille[i] or Cbest[i]==0: #2
                                Taille[i+1] = Taille[i] + Taille[i+1]
                                minX[i+1] = minX[i]
                                del(Taille[i]) 
                                del(Cbest[i])
                                del(Calt[i])
                                del(maxX[i])  
                                del(minX[i]) 
                            else:
                                Taille[i] = Taille[i] + Taille[i+1] #3
                                maxX[i] = maxX[i+1]
                                del(Taille[i+1]) 
                                del(Cbest[i+1])
                                del(Calt[i+1])   
                                del(maxX[i+1])  
                                del(minX[i+1])                          
                    else: #Taille[i-1]< Taille[i]  #not considered in any RAF
                        if Cbest[i] != 0 : #4
                            Taille[i] = Taille[i] + Taille[i-1]
                            minX[i] = minX[i-1]
                            del(Taille[i-1]) 
                            del(Cbest[i-1])
                            del(Calt[i-1])
                            del(maxX[i-1])  
                            del(minX[i-1])
                            
                        else:
                            Taille[i-1] = Taille[i] + Taille[i-1] #5
                            maxX[i-1] = maxX[i]
                            del(Taille[i]) 
                            del(Cbest[i])
                            del(Calt[i]) 
                            del(maxX[i])  
                            del(minX[i]) 
                else: #T[i-1]<T[i+1]
                    if Taille[i+1]>= Taille[i] :
                        if Cbest[i+1] != 0 : #6
                            Taille[i+1] = Taille[i] + Taille[i+1]
                            minX[i+1] = minX[i]
                            del(Taille[i]) 
                            del(Cbest[i])
                            del(Calt[i])
                            del(maxX[i])  
                            del(minX[i]) 
                        else:
                            if Taille[i-1]>= Taille[i] or Cbest[i]==0: #7
                                Taille[i-1] = Taille[i] + Taille[i-1]
                                maxX[i-1] = maxX[i]
                                del(Taille[i]) 
                                del(Cbest[i])
                                del(Calt[i])
                                del(maxX[i])  
                                del(minX[i]) 
                            else:
                                Taille[i] = Taille[i] + Taille[i-1] #8
                                minX[i] = minX[i-1]
                                del(Taille[i-1]) 
                                del(Cbest[i-1])
                                del(Calt[i-1])
                                del(maxX[i-1])  
                                del(minX[i-1])
                    else: #Taille[i+1]< Taille[i]
                        if Cbest[i] != 0 :
                            Taille[i] = Taille[i] + Taille[i+1] #9
                            maxX[i] = maxX[i+1]
                            del(Taille[i+1]) 
                            del(Cbest[i+1])
                            del(Calt[i+1])
                            del(maxX[i+1])  
                            del(minX[i+1])  
                        else:
                            Taille[i+1] = Taille[i] + Taille[i+1] #10
                            minX[i+1] = minX[i]
                            del(Taille[i]) 
                            del(Cbest[i])
                            del(Calt[i]) 
                            del(maxX[i])  
                            del(minX[i])             
                i = i + 2               
            else:
                i = i + 1            
                        
    #traiter cas 0 
    if Taille[0] < tailleBlocMin:
        Taille[1] = Taille[1] + Taille[0]
        minX[1] = minX[0]
        del(Taille[0]) 
        del(Cbest[0])
        del(Calt[0])
        del(maxX[0])  
        del(minX[0])
    
    #traiter cas len(Cbest)
    i = len(Cbest)-1
    if Taille[i] < tailleBlocMin:
        Taille[i-1] = Taille[i-1] + Taille[i]
        maxX[i-1] = maxX[i]
        del(Taille[i]) 
        del(Cbest[i])
        del(Calt[i])
        del(maxX[i])  
        del(minX[i])
    
    print("row ", row, "RAF4 verif nb bloc ",len(Taille), "somme taille ",np.sum(Taille[0:len(Taille)]), "\n")
    print("le nombre de trou apres appliquer RAF4 ", Cbest.count(0))
    
#convert numpy to array
def convert(minX,Xmin):
    i=0
    while (i < len(minX)):
        Xmin.append(minX[i])
        i = i + 1
      
       
#convertir en time
def convertTime(tempo_bloc):
    i=0
    while (i < len(tempo_bloc)):
        tempo_bloc[i] = int (round (tempo_bloc[i]  / vitesseRobot , 1) * 10)
        i = i + 1  
                
resolution_x = 0.1 
medianL = 55.0
medianM = 134.0
medianH = 42.0
medianT = 241.0

trous_bas = 0.1*medianL
trous_milieu = 0.34*medianM 
trous_haut = 5

tailleBlocMin = 0.5
vitesseRobot = 1.4 #m par seconde 

df = pd.read_excel (r'Aglae_RS.xlsx')
#print (df)
row = df['row'].values # returns numpy.ndarray
porosity_total = df['TSDC'].values 
porosity_haut = df['HSDC'].values 
porosity_milieu = df['MSDC'].values 
porosity_bas = df['LSDC'].values
nb_total = df['Tcounts'].values 
nb_haut = df['Hcounts'].values 
nb_milieu = df['Mcounts'].values 
nb_bas = df['Lcounts'].values
minX = df['minX'].values
maxX = df['maxX'].values



row_1 = row[0:np.sum(row == 1) ]
min_X_row_1 = row[0:np.sum(row == 1)]
porosity_total_1 = porosity_total[0:np.sum(row == 1) ]
porosity_haut_1 = porosity_haut[0:np.sum(row == 1) ]
porosity_milieu_1 = porosity_milieu[0:np.sum(row == 1) ]
porosity_bas_1 = porosity_bas[0:np.sum(row == 1) ]
nb_total_1 = nb_total[0:np.sum(row == 1) ]
nb_haut_1 = nb_haut[0:np.sum(row == 1) ]
nb_milieu_1 = nb_milieu[0:np.sum(row == 1) ]
nb_bas_1 = nb_bas[0:np.sum(row == 1) ]
minX_1 = minX[0:np.sum(row == 1) ]
maxX_1 = maxX[0:np.sum(row == 1) ]

row_2 = row[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ]
porosity_total_2 = porosity_total[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ] 
porosity_haut_2 = porosity_haut[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ]
porosity_milieu_2 = porosity_milieu[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ]
porosity_bas_2 = porosity_bas[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2)]
nb_total_2 = nb_total[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ] 
nb_haut_2 = nb_haut[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ]
nb_milieu_2 = nb_milieu[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2) ]
nb_bas_2 = nb_bas[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2)]
minX_2 = minX[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2)]
maxX_2 = maxX[np.sum(row == 1):np.sum(row == 1) + np.sum(row == 2)]

row_3 = row[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
porosity_total_3 = porosity_total[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
porosity_haut_3 = porosity_haut[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
porosity_milieu_3 = porosity_milieu[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
porosity_bas_3 = porosity_bas[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
nb_total_3 = nb_total[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
nb_haut_3 = nb_haut[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
nb_milieu_3 = nb_milieu[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
nb_bas_3 = nb_bas[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
minX_3 = minX[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]
maxX_3 = maxX[np.sum(row == 1) + np.sum(row == 2): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)]


row_4 = row[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
porosity_total_4 = porosity_total[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
porosity_haut_4 = porosity_haut[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
porosity_milieu_4 = porosity_milieu[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
porosity_bas_4 = porosity_bas[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
nb_total_4 = nb_total[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
nb_haut_4 = nb_haut[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
nb_milieu_4 = nb_milieu[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
nb_bas_4 = nb_bas[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
minX_4 = minX[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]
maxX_4 = maxX[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)]


row_5 = row[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
porosity_total_5 = porosity_total[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
porosity_haut_5 = porosity_haut[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
porosity_milieu_5 = porosity_milieu[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
porosity_bas_5 = porosity_bas[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
nb_total_5 = nb_total[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
nb_haut_5 = nb_haut[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
nb_milieu_5 = nb_milieu[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
nb_bas_5 = nb_bas[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
minX_5 = minX[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]
maxX_5 = maxX[np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3)+  np.sum(row == 4): np.sum(row == 1) + np.sum(row == 2)+  np.sum(row == 3) + np.sum(row == 4)+ np.sum(row == 5)]


notFound = list()
trous_1 = list() # la liste des trous
choice_1 = np.zeros(len(porosity_bas_1)) #premier choix proche de l'optimum

trous_2 = list() # la liste des trous
choice_2 = np.zeros(len(porosity_bas_2)) #premier choix proche de l'optimum

trous_3 = list() # la liste des trous
choice_3 = np.zeros(len(porosity_bas_3)) #premier choix proche de l'optimum

trous_4 = list() # la liste des trous
choice_4 = np.zeros(len(porosity_bas_4)) #premier choix proche de l'optimum

trous_5 = list() # la liste des trous
choice_5 = np.zeros(len(porosity_bas_5)) #premier choix proche de l'optimum

tempo_bloc_1 = list()
Cbest_1 = list()
Calt_1 = list()
Xmin_1 = list()
Xmax_1 = list()

tempo_bloc_2 = list()
Cbest_2 = list()
Calt_2 = list()
Xmin_2 = list()
Xmax_2 = list()

tempo_bloc_3 = list()
Cbest_3 = list()
Calt_3 = list()
Xmin_3 = list()
Xmax_3 = list()

tempo_bloc_4 = list()
Cbest_4 = list()
Calt_4 = list()
Xmin_4 = list()
Xmax_4 = list()

tempo_bloc_5 = list()
Cbest_5 = list()
Calt_5 = list()
Xmin_5 = list()
Xmax_5 = list()

#convert numpy to array
convert(minX_1,Xmin_1)
convert(minX_2,Xmin_2)
convert(minX_3,Xmin_3)
convert(minX_4,Xmin_4)
convert(minX_5,Xmin_5)

convert(maxX_1,Xmax_1)
convert(maxX_2,Xmax_2)
convert(maxX_3,Xmax_3)
convert(maxX_4,Xmax_4)
convert(maxX_5,Xmax_5)
#apply RAF1 to all rows    
RAF1(porosity_bas_1, porosity_milieu_1, porosity_haut_1, porosity_total_1)
RAF1(porosity_bas_2, porosity_milieu_2, porosity_haut_2, porosity_total_2)
RAF1(porosity_bas_3, porosity_milieu_3, porosity_haut_3, porosity_total_3)
RAF1(porosity_bas_4, porosity_milieu_4, porosity_haut_4, porosity_total_4)
RAF1(porosity_bas_5, porosity_milieu_5, porosity_haut_5, porosity_total_5)

VisualisationVegStateRow(1, porosity_bas_1, porosity_milieu_1, porosity_haut_1, porosity_total_1)
VisualisationVegStateRow(2, porosity_bas_2, porosity_milieu_2, porosity_haut_2, porosity_total_2)
VisualisationVegStateRow(3, porosity_bas_3, porosity_milieu_3, porosity_haut_3, porosity_total_3)
VisualisationVegStateRow(4, porosity_bas_4, porosity_milieu_4, porosity_haut_4, porosity_total_4)
VisualisationVegStateRow(5, porosity_bas_5, porosity_milieu_5, porosity_haut_5, porosity_total_5) 

#Définir les commandes Cbest et Calt  
computeCbestCalt(Cbest_1, Calt_1, tempo_bloc_1,porosity_bas_1, porosity_milieu_1, porosity_haut_1, porosity_total_1, notFound)
computeCbestCalt(Cbest_2, Calt_2, tempo_bloc_2,porosity_bas_2, porosity_milieu_2, porosity_haut_2, porosity_total_2, notFound)
computeCbestCalt(Cbest_3, Calt_3, tempo_bloc_3,porosity_bas_3, porosity_milieu_3, porosity_haut_3, porosity_total_3, notFound)
computeCbestCalt(Cbest_4, Calt_4, tempo_bloc_4,porosity_bas_4, porosity_milieu_4, porosity_haut_4, porosity_total_4, notFound)
computeCbestCalt(Cbest_5, Calt_5, tempo_bloc_5,porosity_bas_5, porosity_milieu_5, porosity_haut_5, porosity_total_5, notFound)
notFound.sort()
print ("not found list = ",notFound)

#apply RAF2
#RAF2 : resolution 10 cm (C_{best}[i - 1] = C_{best}[i + 1]) ->  C_{best}[i] = C_{best}[i + 1]

RAF2(1, Cbest_1, Calt_1, tempo_bloc_1)
RAF2(2, Cbest_2, Calt_2, tempo_bloc_2)
RAF2(3, Cbest_3, Calt_3, tempo_bloc_3)
RAF2(4, Cbest_4, Calt_4, tempo_bloc_4)
RAF2(5, Cbest_5, Calt_5, tempo_bloc_5)


#apply RAF3
#RAF3 AGREGATION DE CBEST = 0:  C_{best} [i-1] = 0 && C_{best} [i + 1] = 0 && C_{best} [i] \in \{LH, HH, CH \} -> merge(i, i  -1) && merge(i, i + 1 )

RAF3(1, Cbest_1, Calt_1, tempo_bloc_1, Xmin_1, Xmax_1)
RAF3(2, Cbest_2, Calt_2, tempo_bloc_2, Xmin_2, Xmax_2)
RAF3(3, Cbest_3, Calt_3, tempo_bloc_3, Xmin_3, Xmax_3)
RAF3(4, Cbest_4, Calt_4, tempo_bloc_4, Xmin_4, Xmax_4)
RAF3(5, Cbest_5, Calt_5, tempo_bloc_5, Xmin_5, Xmax_5)

#Afficher liste des trous        
AfficheTrou(1, Cbest_1, tempo_bloc_1, Xmin_1,Xmax_1)
AfficheTrou(2, Cbest_2, tempo_bloc_2, Xmin_2,Xmax_2)
AfficheTrou(3, Cbest_3, tempo_bloc_3, Xmin_3,Xmax_3)
AfficheTrou(4, Cbest_4, tempo_bloc_4, Xmin_4,Xmax_4)
AfficheTrou(5, Cbest_5, tempo_bloc_5, Xmin_5,Xmax_5)
    
#aggregate same command
RAFAgregate(1, Cbest_1, Calt_1, tempo_bloc_1, Xmin_1,Xmax_1)
RAFAgregate(2, Cbest_2, Calt_2, tempo_bloc_2, Xmin_2,Xmax_2)
RAFAgregate(3, Cbest_3, Calt_3, tempo_bloc_3, Xmin_3,Xmax_3)
RAFAgregate(4, Cbest_4, Calt_4, tempo_bloc_4, Xmin_4,Xmax_4)
RAFAgregate(5, Cbest_5, Calt_5, tempo_bloc_5, Xmin_5,Xmax_5)
   
   #Affiche Max Taille blocs 
AfficheMaxTaille(1,tempo_bloc_1)
AfficheMaxTaille(2,tempo_bloc_2)
AfficheMaxTaille(3,tempo_bloc_3)
AfficheMaxTaille(4,tempo_bloc_4)
AfficheMaxTaille(5,tempo_bloc_5)

#afficher liste des trous        
AfficheTrou(1, Cbest_1, tempo_bloc_1, Xmin_1,Xmax_1)
AfficheTrou(2, Cbest_2, tempo_bloc_2, Xmin_2,Xmax_2)
AfficheTrou(3, Cbest_3, tempo_bloc_3, Xmin_3,Xmax_3)
AfficheTrou(4, Cbest_4, tempo_bloc_4, Xmin_4,Xmax_4)
AfficheTrou(5, Cbest_5, tempo_bloc_5, Xmin_5,Xmax_5)

#RAF4: (sizeBlock[i] < resolution)  && (C_{best} [max(i-1,i+1)] != 0) -> merge(i,max(i-1,i+1)), sizeBlock[i] < resolution && C_{best} [max(i-1,i+1)] = 0 -> merge(i,min(i-1,i+1)) 
# Version Oliver et Rim pour RAF4
#close to RAF4 of Rim Aglae
RAF4(1, Cbest_1, Calt_1, tempo_bloc_1, Xmin_1,Xmax_1)
RAF4(2, Cbest_2, Calt_2, tempo_bloc_2, Xmin_2,Xmax_2)
RAF4(3, Cbest_3, Calt_3, tempo_bloc_3, Xmin_3,Xmax_3)
RAF4(4, Cbest_4, Calt_4, tempo_bloc_4, Xmin_4,Xmax_4)
RAF4(5, Cbest_5, Calt_5, tempo_bloc_5, Xmin_5,Xmax_5)

#Affiche Max Taille blocs 
AfficheMaxTaille(1,tempo_bloc_1)
AfficheMaxTaille(2,tempo_bloc_2)
AfficheMaxTaille(3,tempo_bloc_3)
AfficheMaxTaille(4,tempo_bloc_4)
AfficheMaxTaille(5,tempo_bloc_5)

#convertir longueur en temps      
convertTime(tempo_bloc_1)
convertTime(tempo_bloc_2)
convertTime(tempo_bloc_3)
convertTime(tempo_bloc_4)
convertTime(tempo_bloc_5)