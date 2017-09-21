import argparse, os, cPickle, sys, numpy, ntpath
from pyAudioAnalysis import audioFeatureExtraction as aF
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioSegmentation as aS
import matplotlib.pyplot as plt
import io
import os
import shutil
import ntpath
import numpy
import cPickle
import glob

def parseArguments():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('-f' , '--foldPath', nargs=1, required=True, help="path to a particular fold's folder")  
    parser.add_argument('-m' , '--modeltype', nargs=1, required=True, help="model type")    
    args = parser.parse_args()
        
    return args



if __name__ == '__main__':
    args = parseArguments()
    dirName = args.foldPath[0]
    modelType = args.modeltype[0]        
    #dirName = "/Users/tyiannak/ResearchData/Audio Dataset/mobileSoundScape/data"
    #aT.featureAndTrainRegression(dirName, 1, 1, 0.4, 0.2, modelType, modelType+"_soundscape", False)
    #aT.featureAndTrainRegression(dirName, 1, 1, 0.02, 0.02, "svm_rbf", "sq_svm_rbf", False)
