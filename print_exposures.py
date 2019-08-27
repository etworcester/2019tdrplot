#!/usr/bin/env python

import sys
import math
import ROOT
from array import array

ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetTitleFillColor(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetMarkerStyle(20)
ROOT.gStyle.SetTitleX(0.5)
ROOT.gStyle.SetTitleAlign(23)
ROOT.gStyle.SetLineWidth(3)
ROOT.gStyle.SetLineColor(1)
ROOT.gStyle.SetTitleSize(0.03,"t")

def filldiff(up,down):
      n = up.GetN()
      diffgraph = ROOT.TGraph(2*n);
      i = 0
      xup = ROOT.Double(-9.9)
      yup = ROOT.Double(-9.9)
      xlo = ROOT.Double(-9.9)
      ylo = ROOT.Double(-9.9)
      while i<n:
          up.GetPoint(i,xup,yup);
          down.GetPoint(n-i-1,xlo,ylo);
          diffgraph.SetPoint(i,xup,yup);
          diffgraph.SetPoint(n+i,xlo,ylo);
          i += 1
      return diffgraph;

hier = sys.argv[1]
if (hier == 'nh'):
      htext = "Normal Ordering"
elif (hier == 'ih'):
      htext = "Inverted Ordering"
else:
      print "Must supply no or io!"
      exit()

explist = [0,1,5,10,30,50,100,200,336,450,624,800,1104,1300,1500]
explist_nozero = [1,5,10,30,50,100,200,336,450,624,800,1104,1300,1500]
explist = array('d',explist)
explist_nozero = array('d',explist_nozero)

f1 = ROOT.TFile("root_v4/staging_convert.root")
g_exp = f1.Get("g_exp")

adict = {}
ndict = {}
f2 = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root")
for g in f2.GetListOfKeys():
      name = g.GetName()
      tmp = f2.Get(name)
      thisn = tmp.GetN()
      thisa = [ROOT.Double(0.0)]*thisn
      thisa = array('d',thisa)
      thisa = tmp.GetY()
      adict[name] = thisa
      ndict[name] = thisn

#Fill exposure graphs backwards
g_cpvsig75_nopen = ROOT.TGraph(ndict["cpvsig75_nopen"],adict["cpvsig75_nopen"],explist)
g_cpvsig50_nopen = ROOT.TGraph(ndict["cpvsig50_nopen"],adict["cpvsig50_nopen"],explist)
g_cpvsigbest_nopen = ROOT.TGraph(ndict["cpvsigbest_nopen"],adict["cpvsigbest_nopen"],explist)
g_cpvsig75_th13pen = ROOT.TGraph(ndict["cpvsig75_th13pen"],adict["cpvsig75_th13pen"],explist)
g_cpvsig50_th13pen = ROOT.TGraph(ndict["cpvsig50_th13pen"],adict["cpvsig50_th13pen"],explist)
g_cpvsigbest_th13pen = ROOT.TGraph(ndict["cpvsigbest_th13pen"],adict["cpvsigbest_th13pen"],explist)

g_mhsig100_nopen = ROOT.TGraph(ndict["mhsig100_nopen"],adict["mhsig100_nopen"],explist)
g_mhsigbest_nopen = ROOT.TGraph(ndict["mhsigbest_nopen"],adict["mhsigbest_nopen"],explist)
g_mhsig100_th13pen = ROOT.TGraph(ndict["mhsig100_th13pen"],adict["mhsig100_th13pen"],explist)
g_mhsigbest_th13pen = ROOT.TGraph(ndict["mhsigbest_th13pen"],adict["mhsigbest_th13pen"],explist)

g_dcpres0_nopen = ROOT.TGraph(ndict["dcpres0_nopen"],adict["dcpres0_nopen"],explist_nozero)
g_dcpresneg_nopen = ROOT.TGraph(ndict["dcpresneg_nopen"],adict["dcpresneg_nopen"],explist_nozero)
g_dcpres0_th13pen = ROOT.TGraph(ndict["dcpres0_th13pen"],adict["dcpres0_th13pen"],explist_nozero)
g_dcpresneg_th13pen = ROOT.TGraph(ndict["dcpresneg_th13pen"],adict["dcpresneg_th13pen"],explist_nozero)

g_th13res_nopen = ROOT.TGraph(ndict["th13res_nopen"],adict["th13res_nopen"],explist_nozero)
g_th23res_nopen = ROOT.TGraph(ndict["th23res_nopen"],adict["th23res_nopen"],explist_nozero)
g_dmsqres_nopen = ROOT.TGraph(ndict["dmsqres_nopen"],adict["dmsqres_nopen"],explist_nozero)

g_th23res_th13pen = ROOT.TGraph(ndict["th23res_th13pen"],adict["th23res_th13pen"],explist_nozero)
g_dmsqres_th13pen = ROOT.TGraph(ndict["dmsqres_th13pen"],adict["dmsqres_th13pen"],explist_nozero)

#Get numbers I want

cpv75_nom_3sig = g_cpvsig75_th13pen.Eval(3.0,0,"S")
cpv50_nom_3sig = g_cpvsig50_th13pen.Eval(3.0,0,"S")
cpv50_nom_5sig = g_cpvsig50_th13pen.Eval(5.0,0,"S")
cpvbest_nom_5sig = g_cpvsigbest_th13pen.Eval(5.0,0,"S")
cpvbest_nom_3sig = g_cpvsigbest_th13pen.Eval(3.0,0,"S")

mh100_nom_5sig = g_mhsig100_th13pen.Eval(5.0,0,"S")
mhbest_nom_5sig = g_mhsigbest_th13pen.Eval(5.0,0,"S")

dcpres0_nom_10deg = g_dcpres0_th13pen.Eval(10.0,0,"S")
dcpresneg_nom_20deg = g_dcpresneg_th13pen.Eval(20.0,0,"S")

#g_th13res_nopen.Draw("alp")
#raw_input()
th13res_nom_005 = g_th13res_nopen.Eval(0.005,0,"S")
th13res_nom_004 = g_th13res_nopen.Eval(0.004,0,"L")
th13res_nom_003 = g_th13res_nopen.Eval(0.003,0,"L")

print "CPV 75% (3 sigma): ", cpv75_nom_3sig, g_exp.Eval(cpv75_nom_3sig,0,"S")
print "CPV 50% (3 sigma): ", cpv50_nom_3sig, g_exp.Eval(cpv50_nom_3sig,0,"S")
print "CPV 50% (5 sigma): ", cpv50_nom_5sig, g_exp.Eval(cpv50_nom_5sig,0,"S")
print "CPV -pi/2 (3 sigma): ", cpvbest_nom_3sig, g_exp.Eval(cpvbest_nom_3sig,0,"S")
print "CPV -pi/2 (5 sigma): ", cpvbest_nom_5sig, g_exp.Eval(cpvbest_nom_5sig,0,"S")

print "MH 100% (5 sigma): ", mh100_nom_5sig, g_exp.Eval(mh100_nom_5sig,0,"S")
print "MH -pi/2 (5 sigma): ", mhbest_nom_5sig, g_exp.Eval(mhbest_nom_5sig,0,"S")
print "Res at dcp=0 (10 degs): ", dcpres0_nom_10deg, g_exp.Eval(dcpres0_nom_10deg,0,"S")
print "Res at dcp=-pi/2 (20 degs): ", dcpresneg_nom_20deg, g_exp.Eval(dcpresneg_nom_20deg,0,"S")

print "sin22th13 res (0.005): ", th13res_nom_005, g_exp.Eval(th13res_nom_005,0,"S")
print "sin22th13 res (0.004): ", th13res_nom_004, g_exp.Eval(th13res_nom_004,0,"S")
print "sin22th13 res (0.003): ", th13res_nom_003, g_exp.Eval(th13res_nom_003,0,"S")

