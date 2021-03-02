#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
from python.Random import Random
# Electricity Analysis Main Function
if __name__ == "__main__":
    # if user do not provide any arguments  or provide -h then print this option
    if '-h' in sys.argv or '--help' in sys.argv :
        print ("Usage: %s [-seed number] [options]" % sys.argv[0] )
        print ("options:")
        print ("-seed <number >        provide any four digit seed for random number, default is 5555" )
        print ("-cause <stringr>         cuse of electricity use , default is <ED> options is either electric devices <ED> or Heating Furnace <HF>")
        print ("-Nmes <number>         number of measurements to make, default is 1")
        print ("-Nexp <number>         number of experiment to perform, default is 1")
        print ("-output <string>       name of output file to produce, default is 1")
        print ("-temp <number>         outside temperature , default is 30 celsious")
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default rate parameter for cookie disappearance (cookies per day)
    cause = "ED"

    # default number of time measurements (time to next missing cookie) - per experiment
    Nmes = 1

    # default number of experiments
    Nexp = 1

    #Temperature in celcious
    temp = 30.

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-cause' in sys.argv:
        p = sys.argv.index('-cause')
        ptemp = sys.argv[p+1]
        cause = ptemp
    if '-Nmes' in sys.argv:
        p = sys.argv.index('-Nmes')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-temp' in sys.argv:
        p = sys.argv.index('-temp')
        tp = float(sys.argv[p+1])
        temp = tp
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = Random(seed)
    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        outfile.write(cause)
        outfile.write(str(temp))
        outfile.write(str(seed)+" \n")

        if (cause=="ED"):
            for e in range(0,Nexp):
                for t in range(0,Nmeas):
                    outfile.write(str(random.linear_dist(temp))+" ")
                outfile.write(" \n")
        if (cause=="HF"):
            for e in range(0,Nexp):
                for t in range(0,Nmeas):
                    outfile.write(str(random.parabolic_dist(temp))+" ")
                outfile.write(" \n")
        outfile.close()
