#!/usr/bin/env python

import os
import sys
import math
import ROOT
from array import array

param1 = sys.argv[1]
try:
    sys.argv[2]
except:
    rotate = 0
else:
    rotate = int(sys.argv[2])

file_no = "v40.release-SKoff-NO.txt"
file_io = "v40.release-SKoff-IO.txt"
#filelist = [file_no, file_io]
#More needed to make it work with IO b/c of negative dmsq values
filelist = [file_no]

if (param1 == "dcpvq13"):
    searchstring = "# T13/DCP projection"
    job = 1
elif (param1 == "dcpvq23"):
    searchstring = "# T23/DCP projection"
    job = 2
elif (param1 == "dmsqvq23"):
    searchstring = "# T23/DMA projection"
    job = 3

filenum = 0
for myfile in filelist:
    filenum += 1
    xvals = []
    yvals = []
    chi2 = []
    xbins = []
    ybins = []

    lfirst = True

    f = open(myfile)
    for line in f.readlines():
        if (lfirst and searchstring not in line):
            continue
        else:
            if lfirst:
                lfirst = False
                continue
        if not line.strip():
            break
        vals = line.split()
        xval = float(vals[0])
        yval = float(vals[1])
        chi2val = float(vals[2])

        if (job == 1):
            xval = math.sin(2*math.asin(math.sqrt(xval)))*math.sin(2*math.asin(math.sqrt(xval)))
            yval = dcpval/180.
        elif (job == 2):
            yval = yval/180.
        elif (job == 3):
            yvalorig = yval
            yval = yval - 0.0739
            print yval, yvalorig

        xvals.append(xval)
        yvals.append(yval)
        chi2.append(chi2val)
        if (job == 1 and xval==0.0):
            ybins.append(yval-2.5/180.)
        if (job == 2 and xval==0.250):
            ybins.append(yval-2.5/180.)
        if (job == 3 and xval==0.250):
            ybins.append(yval - 0.001)
        if ((job==1 or job==2) and yval==-1.):
            xbins.append(xval-0.0001)
        if (job==3 and yvalorig== 0.200):
            xbins.append(xval-0.001)

    xbins.append(xval+0.001)
    if (job==1 or job==2):
        ybins.append(yval+2.5/180)
    elif (job==3):
        ybins.append(yval+0.001)
    print xbins
    print ybins
    n = len(xvals)        
    nx = len(xbins)-1
    ny = len(ybins)-1
    xbins = array('d', xbins)
    ybins = array('d', ybins)
    if (filenum == 1):
        if (rotate==1):
            h_no = ROOT.TH2D("h_no","nufit contours rotated", ny, ybins, nx, xbins)
        else:
            h_no = ROOT.TH2D("h_no","nufit contours", nx, xbins, ny, ybins)
    elif (filenum == 2):
        if (rotate==1):
            h_io = ROOT.TH2D("h_io","nufit contours rotated", ny, ybins, nx, xbins)
        else:
            h_io = ROOT.TH2D("h_io","nufit contours", nx, xbins, ny, ybins)
        
    i=0
    while i<n:
        if (filenum == 1):
            if (rotate==1):
                h_no.Fill(yvals[i],xvals[i],chi2[i])
            else:
                h_no.Fill(xvals[i],yvals[i],chi2[i])
        elif (filenum == 2):
            if (rotate==1):
                h_io.Fill(yvals[i],xvals[i],chi2[i])
            else:
                h_io.Fill(xvals[i],yvals[i],chi2[i])                
        i += 1

if (job == 1):
    outfile = "root_v3/nufit_dcpvq13_contours.root"
elif (job == 2):
    outfile = "root_v3/nufit_dcpvq23_contours.root"
elif (job == 3):
    outfile = "root_v3/nufit_dmsqvq23_contours.root"
    
fout = ROOT.TFile(outfile,"RECREATE")
h_no.Write()
#h_io.Write()
fout.Close()

# c1 = ROOT.TCanvas("c1","c1",800,800)
# if (job == 1):
#     h1 = c1.DrawFrame(0.055, -180, 0.145, 180)
#     h1.GetXaxis().SetTitle("sin^{2}2#theta_{13}")
# elif (job == 2):
#     h1 = c1.DrawFrame(0.35, -180, 0.75, 180)
# h1.GetYaxis().SetTitle("#delta_{CP} (degrees)")
# h_no.Draw("cont0 same")
# h_no.SetContour(2)
# h_no.SetContourLevel(0,0)
# h_no.SetContourLevel(1,4.61)
# colors = [ROOT.kYellow-7]
# colors = array('i',colors)
# ROOT.gStyle.SetPalette(1,colors)

# if (job == 1):
#     plotname = "plots/nufit_dcpvth13_no.png"
# elif (job == 2):
#     plotname = "plots/nufit_dcpvth23_no.png"

# c1.SaveAs(plotname)


