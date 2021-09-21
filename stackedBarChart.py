#!/usr/bin/env python3
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
from operator import add
from pprint import pprint
#
#             LEGEND
#   Read cndl as Candle
#   Read lbl  as Label
#
# In normal config
# cndlsMasterLbl sits parallel to X Axis
# valuesMasterLbl sits parallel to Y Axis
#
#               TITLE
#      ^
#      |
#    Y |              +-+
#      |              | |
#      |        +-+   | |
#      |  +-+   | |   | |
#      |  | |   | |   | |
#      +--+-+---+-+---+-+------->
#       X Axis cndlsMasterLbl
#              Legend
#       lyrColors -> lyrNames
#
def stackedBarChart(Title, cndlsMasterLbl, valuesMasterLbl, cndlThickness,
        minValue, maxValue, cndlCount, cndlLbls, arrVals, lyrNames,
        lyrColors):
    #draw bar chart
    print("cndlCount:"+str(cndlCount))
    assert( len(arrVals) == len(lyrColors))

    # XXX: Perhaps cndlCount can be derived from cndlLbls
    assert( (cndlCount) == len(cndlLbls))

    minReading = minValue
    # just so that the maximum value doesn't get missed
    maxReading = maxValue + 1
    # gradual gradient markers to help read the values
    stepSize = (maxReading - minReading) /10

    ind = np.arange(cndlCount)    # the x locations for the groups
    emptyArr = [0] * cndlCount
    sumArr = emptyArr
    containerArr = []
    graphBottom = None
    p = [] # list of bar properties

    plt.subplots_adjust(bottom=0.2) #make room for the legend
    for i in range(len(arrVals)):
        selectedColor = lyrColors[i]
        print("Adding color " + selectedColor)
        tmpContainer = plt.bar(ind, arrVals[i], cndlThickness, color=selectedColor, bottom=graphBottom)
        containerArr.append(tmpContainer)
        tmpArr = arrVals[i]
        sumArr = [tmpArr[j] + sumArr[j] for j in range(cndlCount)]
        graphBottom = sumArr
        pprint(graphBottom)

    plt.ylabel(valuesMasterLbl)
    plt.xlabel(cndlsMasterLbl)
    plt.title(Title)
    #plt.xticks(ind+cndlThickness/2., cndlLbls)
    spacing = ind+cndlThickness/2.
    pprint(spacing)
    plt.xticks(spacing, cndlLbls)
    legArr = []
    print(type(legArr))

    plt.yticks(np.arange(minReading, maxReading, stepSize))
    #plt.legend( (p1[0], p2[0], p3[0], p4[0]), lyrNames)
    #TODO: solve the part of passing variable length args to a function

    print("len(containerArr):" + str(len(containerArr)))
    for zz in range(0, len(containerArr)):
        legArr.append(containerArr[zz])

    # its called the splat operator
    # http://stackoverflow.com/questions/7745952/python-expand-list-to-function-arguments
    # http://stackoverflow.com/questions/12720450/unpacking-arguments-only-named-arguments-may-follow-expression
    plt.legend(
         bbox_to_anchor=(0.5, -0.3),
         loc='lower center',
         ncol=7,labels=(lyrNames),*legArr)
    plt.grid()
    #plt.show()
    plt.savefig('books_read.png')

if __name__ == "__main__":
    Title  = 'Visitors by block and day'
    cndlsMasterLbl = 'Date'
    valuesMasterLbl = 'No. of Visitors'
    cndlThickness = 0.30 # the cndlThickness of the bars: can also be len(x) sequence
    #           Mo, Tu, We, Th, Fr, Sa, Su
    blkCntAr = (10, 30, 30, 35, 27, 67, 21)
    blkCntBr = (20, 32, 34, 20, 25, 76, 21)
    blkCntEl = (30, 34, 34, 20, 25, 76, 21)
    blkCntGl = (40, 36, 34, 20, 25, 76, 21)
    blkCntHl = (25, 32, 34, 20, 25, 76, 21)
    blkCntJg = (25, 32, 34, 20, 25, 76, 21)
    blkCntJl = (25, 32, 34, 20, 25, 76, 21)
    blkCntZr = (25, 32, 34, 20, 25, 76, 21)
    blkCntMB = (25, 32, 34, 20, 25, 76, 21)
    blkCntMR = (25, 32, 34, 20, 25, 76, 21)
    blkCntMT = (25, 32, 34, 20, 25, 76, 21)
    blkCntRs = (25, 32, 34, 20, 25, 76, 21)
    blkCntOh = (25, 32, 34, 20, 25, 76, 21)
    minValue = 0
    maxValue = 1000
    # XXX: Round off to nearest bracket ..multiple of 10..50..100..500..1000
    maxObsValue = max(map(sum,zip(blkCntAr,blkCntBr,blkCntEl,blkCntGl,blkCntHl,blkCntJg,blkCntJl,blkCntZr,blkCntMB,blkCntMR,blkCntMT,blkCntRs,blkCntOh)))
    assert(maxValue > maxObsValue),"Max val " + str(maxValue) + " < max observed val " + str(maxObsValue)
    cndlCount = len(blkCntAr) # count of elements in each category
    blocks=["Ar","Br","El","Gl","Hl","Jl","Jg","Zr","MB","MR","MT","Rs","Oh"]
    lyrNames = blocks
    cndlLbls = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    arrVals = blkCntAr,blkCntBr,blkCntEl,blkCntGl,blkCntHl,blkCntJg,blkCntJl,blkCntZr,blkCntMB,blkCntMR,blkCntMT,blkCntRs,blkCntOh
    lyrColors = ('r','g','b','c','m','y','k','Brown', 'Crimson','w','BlueViolet', 'DarkOrange','DeepPink')
    # days   -> cndls -> X
    # blocks -> lyrs  -> Y
    # len(arrVals) = len(lyrColors)
    stackedBarChart(Title, cndlsMasterLbl, valuesMasterLbl, cndlThickness, minValue, maxValue, cndlCount, cndlLbls, arrVals, lyrNames, lyrColors)
