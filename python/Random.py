#! /usr/bin/env python

import math
import numpy as np

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)

        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()
# function returns random integer between 1 and 100
    def myrandint(self,min=1., max=100.):
        ran1 = self.rand()
        ran2 = self.rand()*100
        Inti = 100*ran1%ran2
        print (min, max , Inti)
        while Inti>max or Inti<min :
            ran1 = self.rand()
            ran2 = self.rand()
            #print (Inti)
        return int(Inti)
    def parabolic_dist(self,temp=30.):
        room_temp = 30
        low_temp = -40.0
        high_temp= 100.

        if temp < -40.:
            print("temperature is too low  \n changing the  value of a to  %f " % low_temp )
        if temp > 100.:
            print("temperature is too low  \n changing the  value of a to  %f " % high_temp )
            temp = low_temp
        change_temp = abs(temp-room_temp)
        Myrand = float(self.rand())
        #Myrand = self.myrandint(1,10)
        while Myrand <= 0.:
            Myrand = float(self.rand())
            #Myrand = self.myrandint(1,10)
            #hisrand = float(self.rand())

        X= np.sqrt(Myrand/change_temp)
        #print (X)
        return X
    def linear_dist(self,temp=30.):
        room_temp = 30
        low_temp = -40.0
        high_temp= 100.

        if temp < -40.:
            print("temperature is too low  \n changing the  value of a to  %f " % low_temp )
        if temp > 100.:
            print("temperature is too low  \n changing the  value of a to  %f " % high_temp )
            temp = low_temp
        change_temp = abs(temp-room_temp)
        NewRand = float(self.rand())
        #NewRand = self.myrandint(1,10)
        while NewRand<=0.:
            NewRand=float(self.rand())
            #NewRand = self.myrandint(1,10)
        y = float(NewRand/change_temp)
        return y
