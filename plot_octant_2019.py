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

def filldiff(up,down,mid):
      n = up.GetN()
      diffgraph = ROOT.TGraph(2*n)
      i = 0
      xup = ROOT.Double(-9.9)
      yup = ROOT.Double(-9.9)
      xlo = ROOT.Double(-9.9)
      ylo = ROOT.Double(-9.9)
      xmid = ROOT.Double(-9.9)
      ymid = ROOT.Double(-9.9)

      while i<n:
            up.GetPoint(i,xup,yup)
            mid.GetPoint(i,xmid,ymid)
            down.GetPoint(i,xlo,ylo)
            yval = max(yup,ymid)
            yval = max(yval,ylo)

            diffgraph.SetPoint(i,xup,yval)

            up.GetPoint(n-i-1,xup,yup)
            down.GetPoint(n-i-1,xlo,ylo)
            mid.GetPoint(n-i-1,xmid,ymid)
            yval = min(yup,ymid)
            yval = min(yval,ylo)
            diffgraph.SetPoint(n+i,xlo,yval)

            i += 1
      return diffgraph

f1_7 = ROOT.TFile("root_callum/octant_sens_ndfd_336kTMWyr_allsyst_th13_hie1_asimov0_v3.root")
f2_7 = ROOT.TFile("root_callum/octant_sens_ndfd_336kTMWyr_allsyst_th13_hie1_asimov10_v3.root")
f3_7 = ROOT.TFile("root_callum/octant_sens_ndfd_336kTMWyr_allsyst_th13_hie1_asimov11_v3.root")

f1_10 = ROOT.TFile("root_callum/octant_sens_ndfd_624kTMWyr_allsyst_th13_hie1_asimov0_v3.root")
f2_10 = ROOT.TFile("root_callum/octant_sens_ndfd_624kTMWyr_allsyst_th13_hie1_asimov10_v3.root")
f3_10 = ROOT.TFile("root_callum/octant_sens_ndfd_624kTMWyr_allsyst_th13_hie1_asimov11_v3.root")

f1_15 = ROOT.TFile("root_callum/octant_sens_ndfd_1104kTMWyr_allsyst_th13_hie1_asimov0_v3.root")
f2_15 = ROOT.TFile("root_callum/octant_sens_ndfd_1104kTMWyr_allsyst_th13_hie1_asimov10_v3.root")
f3_15 = ROOT.TFile("root_callum/octant_sens_ndfd_1104kTMWyr_allsyst_th13_hie1_asimov11_v3.root")

graph_7yr_asimov0 = f1_7.Get("sens_oct_nh") 
graph_7yr_asimov10 = f2_7.Get("sens_oct_nh") 
graph_7yr_asimov11 = f3_7.Get("sens_oct_nh") 
                    
graph_10yr_asimov0 = f1_10.Get("sens_oct_nh") 
graph_10yr_asimov10 = f2_10.Get("sens_oct_nh") 
graph_10yr_asimov11 = f3_10.Get("sens_oct_nh") 
                    
graph_15yr_asimov0 = f1_15.Get("sens_oct_nh") 
graph_15yr_asimov10 = f2_15.Get("sens_oct_nh") 
graph_15yr_asimov11 = f3_15.Get("sens_oct_nh") 

graph_diff_7yr = filldiff(graph_7yr_asimov0,graph_7yr_asimov10,graph_7yr_asimov11)
graph_diff_10yr = filldiff(graph_10yr_asimov0,graph_10yr_asimov10,graph_10yr_asimov11)
graph_diff_15yr = filldiff(graph_15yr_asimov0,graph_15yr_asimov10,graph_15yr_asimov11)

c3 = ROOT.TCanvas("c3","c3",800,800)
h3 = c3.DrawFrame(0.328, 0.0, 0.671, 10.0)
h3.SetTitle("")
h3.GetXaxis().SetTitle("sin^{2}#theta_{23}")
#h3.GetYaxis().SetTitleOffset(1.)
h3.GetXaxis().SetTitleOffset(1.15)
h3.GetYaxis().CenterTitle()
h3.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")

th23lo = 47.3*math.pi/180
lo = math.sin(th23lo)*math.sin(th23lo)
th23hi = 51.2 * math.pi/180
hi = math.sin(th23hi)*math.sin(th23hi)
b1 = ROOT.TBox(lo,0.0,hi,10.0)
b1.SetFillColor(ROOT.kYellow-4)
b1.SetLineColor(0)
b1.Draw("same")

graph_diff_7yr.SetFillColor(ROOT.kBlue-7)
graph_diff_7yr.SetLineColor(0)
graph_diff_7yr.Draw("Fsame")

graph_diff_10yr.SetFillColor(ROOT.kOrange-3)
graph_diff_10yr.SetLineColor(0)
graph_diff_10yr.Draw("Fsame")

graph_diff_15yr.SetFillColor(ROOT.kGreen-7)
graph_diff_15yr.SetLineColor(0)
graph_diff_15yr.Draw("Fsame")


leg1 = ROOT.TLegend(0.11,0.6,0.5,0.75)
leg1.AddEntry(graph_diff_7yr,"7 years (staged)","F")
leg1.AddEntry(graph_diff_10yr,"10 years (staged)","F")
leg1.AddEntry(graph_diff_15yr,"15 years (staged)","F")
leg1.AddEntry(b1,"NuFit 4.0 90% C.L.","f")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.Draw()

t1 = ROOT.TPaveText(0.11,0.75,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLine(0.328,3.,0.671,3.0)
l1.SetLineWidth(3)
l1.SetLineStyle(2)
l1.Draw()

l2 = ROOT.TLine(0.328,5.,0.671,5.0)
l2.SetLineWidth(3)
l2.SetLineStyle(2)
l2.Draw()

ROOT.gPad.RedrawAxis()

c3.SaveAs("plot/octant/octant_no_2019.png")
c3.SaveAs("plot/octant/octant_no_2019.eps")



    
