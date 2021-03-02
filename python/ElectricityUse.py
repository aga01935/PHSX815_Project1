#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random
from MySort import MySort

# main function for our coin toss Python code
if __name__ == "__main__":
    # default single coin-toss probability for hypothesis 0
    p0 = 0.5


    # default single coin-toss probability for hypothesis 1
    p1 = 0.9
    print (sys.argv[0])

    haveH0 = False
    haveH1 = False

    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True

    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("options:")
        print ("-input0 <string>       name of Simulated H0 Hypothesis ASCII data")
        print ("-input1 <string>       name of Simulated H1 Hypothesis ASCII data")
        print
        sys.exit(1)
    Troom = 30
    Ntoss = 1
    Npass0 = []
    LogLikeRatio0 = []
    Npass1 = []
    LogLikeRatio1 = []
    #first_line= []
    Npass_min = 1e8
    Npass_max = -1e8
    LLR_min = 1e8
    LLR_max = -1e8
    sorter = MySort()

    with open(InputFile0) as ifile:
        first_line1 =ifile.readline().strip()
        cause1 = first_line1[0] + first_line1[1]
        #print(first_line[3])
        temp = float(first_line1[2]+first_line1[3])
        abs_temp = abs(Troom-temp)
        next(ifile)
        for line in ifile:
            #print (line)
            lineVals = line.split()
            #print (lineVals)
            Ntoss = len(lineVals)
            Npass = 0
            LLR = 0
            for v in lineVals:
                # adding LLR for this toss
                #if float(v) >= 1:
                LLR += math.log( (abs_temp * float(v)**2)/( abs_temp * float(v) ) )
                #else:
                #    LLR += math.log( (1.-p1)/(1.-p0) )

            if Npass < Npass_min:
                Npass_min = Npass
            if Npass > Npass_max:
                Npass_max = Npass
            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR
            Npass0.append(Npass)
            LogLikeRatio0.append(LLR)

    if haveH1:
        with open(InputFile1) as ifile:
            first_line2 =ifile.readline().strip()
            cause2 = first_line2[0] + first_line2[1]
            #print(first_line[0],first_line[1],first_line[1])
            temp = float(first_line2[2]+first_line2[3])
            abs_temp = abs(Troom-temp)
            next(ifile)
            for line in ifile:
                lineVals = line.split()
                Ntoss = len(lineVals)
                Npass = 0
                LLR = 0
                for v in lineVals:
                    Npass += float(v);
                    # adding LLR for this toss
                    #if float(v) >= 1:
                    LLR += math.log(( abs_temp * float(v) )/(abs_temp * float(v)**2))
                    #else:
                    #    LLR += math.log( (1.-p1)/(1.-p0) )

                if Npass < Npass_min:
                    Npass_min = Npass
                if Npass > Npass_max:
                    Npass_max = Npass
                if LLR < LLR_min:
                    LLR_min = LLR
                if LLR > LLR_max:
                    LLR_max = LLR
                Npass1.append(Npass)
                LogLikeRatio1.append(LLR)

    title = str(Ntoss) +  " Trial / experiment"

    # make Npass figure
    plt.figure()
    plt.hist(Npass0, Ntoss-1, density=True, facecolor='b', alpha=0.5,range=(1,5), label="assuming " + cause1)
    if haveH1:
        plt.hist(Npass1, Ntoss-1, density=True, facecolor='g', alpha=0.5,range=(1,5), label="assuming " + cause2)
        plt.legend()

    plt.xlabel('$\\lambda = N_{pass}$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()

    # make LLR figure
    LogLikeRatio0 = sorter.DefaultSort(LogLikeRatio0)
    LogLikeRatio1 = sorter.DefaultSort(LogLikeRatio1)
    plt.figure()
    plt.hist(LogLikeRatio0, Ntoss+1, density=True, facecolor='b', alpha=0.5,label="assuming "+ cause1)
    if haveH1:
        plt.hist(LogLikeRatio1, Ntoss+1, density=True, facecolor='g', alpha=0.7, label="assuming "+ cause2)
        plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()
