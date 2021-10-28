#!/usr/bin/env python

import sys
import math
import ctypes
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

hier = sys.argv[1]
if (hier == 'nh'):
      htext = "Normal Ordering"
      hnum = "1"
elif (hier == 'ih'):
      htext = "Inverted Ordering"
      hnum = "-1"
else:
      print("Must supply nh or ih!")
      exit()

explist = [0,6,12,24,66,100,150,200,336]
mhlist100_nom = [0]
mhlist50_nom = [0]
mhlistbest_nom = [0]
mhlist100_notms = [0]
mhlist50_notms = [0]
mhlistbest_notms = [0]

for myexp in explist:

      if (myexp==0):
            continue

      #Nominal
      filename = "/Users/etw/Documents/DUNE/work/2019_cafana_tdrplot/root_notms/mh_sens_ndfd"+str(myexp)+"_allsyst_th13_asimov0_hie1_nominal.root"
      f1 = ROOT.TFile(filename)
      mhgraph = f1.Get("sens_mh_"+hier)
      nvals = mhgraph.GetN()
      cutbest = int(0.25*nvals)
      cut50 = int(0.5*nvals)     
      mh_vals = [0.0]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph.GetY()

      i = 0
      mh_vals_nom = []
      while i < nvals:
            mh_vals_nom.append(mh_vals[i])
            i += 1

      mhlist100_nom.append(min(mh_vals_nom))
      mhlistbest_nom.append(mh_vals_nom[cutbest])
      mhlist50_nom.append(sorted(mh_vals_nom)[cut50])
      f1.Close()

      #No TMS
      filename = "/Users/etw/Documents/DUNE/work/2019_cafana_tdrplot/root_notms/mh_sens_ndfd"+str(myexp)+"_allsyst_th13_asimov0_hie1_FluxWiggle_BOTH:-1.root"
      f1 = ROOT.TFile(filename)
      mhgraph = f1.Get("sens_mh_"+hier)
      nvals = mhgraph.GetN()
      cutbest = int(0.25*nvals)
      cut50 = int(0.5*nvals)           
      mh_vals = [0.0]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph.GetY()

      i = 0
      mh_vals_notms = []
      while i < nvals:
            mh_vals_notms.append(mh_vals[i])
            i += 1

      mhlist100_notms.append(min(mh_vals_notms))
      mhlistbest_notms.append(mh_vals_notms[cutbest])
      mhlist50_notms.append(sorted(mh_vals_notms)[cut50])      
      f1.Close()

n = len(explist)
explist = array('d',explist)

mhlist100_nom = array('d',mhlist100_nom)
mhlist100_notms = array('d',mhlist100_notms)

mhlist50_nom = array('d',mhlist50_nom)
mhlist50_notms = array('d',mhlist50_notms)

mhlistbest_nom = array('d',mhlistbest_nom)
mhlistbest_notms = array('d',mhlistbest_notms)

g_mhsig_100_nom = ROOT.TGraph(n,explist,mhlist100_nom)
g_mhsig_100_notms = ROOT.TGraph(n,explist,mhlist100_notms)

g_mhsig_50_nom = ROOT.TGraph(n,explist,mhlist50_nom)
g_mhsig_50_notms = ROOT.TGraph(n,explist,mhlist50_notms)

g_mhsig_best_nom = ROOT.TGraph(n,explist,mhlistbest_nom)
g_mhsig_best_notms = ROOT.TGraph(n,explist,mhlistbest_notms)

g_mhsig_100_nom.SetLineWidth(3)
g_mhsig_100_notms.SetLineStyle(3)
g_mhsig_100_notms.SetLineWidth(3)

g_mhsig_50_nom.SetLineWidth(3)
g_mhsig_50_notms.SetLineStyle(3)
g_mhsig_50_notms.SetLineWidth(3)

g_mhsig_best_nom.SetLineWidth(3)
g_mhsig_best_notms.SetLineStyle(3)
g_mhsig_best_notms.SetLineWidth(3)


g_mhsig_100_nom.SetLineColor(ROOT.kOrange-3)
g_mhsig_100_notms.SetLineColor(ROOT.kOrange+3)
g_mhsig_50_nom.SetLineColor(ROOT.kOrange-3)
g_mhsig_50_notms.SetLineColor(ROOT.kOrange+3)
g_mhsig_best_nom.SetLineColor(ROOT.kOrange-3)
g_mhsig_best_notms.SetLineColor(ROOT.kOrange+3)


myout = ROOT.TFile("root_v4/exposure_graphs_notms_"+hier+".root","recreate")
g_mhsig_100_nom.SetName("mhsig100_nom")
g_mhsig_50_nom.SetName("mhsig50_nom")
g_mhsig_best_nom.SetName("mhsigbest_nom")
g_mhsig_100_notms.SetName("mhsig100_notms")
g_mhsig_50_notms.SetName("mhsig50_notms")
g_mhsig_best_notms.SetName("mhsigbest_notms")

g_mhsig_100_nom.Write()
g_mhsig_50_nom.Write()
g_mhsig_best_nom.Write()
g_mhsig_100_notms.Write()
g_mhsig_50_notms.Write()
g_mhsig_best_notms.Write()

myout.Close()
      
c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,336.,15.)
h2.SetTitle("Mass Ordering Sensitivity")
h2.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
g_mhsig_100_nom.Draw("L same")
g_mhsig_100_notms.Draw("L same")

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.AddText("100% of #delta_{CP} values")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)      
t1.Draw("same")

lm1 = ROOT.TLegend(0.52,0.75,0.89,0.89)
lm1.AddEntry(g_mhsig_100_nom,"Reference Near Detector","L")
lm1.AddEntry(g_mhsig_100_notms,"ND-LAr (no spectrometer)","L")      
lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

line3 = ROOT.TLine(0.0,5.,336.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot_v4/exposures/mh_exp_ndnospect_100_"+hier+".eps"
outname2 = "plot_v4/exposures/mh_exp_ndnospect_100_"+hier+".png"

c2.SaveAs(outname)
c2.SaveAs(outname2)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.0,100.,15.)
h3.SetTitle("Mass Ordering Sensitivity")
h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h3.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.3)
h3.GetYaxis().CenterTitle()
c3.Modified()
g_mhsig_best_nom.Draw("L same")
g_mhsig_best_notms.Draw("L same")

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.AddText("#delta_{CP} = -#pi/2") 
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)      
t1.Draw("same")

lm1 = ROOT.TLegend(0.52,0.75,0.89,0.89)
lm1.AddEntry(g_mhsig_100_nom,"Reference Near Detector","L")
lm1.AddEntry(g_mhsig_100_notms,"ND-LAr (no spectrometer)","L")      
lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

line3 = ROOT.TLine(0.0,5.,100.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot_v4/exposures/mh_exp_ndnospect_best_"+hier+".eps"
outname2 = "plot_v4/exposures/mh_exp_ndnospect_best_"+hier+".png"
c3.SaveAs(outname)
c3.SaveAs(outname2)
           

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0,0.0,100.,15.)
h4.SetTitle("Mass Ordering Sensitivity")
h4.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h4.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h4.GetYaxis().SetTitleOffset(1.3)
h4.GetYaxis().CenterTitle()
c4.Modified()
g_mhsig_50_nom.Draw("L same")
g_mhsig_50_notms.Draw("L same")

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.AddText("50% of #delta_{CP} values")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)      
t1.Draw("same")

lm1 = ROOT.TLegend(0.52,0.75,0.89,0.89)
lm1.AddEntry(g_mhsig_100_nom,"Reference Near Detector","L")
lm1.AddEntry(g_mhsig_100_notms,"ND-LAr (no spectrometer)","L")      
lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

line3 = ROOT.TLine(0.0,5.,100.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot_v4/exposures/mh_exp_ndnospect_50_"+hier+".eps"
outname2 = "plot_v4/exposures/mh_exp_ndnospect_50_"+hier+".png"
c4.SaveAs(outname)
c4.SaveAs(outname2)
