#!/usr/bin/env python

import sys
import math
import ROOT
from array import array
import ctypes

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
      xup = ctypes.c_double(-9.9) #ROOT.Double(-9.9)
      yup = ctypes.c_double(-9.9) #ROOT.Double(-9.9)
      xlo = ctypes.c_double(-9.9) #ROOT.Double(-9.9)
      ylo = ctypes.c_double(-9.9) #ROOT.Double(-9.9)
      while i<n:
          up.GetPoint(i,xup,yup);
          down.GetPoint(n-i-1,xlo,ylo);
          diffgraph.SetPoint(i,xup,yup);
          diffgraph.SetPoint(n+i,xlo,ylo);
          i += 1
      return diffgraph;


f1 = ROOT.TFile("root_v4/throws/graphs_final.root")
g1 = f1.Get("dcp_th23upper_th13_7yr")
g1nopen = f1.Get("dcp_th23upper_np_7yr")
g2 = f1.Get("dcp_th23upper_th13_10yr")
g2nopen = f1.Get("dcp_th23upper_np_10yr")
g3 = f1.Get("dcp_th23upper_th13_15yr")
g3nopen = f1.Get("dcp_th23upper_np_15yr")

r1s =ROOT.TGraphSmooth("normal")
r1 = r1s.SmoothKern(g1,"normal",0.25)
r2s =ROOT.TGraphSmooth("normal")
r2 = r2s.SmoothKern(g2,"normal",0.25)
r3s =ROOT.TGraphSmooth("normal")
r3 = r3s.SmoothKern(g3,"normal",0.25)

r1s_nopen =ROOT.TGraphSmooth("normal")
r1nopen = r1s_nopen.SmoothKern(g1nopen,"normal",0.25)
r2s_nopen =ROOT.TGraphSmooth("normal")
r2nopen = r2s_nopen.SmoothKern(g2nopen,"normal",0.25)
r3s_nopen =ROOT.TGraphSmooth("normal")
r3nopen = r3s_nopen.SmoothKern(g3nopen,"normal",0.25)


r1.SetLineWidth(5)
r2.SetLineWidth(5)
r3.SetLineWidth(5)
r1nopen.SetLineWidth(5)
r2nopen.SetLineWidth(5)
r3nopen.SetLineWidth(5)

r1nopen.SetLineStyle(2)
r2nopen.SetLineStyle(2)
r3nopen.SetLineStyle(2)

graph_range1 = filldiff(r1nopen,r1)
graph_range2 = filldiff(r2nopen,r2)
graph_range3 = filldiff(r3nopen,r3)

graph_range1.SetFillStyle(1001)
graph_range2.SetFillStyle(1001)
graph_range3.SetFillStyle(1001)

graph_range1.SetLineColor(0)
graph_range2.SetLineColor(0)
graph_range3.SetLineColor(0)

graph_range1.SetFillColor(ROOT.kBlue-7)
graph_range2.SetFillColor(ROOT.kOrange-3)
graph_range3.SetFillColor(ROOT.kGreen-7)


c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.0,0.0,1.0,45.0)
h1.SetTitle("")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#delta_{CP} Resolution (degrees)")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_range1.Draw("cf,same")
graph_range2.Draw("cf,same")
graph_range3.Draw("cf,same")
r1.Draw("c,same")
r2.Draw("c,same")
r3.Draw("c,same")
r1nopen.Draw("c,same")
r2nopen.Draw("c,same")
r3nopen.Draw("c,same")

ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.55,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
#t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.6,0.73,0.89,0.89)
#l1.AddEntry(graph_range1,"7 years (staged)","F")
#l1.AddEntry(graph_range2,"10 years (staged)","F")
#l1.AddEntry(graph_range3,"15 years (staged)","F")
l1.AddEntry(graph_range1,"336 kt-MW-years", "F")
l1.AddEntry(graph_range2,"624 kt-MW-years", "F")
l1.AddEntry(graph_range3,"1104 kt-MW-years", "F")
l1.AddEntry(r1,"Nominal Analysis","L")
l1.AddEntry(r1nopen,"#theta_{13} unconstrained","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")
ROOT.gPad.RedrawAxis()

outname = "plot_v4/res/dcpresvdcp_smooth_v4_exp.eps"
outname2 = "plot_v4/res/dcpresvdcp_smooth_v4_exp.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

