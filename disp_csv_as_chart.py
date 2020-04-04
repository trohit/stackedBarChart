#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:15:48 2020

@author: rohit
"""
import csv

import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil


def get_ll_by_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
    #print(data)
    return data


def get_time_and_val_lists(ll):
    # ll is a list of sub-lists where each sub-list is [dt,val] 
    dl = []
    vl = []
    for sl in ll:
        #print("sl:" + str(sl))
        dl.append(sl[0])
        vl.append(sl[1])
    #print("dl" + str(dl))
    #print("vl" + str(vl))
    return (dl, vl)

def show_graph_from_tv_ll(xl, yl):    
    dates = [dateutil.parser.parse(s) for s in xl]
    plt_data = yl
    plt.subplots_adjust(bottom=0.4)
    #plt.xticks( rotation=50 )
    labels = dates
    x = plt_data
    plt.xticks(rotation='vertical')
    
    ax=plt.gca()
    ax.set_xticks(dates)
    ax.xaxis.grid(True, which='minor')
    
    # set the basic properties
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel('Available Mem')
    ax.set_title('Avail mem during NDU ')
    # tweak the title
    ttl = ax.title
    ttl.set_weight('bold')

    # set the grid on
    ax.grid('on')

    # tweak the axis labels
    xlab = ax.xaxis.get_label()
    ylab = ax.yaxis.get_label()
    xlab.set_style('italic')
    xlab.set_size(10)
    ylab.set_style('italic')
    ylab.set_size(10)
    
    ## show bluish tint under graph
    #l = ax.fill_between(xl, yl)
    ## change the fill into a blueish color with opacity .3
    #l.set_facecolors([[.5,.5,.8,.3]])
    
    # change the edge color (bluish and transparentish) and thickness
    #l.set_edgecolors([[0, 0, .5, .3]])
    #l.set_linewidths([3])

    ax.fill_between(dates, plt_data)    
    xfmt = md.DateFormatter('%b %d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.plot(dates,plt_data, "o-")
    #plt.show()

#main
if __name__ == "__main__":
    ll = get_ll_by_csv('data.csv')
    dll, vll = get_time_and_val_lists(ll)
    print("dll" + str(dll))        
    print("vll" + str(vll))
    show_graph_from_tv_ll(dll, vll)