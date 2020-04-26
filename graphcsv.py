#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:15:48 2020
@author: rohit

python3.7 ./graphcsv.py -i /tmp/linuxmem_a.csv --offset 5 --vxdate "Apr 06 11:04:50" --vpct 20 --vtitle "report gen started"

date,drname,cpupct,curmem,maxmem,mempct,netrx,nettx
Apr 06 11:00:37,ubuntu_docker,26.52,5.019,28G,17.93,0B,0B
Apr 06 11:01:40,ubuntu_docker,0.22,5.019,28G,17.92,0B,0B
Apr 06 11:02:44,ubuntu_docker,0.20,5.019,28G,17.93,0B,0B
Apr 06 11:03:47,ubuntu_docker,0.22,5.019,28G,17.93,0B,0B

"""
import csv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
import sys
import os
import argparse

def extract_datetime(dt_str):
    print("parsing date:" + dt_str)
    dt = dateutil.parser.parse(dt_str)
    return dt

def is_header_in_row(row):
    if row[0].isalpha():
        return True

def get_ll_by_csv(filename):
    hdr = None
    if not os.path.isfile(filename):
        print("Unable to open file " + str(filename))
        sys.exit(1)

    with open(filename) as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
    if is_header_in_row(data[0]):
        hdr = data.pop(0)
    #import pdb; pdb.set_trace()
    return hdr, data

def get_time_and_val_lists(ll, field_offset_to_graph):
    # ll is a list of sub-lists where each sub-list is [dt,val]
    dl = []
    vl = []
    for sl in ll:
        # offset 0 is the date list
        #print("sl:" + str(sl))
        #import pdb; pdb.set_trace()
        dl.append(sl[0])
        vl.append(float(sl[field_offset_to_graph]))
    return (dl, vl)

    #disp_chart(date_list, val_list, hdr[0], hdr[field_offset_to_graph], fname, vxdate, vtitle, vpct)
def disp_chart(xl, yl, x_label, y_label, title, vx_date=None, vx_label=None, vpct=20):
    import pdb; pdb.set_trace()
    x = [ extract_datetime(i) for i in xl ]
    y = [float(i) for i in yl]
#    import pdb; pdb.set_trace()
    print("x:" + str(x))
    print("y:" + str(y))

    # embellishments
    ax=plt.gca()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.title.set_weight('bold')
    ax.grid('on')
    ax.xaxis.get_label().set_style('italic')
    ax.xaxis.get_label().set_size(10)
    ax.yaxis.get_label().set_style('italic')
    ax.yaxis.get_label().set_size(10)
    ## show bluish tint under graph
    ax.fill_between(x, y)
    plt.tight_layout()
    #plt.minorticks_on()
    plt.xticks(rotation=50)

    ymin, ymax = ax.get_ylim()


    #ax.axvline("Apr 06 19:38:10", color="red", linestyle="--")
    #plt.axvline(extract_datetime("Apr 12 16:28:41"), color='r', linewidth=2.0, linestyle='--')
    #plt.text(extract_datetime("Apr 12 16:28:20"),(ymax-ymin)/4,'16:28:41 rx nw hb slow 4123ms',rotation=90,color='r')

    #def disp_chart(xl, yl, x_label, y_label, title, vx_date=None, vx_label=None, vpct=0.2):
    if vx_date is not None:
        plt.axvline(extract_datetime(vx_date), color='r', linewidth=2.0, linestyle='--')
        if vx_label is not None:
            plt.text(extract_datetime(vx_date),(ymax-ymin)*(int(vpct)/100),vx_label, rotation=90,color='r')
            
    # set the basic properties
    #plt.plot(x,y, "or-")
    plt.plot(x,y, "ok-")
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    myFmt = md.DateFormatter('%H:%M')
    plt.gca().xaxis.set_major_formatter(myFmt)
    #plt.show()
    print("Saving to :" + title + '.png')
    plt.savefig(title + '.png')
    plt.close()

def parse():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('-i', required=True, help="<input_csv_file>")
    #optional.add_argument('-o', help="<out_png_file>")
    #optional.add_argument('--vxdate', metavar='vx timeline')
    optional.add_argument('--offset', help="offset in csvfile(2 onwards)",default=2, type=int)
    optional.add_argument('--vxdate',help="date like 'Apr 19 13:23:31'")
    optional.add_argument('--vpct', metavar="<0-100>(in percent)")
    optional.add_argument('--vtitle')
    return parser.parse_args()

#main
if __name__ == "__main__":
    dd = parse()
    path = dd.i
    field_offset_to_graph = dd.offset
    vpct = dd.vpct
    vxdate = dd.vxdate
    vtitle = dd.vtitle
    #matplotlib.use("agg")
    #import pdb; pdb.set_trace()
    #defaults

    #field_offset_to_graph = 2
    #argc = len(sys.argv)
    ##import pdb; pdb.set_trace()
    #if argc > 1:
    #    path = sys.argv[1]
    #else:
    #    #path = input("Please enter a csv file to graph:\n")
    #    print("Usage:" + sys.argv[0] + " <file> [offset_starts_from_2]\n")
    #    sys.exit(1)
    #    path = "data.csv"
    #if argc > 2:
    #    # first field is datetime which is at offset 0
    #    field_offset_to_graph = sys.argv[2]
    #    print("using  offset:" + str(field_offset_to_graph))
    #    field_offset_to_graph = int(field_offset_to_graph)

    print(os.getcwd())
    hdr, ll = get_ll_by_csv(path)
    fname = os.path.basename(path)
    date_list, val_list = get_time_and_val_lists(ll, field_offset_to_graph)
    #import pdb; pdb.set_trace()
# =============================================================================
#    import pdb; pdb.set_trace()
#     date_list=["Apr 10 09:22:41", "Apr 10 09:32:41", "Apr 10 09:35:41"]
#     val_list = [50,20,30]
#     hdr= ["hdra", "hdrb"]
# =============================================================================
    #disp_chart(date_list, val_list, hdr[0], hdr[2], fname)
    #disp_chart(date_list, val_list, hdr[0], hdr[field_offset_to_graph], fname)
#def disp_chart(xl, yl, x_label, y_label, title, vx_date=None, vx_label=None, vpct=0.2):
    disp_chart(date_list, val_list, hdr[0], hdr[field_offset_to_graph], fname, vxdate, vtitle, vpct)
