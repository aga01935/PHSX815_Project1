#! /usr/bin/env python3
python3 $PWD/python/Simulator.py -Nexp ${1:-10000} -Nmes ${2:-10} -temp ${3:-20} -seed ${4:-430} -output ${5:-"H0.txt"} -cause ${6:-"HF"}
python3 $PWD/python/Simulator.py -Nexp ${1:-10000} -Nmes ${2:-10} -temp ${3:-20} -seed ${4:-450} -output ${7:-"H1.txt"} -cause ${8:-"ED"}
#echo $7
#echo $5
python3 $PWD/python/ElectricityUse.py -input0 ${5:-H0.txt} -input1 ${7:-H1.txt}
