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

f1 =  ROOT.TFile("root_v4/throws/graphs_final.root")
#f1_7 = ROOT.TFile("root_v4/sens_error_bands/final_th13_7yr_BAND.root")
#f1_10 = ROOT.TFile("root_v4/sens_error_bands/final_th13_10yr_BAND.root")
#f1_15 = ROOT.TFile("root_v4/sens_error_bands/final_th13_15yr_BAND.root")


#graph_7yr = f1_7.Get("oct_throws_1sigma")
#graph_10yr = f1_10.Get("oct_throws_1sigma")
#graph_15yr = f1_15.Get("oct_throws_1sigma")

graph_7yr = f1.Get("octant_1sigma_th13_7yr")
graph_10yr = f1.Get("octant_1sigma_th13_10yr")
graph_15yr = f1.Get("octant_1sigma_th13_15yr")

c3 = ROOT.TCanvas("c3","c3",800,800)
h3 = c3.DrawFrame(0.41, 0.0, 0.59, 10.0)
h3.SetTitle("")
h3.GetXaxis().SetTitle("sin^{2}#theta_{23}")
#h3.GetYaxis().SetTitleOffset(1.)
h3.GetXaxis().SetTitleOffset(1.15)
h3.GetYaxis().CenterTitle()
h3.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")

graph_7yr.SetFillColorAlpha(ROOT.kBlue-7,0.5)
graph_7yr.SetLineColor(ROOT.kBlue-7)
#graph_7yr.Draw("l e3 same")

graph_10yr.SetFillColorAlpha(ROOT.kOrange-3,0.5)
graph_10yr.SetLineColor(ROOT.kOrange-3)
graph_10yr.SetLineWidth(3)
graph_10yr.Draw("l e3 same")

graph_15yr.SetFillColorAlpha(ROOT.kGreen-7,0.5)
graph_15yr.SetLineColor(ROOT.kGreen-7)
#graph_15yr.Draw("l e3 same")

null = ROOT.TObject()
gdum = graph_10yr.Clone()
gdum.SetLineColor(0)

leg1 = ROOT.TLegend(0.5,0.7,0.87,0.89)
#leg1.AddEntry(graph_7yr,"7 years (staged)","F")
#leg1.AddEntry(graph_15yr,"15 years (staged)","F")
leg1.AddEntry(graph_10yr,"Median of Throws","L")
leg1.AddEntry(gdum, "1#sigma: Variations of","F")
leg1.AddEntry(null,"statistics, systematics,","")
leg1.AddEntry(null,"and oscillation parameters","")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.Draw()

t1 = ROOT.TPaveText(0.22,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("624 kt-MW-years")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLine(0.41,3.,0.59,3.0)
l1.SetLineWidth(3)
l1.SetLineStyle(2)
l1.Draw()

l2 = ROOT.TLine(0.41,5.,0.59,5.0)
l2.SetLineWidth(3)
l2.SetLineStyle(2)
l2.Draw()

ROOT.gPad.RedrawAxis()

c3.SaveAs("plot_v4/octant/octant_no_2019_10yronly_v4_exp.png")
c3.SaveAs("plot_v4/octant/octant_no_2019_10yronly_v4_exp.eps")



    
