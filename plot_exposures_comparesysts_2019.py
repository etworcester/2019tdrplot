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


explist = [0,1,5,10,30,50,100,200,336,450,624,800,1104,1300,1500]

cpvlist75_cdr = [0]
cpvlist50_cdr = [0]
cpvlistbest_cdr = [0]

cpvlist75_cdr_1pc = [0]
cpvlist50_cdr_1pc = [0]
cpvlistbest_cdr_1pc = [0]

for myexp in explist:
      if (myexp==0):
            continue
      filename = "root_cdrsysts/cpv_sens_aset0_exp"+str(myexp)+".root"
      f1 = ROOT.TFile(filename)
      cpvgraph = f1.Get("sens_cpv_nh")
      nvals = cpvgraph.GetN()
      cut75 = int(0.25*nvals)
      cut50 = int(0.5*nvals)
      cutbest = int(0.25*nvals)
      this_cpv_vals = [ROOT.Double(0.0)]*nvals
      this_cpv_vals = array('d',this_cpv_vals)
      this_cpv_vals = cpvgraph.GetY()

      i = 0
      cpv_vals = []
      while i < nvals:
            cpv_vals.append(this_cpv_vals[i])
            i += 1

      cpvsig_75_cdr = sorted(cpv_vals)[cut75]
      cpvsig_50_cdr = sorted(cpv_vals)[cut50]
      cpvlist75_cdr.append(cpvsig_75_cdr)
      cpvlist50_cdr.append(cpvsig_50_cdr)
      cpvlistbest_cdr.append(cpv_vals[cutbest])
      f1.Close()

      filename = "root_cdrsysts/cpv_sens_aset0_exp"+str(myexp)+"_1pc.root"
      f1 = ROOT.TFile(filename)
      cpvgraph = f1.Get("sens_cpv_nh")
      nvals = cpvgraph.GetN()
      cut75 = int(0.25*nvals)
      cut50 = int(0.5*nvals)
      cutbest = int(0.25*nvals)
      this_cpv_vals = [ROOT.Double(0.0)]*nvals
      this_cpv_vals = array('d',this_cpv_vals)
      this_cpv_vals = cpvgraph.GetY()

      i = 0
      cpv_vals = []
      while i < nvals:
            cpv_vals.append(this_cpv_vals[i])
            i += 1

      cpvsig_75_cdr = sorted(cpv_vals)[cut75]
      cpvsig_50_cdr = sorted(cpv_vals)[cut50]
      cpvlist75_cdr_1pc.append(cpvsig_75_cdr)
      cpvlist50_cdr_1pc.append(cpvsig_50_cdr)
      cpvlistbest_cdr_1pc.append(cpv_vals[cutbest])
      f1.Close()
      
      
n = len(explist)
explist = array('d',explist)
cpvlist75_cdr = array('d',cpvlist75_cdr)
cpvlist50_cdr = array('d',cpvlist50_cdr)
cpvlistbest_cdr = array('d',cpvlistbest_cdr)

cpvlist75_cdr_1pc = array('d',cpvlist75_cdr_1pc)
cpvlist50_cdr_1pc = array('d',cpvlist50_cdr_1pc)
cpvlistbest_cdr_1pc = array('d',cpvlistbest_cdr_1pc)

g_cpvsig75_cdr = ROOT.TGraph(n,explist,cpvlist75_cdr)
g_cpvsig50_cdr = ROOT.TGraph(n,explist,cpvlist50_cdr)
g_cpvsigbest_cdr = ROOT.TGraph(n,explist,cpvlistbest_cdr)

g_cpvsig75_cdr_1pc = ROOT.TGraph(n,explist,cpvlist75_cdr_1pc)
g_cpvsig50_cdr_1pc = ROOT.TGraph(n,explist,cpvlist50_cdr_1pc)
g_cpvsigbest_cdr_1pc = ROOT.TGraph(n,explist,cpvlistbest_cdr_1pc)

myout = ROOT.TFile("root/exposure_graphs_cdrsysts.root","recreate")
g_cpvsig50_cdr_1pc.SetName("cpvsig50_cdr_1pc")
g_cpvsig50_cdr.SetName("cpvsig50_cdr")
g_cpvsig75_cdr_1pc.SetName("cpvsig75_cdr_1pc")
g_cpvsig75_cdr.SetName("cpvsig75_cdr")
g_cpvsigbest_cdr_1pc.SetName("cpvsigbest_cdr_1pc")
g_cpvsigbest_cdr.SetName("cpvsigbest_cdr")

g_cpvsig50_cdr_1pc.Write()
g_cpvsig50_cdr.Write()
g_cpvsig75_cdr_1pc.Write()
g_cpvsig75_cdr.Write()
g_cpvsigbest_cdr_1pc.Write()
g_cpvsigbest_cdr.Write()
myout.Close()

fexp = ROOT.TFile("root/exposure_graphs_nh.root")
g_cpvsig75_hi = fexp.Get("cpvsig75_th13pen")
g_cpvsig50_hi = fexp.Get("cpvsig50_th13pen")
g_cpvsigbest_hi = fexp.Get("cpvsigbest_th13pen")

g_cpvsig75_hi.SetLineWidth(4)
g_cpvsig75_hi.SetLineColor(ROOT.kCyan+2)
g_cpvsig50_hi.SetLineWidth(4)
g_cpvsig50_hi.SetLineColor(ROOT.kCyan-7)
g_cpvsigbest_hi.SetLineWidth(4)
g_cpvsigbest_hi.SetLineColor(ROOT.kPink-3)

g_cpvsig75_cdr.SetLineWidth(4)
g_cpvsig75_cdr.SetLineStyle(2)
g_cpvsig75_cdr.SetLineColor(ROOT.kCyan+2)
g_cpvsig50_cdr.SetLineWidth(4)
g_cpvsig50_cdr.SetLineStyle(2)
g_cpvsig50_cdr.SetLineColor(ROOT.kCyan-7)
g_cpvsigbest_cdr.SetLineWidth(4)
g_cpvsigbest_cdr.SetLineStyle(2)
g_cpvsigbest_cdr.SetLineColor(ROOT.kPink-3)

g_cpvsig75_cdr_1pc.SetLineWidth(4)
g_cpvsig75_cdr_1pc.SetLineStyle(3)
g_cpvsig75_cdr_1pc.SetLineColor(ROOT.kCyan+2)
g_cpvsig50_cdr_1pc.SetLineWidth(4)
g_cpvsig50_cdr_1pc.SetLineStyle(3)
g_cpvsig50_cdr_1pc.SetLineColor(ROOT.kCyan-7)
g_cpvsigbest_cdr_1pc.SetLineWidth(4)
g_cpvsigbest_cdr_1pc.SetLineStyle(3)
g_cpvsigbest_cdr_1pc.SetLineColor(ROOT.kPink-3)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1500.0,13.)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
g_cpvsig75_hi.Draw("L same")
g_cpvsig75_cdr.Draw("L same")
g_cpvsig75_cdr_1pc.Draw("L same")

g_cpvsig50_hi.Draw("L same")
g_cpvsig50_cdr.Draw("L same")
g_cpvsig50_cdr_1pc.Draw("L same")

g_cpvsigbest_hi.Draw("L same")
g_cpvsigbest_cdr.Draw("L same")
g_cpvsigbest_cdr_1pc.Draw("L same")

t1 = ROOT.TPaveText(0.16,0.72,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

nom_dum = g_cpvsigbest_hi.Clone()
nom_dum.SetLineColor(ROOT.kBlack)
cdr_dum = g_cpvsigbest_cdr.Clone()
cdr_dum.SetLineColor(ROOT.kBlack)
cdr1_dum = g_cpvsigbest_cdr_1pc.Clone()
cdr1_dum.SetLineColor(ROOT.kBlack)

l1 = ROOT.TLegend(0.55,0.7,0.89,0.89)
l1.AddEntry(g_cpvsigbest_hi, "#delta_{CP} = -#pi/2", "L")
l1.AddEntry(g_cpvsig50_hi, "50% of #delta_{CP} values","L")
l1.AddEntry(g_cpvsig75_hi, "75% of #delta_{CP} values","L")
l1.AddEntry(nom_dum,"Nominal Analysis","L")
l1.AddEntry(cdr1_dum,"1%/5% Systematics","L")
l1.AddEntry(cdr_dum,"2%/5% Systematics","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,1500.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1500.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(10.,3.1,115.,3.7)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetFillStyle(0)
t3sig.SetBorderSize(0)
#t3sig.Draw("same")

t5sig = ROOT.TPaveText(10.,5.1,115.,5.7)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetFillStyle(0)
t5sig.SetBorderSize(0)
#t5sig.Draw("same")

outname = "plot/exposures/cpv_exp_comparesysts_2019.png"
c1.SaveAs(outname)

