#!/usr/bin/env python

import os
import sys
import math
import ROOT
from array import array

param1 = sys.argv[1]

file_no = "v40.release-SKoff-NO.txt"
file_io = "v40.release-SKoff-IO.txt"
filelist = [file_no, file_io]
#filelist = [file_no]

if (param1 == "dcpvq13"):
    searchstring = "# T13/DCP projection"
    job = 1
elif (param1 == "dcpvq23"):
    searchstring = "# T23/DCP projection"
    job = 2

filenum = 0
for myfile in filelist:
    filenum += 1
    dcp = []
    s22th13 = []
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
        th13val = float(vals[0])
        dcpval = float(vals[1])/180.
        chi2val = float(vals[2])
        dcp.append(dcpval)
        if (job == 1):
            myth13val = math.sin(2*math.asin(math.sqrt(th13val)))*math.sin(2*math.asin(math.sqrt(th13val)))
        elif (job == 2):
            myth13val = th13val
        elif (job == 3):
            mydmsqval = math.pow(10,dcpval) / 0.001
        else:
            myth13val = 99999.9
        s22th13.append(myth13val)
        chi2.append(chi2val)
        if (job == 1 and th13val==0.0):
            ybins.append(dcpval-2.5/180.)
        if (job == 2 and th13val==0.250):
            ybins.append(dcpval-2.5/180.)
        if (dcpval==-1.):
            xbins.append(myth13val-0.0001)

    xbins.append(myth13val+0.001)
    ybins.append(dcpval+2.5/180.)            
    n = len(dcp)        
    nx = len(xbins)-1
    ny = len(ybins)-1
    xbins = array('d', xbins)
    ybins = array('d', ybins)
    if (filenum == 1):
        h_no = ROOT.TH2D("h_no","dcpvs22th13", nx, xbins, ny, ybins)
    elif (filenum == 2):
        h_io = ROOT.TH2D("h_io","dcpvs22th13", nx, xbins, ny, ybins)
        
    i=0
    while i<n:
        if (filenum == 1):
            h_no.Fill(s22th13[i],dcp[i],chi2[i])
        elif (filenum == 2):
            h_io.Fill(s22th13[i],dcp[i],chi2[i])
        i += 1

if (job == 1):
    outfile = "root/nufit_dcpvq13_contours.root"
elif (job == 2):
    outfile = "root/nufit_dcpvq23_contours.root"
    
fout = ROOT.TFile(outfile,"RECREATE")
h_no.Write()
h_io.Write()
fout.Close()

c1 = ROOT.TCanvas("c1","c1",800,800)
if (job == 1):
    h1 = c1.DrawFrame(0.055, -180, 0.145, 180)
    h1.GetXaxis().SetTitle("sin^{2}2#theta_{13}")
elif (job == 2):
    h1 = c1.DrawFrame(0.35, -180, 0.75, 180)
h1.GetYaxis().SetTitle("#delta_{CP} (degrees)")
h_no.Draw("cont0 same")
h_no.SetContour(2)
h_no.SetContourLevel(0,0)
h_no.SetContourLevel(1,4.61)
colors = [ROOT.kYellow-7]
colors = array('i',colors)
ROOT.gStyle.SetPalette(1,colors)

if (job == 1):
    plotname = "plots/nufit_dcpvth13_no.png"
elif (job == 2):
    plotname = "plots/nufit_dcpvth23_no.png"

c1.SaveAs(plotname)


