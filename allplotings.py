#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:29:30 2019

@author: lakshmi
"""

import datetime
a=datetime.datetime.now()
print(a)
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

def addNoise(m, maxnoise):    
    for mm in range(maxnoise):
        	for ll in range(m.shape[0]):
        		ss = np.random.uniform(0,m.shape[1]-1)
        		tt = np.random.uniform(0,1)
        		if tt>0.5:
        			m[ll][int(ss)]=1
    return m

def plotspy(title,xval, eventnumber):  #xval is which matrix u want to plot
        print(title) 
        plt.spy(xval, origin = 'lower', aspect=3.3, markersize=5, color='black')  
        ax = plt.axes();
        ax.invert_yaxis()
        ax.xaxis.tick_bottom()
        ax.set_xticks(np.arange(0, 32, 5));
        ax.set_yticks(np.arange(0, 11, 2));
        plt.xlabel("Strips")#y_test value
        plt.ylabel("Layer")#y_pred value
        plt.savefig('x_stripevent_without_incl_eff_{}.png'.format(eventnumber))
        plt.show()
        
def allhitsm( mult,nLayers,nStrips,eta ): 
    maxnoise=3
    
    xmat=np.zeros((nLayers, nStrips)) 
    ymat=np.zeros((nLayers, nStrips)) 
    
    xmatn=np.zeros((nLayers, nStrips))
    ymatn=np.zeros((nLayers, nStrips))
    
    xnew =np.zeros((nLayers, nStrips))
    ynew =np.zeros((nLayers, nStrips))
    
#    xmaten=np.zeros((nLayers, nStrips))
#    ymaten=np.zeros((nLayers, nStrips))
    
    for j in np.arange(0, mult):
        print(j)
        xcount =0
        ycount =1
        
        while(xcount !=  ycount): #it will run until xount=ycount(xcount is number of hits in x_strip and ycount is number of hits in y_strips)        
            xm=np.random.uniform(-3, 3) 
            xc=np.random.uniform(-50, 50) 
            #print('xintecept',xc)                 
            ym=np.random.uniform(-3, 3) 
            #print('yslope',ym)
            yc=np.random.uniform(-50, 50)
            #print('xintecept',xc)
            if (xm!=0 and xc!=0 and ym!=0 and yc!=0):              
                dx=np.zeros((12, 32)) #creating the matrix for x_strip of size 12x32
                xindi=[] #creating the dummy list for rows of above matrix to store the indexes where the hit is
                xindj=[] #creating the dummy list for columns of above matrix to store the indexes where the hit is
                dy=np.zeros((12, 32)) 
                yindi=[]
                yindj=[]
                
                nlsX=np.random.uniform(0, nLayers)
                nlSX=int(nlsX)
#                print("layer no starts X", nlSX)
                nleX=np.random.uniform(0, nLayers)
                nlEX=int(nleX)
#                print("layer no ends X", nlEX) 
#                diffL = nlEX-nlSX
         
                nlsY=np.random.uniform(0, nLayers)
                nlSY=int(nlsY)
#                    print("layer no starts", nlSY)
                nleY=np.random.uniform(0, nLayers)
                nlEY=int(nleY)
    #                print("layer no ends", nlEY) 
#                diffLY = nlEY-nlSY   
        
#                if(diffL==4):
                for ix in np.arange(nlSX,nlEX): #loop for number of layers
                    xnStrips=xm*ix+xc   #st.mline formula for x_strip
                    #print(nStrips)
                    xp=int(round(xnStrips)) # roundoff the strip number 
                    #print(p)
                    if(xp>=0 and xp<32): #to avoide the values out of the strips bcz my strips range is from 0 to 32 not(-32 to 32)
                       dx[ix, xp]=1    #if above condition satifies then matrix dx it should fill that row with 1 & same will repeat for all 11 layers bcz it is loop   
                       xindi.append(ix)  #now appending the row values in the above created list xindi
                       xindj.append(xp) # appending the columns with xp
                xcount = np.count_nonzero(dx == 1) #to count how many 1's r there in the above created matrix (dx) 
                
                  #same  above procedure is repeated for y
                for iy in np.arange(nlSY, nlEY):
                    ynStrips=ym*iy+yc
                    #print(nStrips)
                    yp=round(ynStrips)
                    #print(p)
                    if(yp>=0 and yp<32):
                        dy[iy, int (yp)]=1
                        yindi.append(iy)
                        yindj.append(int (yp))
                ycount = np.count_nonzero(dy == 1)
                
                minlayer=8   
                if (ycount==xcount!=minlayer): #to avoid hits which r not equal to 4
#                    print("entering loop1")
                    xcount+=1             #xcount and ycount are made unequal bcz again it should go back to while loop
                                
                if (ycount==xcount): #writing the condition for number of hits in x should equal to hits in y                       
                    
                    xmat[xindi,xindj] = 1 #the above if condition satifies then only fill the original matrix by 1, but it should use the indixes dummy matrixes indi & indj
                    ymat[yindi,yindj] = 1 #same for ynmatrix 
                    xmatn[xindi,xindj] = 1
                    ymatn[yindi,yindj] = 1
                    xnew[xindi,xindj] = 1
                    ynew[yindi,yindj] = 1
############################################################################################                    
                    xindief=[] #creating the dummy list for rows of above matrix to store the indexes where the hit is
                    xindjef=[]
                    
                    yindief=[] #creating the dummy list for rows of above matrix to store the indexes where the hit is
                    yindjef=[]
                    
                    xmate= np.tile(xmat,1)
                    ymate= np.tile(ymat,1)
                    
                    xmaten= np.tile(xnew,1)  
                    ymaten= np.tile(ynew,1)
                    
                    for e in np.arange(0, xcount):
                        effx=np.random.uniform(0, 100)
#                        print("Efficiency x",effx)                        
#                        print("Xi = ",xindi)
#                        print("Yi = ",xindj)                   
#                        print('x indices', xindi[e], xindj[e])
                        xmate[xindi[e], xindj[e]]=effx
                        xmaten[xindi[e], xindj[e]]=effx
                        
                        if(effx>eta):
                            xmate[xindi[e], xindj[e]]=0  
                            xmaten[xindi[e], xindj[e]]=0
#                            ey[yindi[e], yindj[e]]=0 
                        else:
                            xmate[xindi[e], xindj[e]]=1
                            xmaten[xindi[e], xindj[e]]=1
                            
                            xindief.append(xindi[e])  #now appending the row values in the above created list xindi
                            xindjef.append(xindj[e])
                            
                        
                        effy=np.random.uniform(0, 100)
#                        print("Efficiency y",effy)
#                        print('y indices', yindi[e],yindj[e])
                        ymate[yindi[e], yindj[e]]=effy
                        ymaten[yindi[e], yindj[e]]=effy
                       
                        if(effy >eta ):
                            ymate[yindi[e], yindj[e]]=0
                            ymaten[yindi[e], yindj[e]]=0
                        else:
                            ymate[yindi[e], yindj[e]]=1
                            ymaten[yindi[e], yindj[e]]=1
                            
                            yindief.append(yindi[e])  #now appending the row values in the above created list xindi
                            yindjef.append(yindj[e])
                            
                        xnew= np.tile(xmaten,1)
                        ynew= np.tile(ymaten,1)   
                            
#######################################################################################                        
                    
                    xmats= np.tile(xmate,1)
                    ymats= np.tile(ymate,1) 
                    
                    for ii in range(len(xindief)):                        
#                        print(ii)                    
                        stp_mult_x = np.random.uniform(0,150)
                        
                        if(xindief[ii]!=0 and xindjef[ii]!=31):                            
                            
                            if (stp_mult_x<50):
                                #print('X ran L',stp_mult_x)
                                xmats[xindief[ii], xindjef[ii]+1]=1
                            elif (stp_mult_x>100):
#                                print('X ran R',stp_mult_x)
                                xmats[xindief[ii], xindjef[ii]-1]=1
                                
                    for jj in range(len(yindief)):                        
#                        print(jj)    
                        stp_mult_y = np.random.uniform(0,150)
                        
                        if(yindief[jj]!=0 and yindjef[jj]!=31):
                        
                            if (stp_mult_y<50):
#                                print('y ran L', stp_mult_y)
                                ymats[yindief[jj], yindjef[jj]+1]=1
                            elif (stp_mult_y>100):
#                                print('y ran R',stp_mult_y)
                                ymats[yindief[jj], yindjef[jj]-1]=1
                        
                    xmat= np.tile(xmats,1)
                    ymat= np.tile(ymats,1)
                   
#################################################################################################################### 
        xmatno = addNoise(xmats, maxnoise)
        ymatno = addNoise(ymats, maxnoise)

#        print("all hits in 4 layer one track")
#        print("xmatn")
#        plt.spy(xmatn, origin = 'lower', aspect=3.3, markersize=4, color='black')
#        plt.show()  
#        
#        print("xmate")
#        plt.spy(xmate, origin = 'lower', aspect=3.3, markersize=4, color='black')
#        plt.show()
#        
#        print("xmat")
#        plt.spy(xmat, origin = 'lower', aspect=3.3, markersize=4, color='black')
#        plt.show()        
#        
##        print("xmats")
##        plt.spy(xmats, origin = 'lower', aspect=3.3, markersize=4, color='black')
##        plt.show()
#        
#        print("xmatno")
#        plt.spy(xmatno, origin = 'lower', aspect=3.3, markersize=4, color='black')
#        plt.show()  
        
#        print("ymatno")
#        plt.spy(ymatno, origin = 'lower', aspect=3.3, markersize=4, color='black')
#        plt.show() 

        return(xmatn, xmate, xmat, xmatno, ymatn, ymate, ymat, ymatno)
        
xmatn, xmate, xmat, xmatno, ymatn, ymate, ymat, ymatno= allhitsm(1,12,32, 60)


def flattenmatrix(n, mult, nLayers, nStrips, min_layer, max_layer, eta):
    maxnoise=3
    out=np.zeros((n,773))    
    for i in np.arange(0,n):       
        
        xmatn, xmate, xmat, xmatno, ymatn, ymate, ymat, ymatno= allhitsm(1,12,32, 60)

#        plotspy('X original plot',xmat, i)
#        plotspy('y original plot',ymat, i)
        xmatn=np.tile(xmatn,1)
        ymatn=np.tile(ymatn,1)
        
        xnew =np.zeros((nLayers, nStrips))
        ynew =np.zeros((nLayers, nStrips))
        
        for j in np.arange(0, mult):
            xcount =0
            ycount =1  

            while(xcount !=  ycount): #it will run until xount=ycount(xcount is number of hits in x_strip and ycount is number of hits in y_strips)            
                xm=np.random.uniform(-3, 3) #maximum slope is(32/12=2.66) varied from +2.66to -2.66
    #                    print('xslope',xm)
                xc=np.random.uniform(-50, 50) 
                #print('xintecept',xc)                 
                ym=np.random.uniform(-3, 3) #maximum slope is(32/12=2.66) varied from +2.66to -2.66
                #print('yslope',ym)
                yc=np.random.uniform(-50, 50)
                #print('xintecept',xc)
                if (xm!=0 and xc!=0 and ym!=0 and yc!=0):
                    
                    dx=np.zeros((12, 32)) #creating the matrix for x_strip of size 12x32
                    xindi=[] #creating the dummy list for rows of above matrix to store the indexes where the hit is
                    xindj=[] #creating the dummy list for columns of above matrix to store the indexes where the hit is
                    dy=np.zeros((12, 32)) #creating the matrix for y_strip of size 12x32
                    yindi=[]
                    yindj=[]
                     
                    nlsX=np.random.uniform(0, nLayers)
                    nlSX=int(nlsX)
        #                print("layer no starts X", nlSX)
                    nleX=np.random.uniform(0, nLayers)
                    nlEX=int(nleX)
                    
                    nlsY=np.random.uniform(0, nLayers)
                    nlSY=int(nlsY)
        #                print("layer no starts", nlSY)
                    nleY=np.random.uniform(0, nLayers)
                    nlEY=int(nleY)
                    
                    
                    for ix in np.arange(nlSX,nlEX):
        #                        print("IX... ",ix)
                            xnStrips=xm*ix+xc   #st.mline formula for x_strip
                            #print(nStrips)
                            xp=int(round(xnStrips)) # roundoff the strip number 
                            #print(p)
                            if(xp>=0 and xp<32): #to avoide the values out of the strips bcz my strips range is from 0 to 32 not(-32 to 32)
                               dx[ix, xp]=1    #if above condition satifies then matrix dx it should fill that row with 1 & same will repeat for all 11 layers bcz it is loop   
                               xindi.append(ix)  #now appending the row values in the above created list xindi
                               xindj.append(xp) # appending the columns with xp
                    xcount = np.count_nonzero(dx == 1) #to count how many 1's r there in the above created matrix (dx) 
#                        print("xcount", xcount) # printing (xcount) in the name of "x" 

                    for iy in np.arange(nlSY, nlEY):
                        ynStrips=ym*iy+yc
                        #print(nStrips)
                        yp=round(ynStrips)
                        #print(p)
                        if(yp>=0 and yp<32):
                            dy[iy, int (yp)]=1
                            yindi.append(iy)
                            yindj.append(int (yp))
                    ycount = np.count_nonzero(dy == 1)
                        
                    minL= np.random.uniform(min_layer, max_layer )    
                    if (ycount==xcount<minL): #to avoid hits less than 3                 
                       xcount+=1             #xcount and ycount are made unequal bcz again it should go back to while loop
                                    
                    if(ycount==xcount): #writing the condition for number of hits in x should equal to hits in y  
                        
                        xmat[xindi,xindj] = 1 #the above if condition satifies then only fill the original matrix by 1, but it should use the indixes dummy matrixes indi & indj
                        ymat[yindi,yindj] = 1 #same for ynmatrix   
                        xmatn[xindi,xindj] = 1
                        ymatn[yindi,yindj] = 1
                        xnew[xindi,xindj] = 1
                        ynew[yindi,yindj] = 1
############################################################################################                    
                        xindief=[] #creating the dummy list for rows of above matrix to store the indexes where the hit is
                        xindjef=[]
                        
                        yindief=[] #creating the dummy list for rows of above matrix to store the indexes where the hit is
                        yindjef=[]
                        
                        xmate= np.tile(xmat,1)
                        ymate= np.tile(ymat,1)
                        
                        xmaten= np.tile(xmate,1)  
                        ymaten= np.tile(ymate,1)
                        
                        for e in np.arange(0, xcount):
                            effx=np.random.uniform(0, 100)
    #                        print("Efficiency x",effx)                        
    #                        print("Xi = ",xindi)
    #                        print("Yi = ",xindj)                   
    #                        print('x indices', xindi[e], xindj[e])
                            xmate[xindi[e], xindj[e]]=effx
                            xmaten[xindi[e], xindj[e]]=effx
                            
                            if(effx>eta):
                                xmate[xindi[e], xindj[e]]=0 
                                xmaten[xindi[e], xindj[e]]=0
    #                            ey[yindi[e], yindj[e]]=0 
                            else:
                                xmate[xindi[e], xindj[e]]=1
                                xmaten[xindi[e], xindj[e]]=1
                                
                                xindief.append(xindi[e])  #now appending the row values in the above created list xindi
                                xindjef.append(xindj[e])
                                
                            
                            effy=np.random.uniform(0, 100)
    #                        print("Efficiency y",effy)
    #                        print('y indices', yindi[e],yindj[e])
                            ymate[yindi[e], yindj[e]]=effy
                            ymaten[yindi[e], yindj[e]]=effy
                            
                            if(effy >eta ):
                                ymate[yindi[e], yindj[e]]=0
                                ymaten[yindi[e], yindj[e]]=0
                            else:
                                ymate[yindi[e], yindj[e]]=1
                                ymaten[yindi[e], yindj[e]]=1
                                
                                yindief.append(yindi[e])  #now appending the row values in the above created list xindi
                                yindjef.append(yindj[e])
                                
                            xnew= np.tile(xmate,1)
                            ynew= np.tile(ymate,1)
    #                        xmat= np.tile(xmate,1)                              
#######################################################################################                        
                        
                        xmats= np.tile(xmate,1)
                        ymats= np.tile(ymate,1) 
                        
                        for ii in range(len(xindief)):                        
    #                        print(ii)                    
                            stp_mult_x = np.random.uniform(0,150)
                            
                            if(xindief[ii]!=0 and xindjef[ii]!=31):                            
                                
                                if (stp_mult_x<50):
                                    #print('X ran L',stp_mult_x)
                                    xmats[xindief[ii], xindjef[ii]+1]=1
                                elif (stp_mult_x>100):
    #                                print('X ran R',stp_mult_x)
                                    xmats[xindief[ii], xindjef[ii]-1]=1
                                    
                        for jj in range(len(yindief)):                        
    #                        print(jj)    
                            stp_mult_y = np.random.uniform(0,150)
                            
                            if(yindief[jj]!=0 and yindjef[jj]!=31):
                            
                                if (stp_mult_y<50):
    #                                print('y ran L', stp_mult_y)
                                    ymats[yindief[jj], yindjef[jj]+1]=1
                                elif (stp_mult_y>100):
    #                                print('y ran R',stp_mult_y)
                                    ymats[yindief[jj], yindjef[jj]-1]=1
                            
                        xmat= np.tile(xmats,1)
                        ymat= np.tile(ymats,1)
                        
#################################################################################################################### 
#######            to see each matrix or trach and how tracks will goes on adds to the previous one                     
#                       plt.spy(xmat)
#                       plt.show()
        xmatno = addNoise(xmats, maxnoise)
        ymatno = addNoise(ymats, maxnoise)
               
        avg_x=[]
        for ii in np.arange(0,nLayers):
            xone=np.count_nonzero(xmat[ii,:]==1)
#            print(xone)
            avg_x.append(xone)          
        avgx=np.mean(avg_x)
        out[i,384]=avgx
        lengthx=len(avg_x)
#        print(lengthx)        
        s_x=[]
        for ii in np.arange(0,nLayers):            
#            su=np.sum((avg_x[ii]-avgx)) 
            sux=(avg_x[ii]-avgx) 
            s_x.append(sux)
        sumx=np.sum(s_x)
#        print('sum', sumx)
        SDx=np.sqrt(sumx**2/lengthx)
#        print('std dev',SDx)       
        out[i,385]=SDx
        
        avg_y=[]       
        for ii in np.arange(0,nLayers):
            yone=np.count_nonzero(ymat[ii,:]==1)
            avg_y.append(yone)
        avgy=np.mean(avg_y)
#            avy=round(avgy)
        out[i,770]=avgy
        print('average y',avgy)
        lengthy=len(avg_y)
#        print(lengthy)        
        s_y=[]
        for ii in np.arange(0,nLayers):            
#            su=np.sum((avg_x[ii]-avgx)) 
            suy=(avg_y[ii]-avgy) 
            s_y.append(suy)
        sumy=np.sum(s_y)
#        print('sum y', sumy)
        SDy=np.sqrt(sumy**2/lengthy)
        print('std dev y',SDy)        
        out[i,771]=SDy                
        
        plotspy('xmatn plot',xmatn, i)
        plotspy('xmate plot',xmate, i)
        plotspy('xmaten plot',xmaten, i)
        plotspy('xmat plot',xmat, i)
        
        plotspy('xmats plot',xmats, i)
        plotspy('xmatno plot',xmatno, i)
          
#        plotspy('y original plot',ymat, i)
        
        rxmat=np.reshape(xmat, (1,np.product(xmat.shape)))
        rymat=np.reshape(ymat, (1,np.product(ymat.shape)))
    
        out[i,:384]=rxmat #it gives array
        out[i,386:770]=rymat
        out[i,772]=mult+1 
        
    return out
eta=60
out1 =flattenmatrix(1, 1, 12, 32, 8, 12, eta)
