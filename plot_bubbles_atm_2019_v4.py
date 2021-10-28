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

try:
    sys.argv[1]
except:
    alt = 0
else:
    alt = int(sys.argv[1])

f1 = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd7year_allsyst_th13_ssth23:0.58_hie1.root")
dcpz1 = f1.Get("ssth23_dmsq32")

f2 = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd10year_allsyst_th13_ssth23:0.58_hie1.root")
dcpz2 = f2.Get("ssth23_dmsq32")

f3 = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd15year_allsyst_th13_ssth23:0.58_hie1.root")
dcpz3 = f3.Get("ssth23_dmsq32")

f1nopen = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd7year_allsyst_nopen_ssth23:0.58_hie1.root")
dcpz1nopen = f1nopen.Get("ssth23_dmsq32")

f2nopen = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd10year_allsyst_nopen_ssth23:0.58_hie1.root")
dcpz2nopen = f2nopen.Get("ssth23_dmsq32")

f3nopen = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd15year_allsyst_nopen_ssth23:0.58_hie1.root")
dcpz3nopen = f3nopen.Get("ssth23_dmsq32")

f1a = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd7year_allsyst_th13_ssth23:0.5_hie1.root")
dcpz1a = f1a.Get("ssth23_dmsq32")

f2a = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd10year_allsyst_th13_ssth23:0.5_hie1.root")
dcpz2a = f2a.Get("ssth23_dmsq32")

f3a = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd15year_allsyst_th13_ssth23:0.5_hie1.root")
dcpz3a = f3a.Get("ssth23_dmsq32")

f1b = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd7year_allsyst_th13_ssth23:0.42_hie1.root")
dcpz1b = f1b.Get("ssth23_dmsq32")

f2b = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd10year_allsyst_th13_ssth23:0.42_hie1.root")
dcpz2b = f2b.Get("ssth23_dmsq32")

f3b = ROOT.TFile("root_v4/bubbles/asimov_ssth23-dmsq32_ndfd15year_allsyst_th13_ssth23:0.42_hie1.root")
dcpz3b = f3b.Get("ssth23_dmsq32")

    

nufit = ROOT.TFile("root_v3/nufit_dmsqvq23_contours.root")
h_no = nufit.Get("h_no")

dcpz1.SetLineWidth(3)
dcpz2.SetLineWidth(3)
dcpz3.SetLineWidth(3)

dcpz1nopen.SetLineWidth(3)
dcpz2nopen.SetLineWidth(3)
dcpz3nopen.SetLineWidth(3)

dcpz1a.SetLineWidth(3)
dcpz2a.SetLineWidth(3)
dcpz3a.SetLineWidth(3)

dcpz1b.SetLineWidth(3)
dcpz2b.SetLineWidth(3)
dcpz3b.SetLineWidth(3)

dcpz1.SetLineColor(ROOT.kBlue-7)
dcpz2.SetLineColor(ROOT.kOrange-3)
dcpz3.SetLineColor(ROOT.kGreen+2)
dcpz1nopen.SetLineColor(ROOT.kBlue-7)
dcpz2nopen.SetLineColor(ROOT.kOrange-3)
dcpz3nopen.SetLineColor(ROOT.kGreen+2)
dcpz1a.SetLineColor(ROOT.kBlue-7)
dcpz2a.SetLineColor(ROOT.kOrange-3)
dcpz3a.SetLineColor(ROOT.kGreen+2)
dcpz1b.SetLineColor(ROOT.kBlue-7)
dcpz2b.SetLineColor(ROOT.kOrange-3)
dcpz3b.SetLineColor(ROOT.kGreen+2)

dcpz1.SetContour(1)
dcpz1.SetContourLevel(0,4.61)
dcpz2.SetContour(1)
dcpz2.SetContourLevel(0,4.61)
dcpz3.SetContour(1)
dcpz3.SetContourLevel(0,4.61)

dcpz1nopen.SetContour(1)
dcpz1nopen.SetContourLevel(0,4.61)
dcpz2nopen.SetContour(1)
dcpz2nopen.SetContourLevel(0,4.61)
dcpz3nopen.SetContour(1)
dcpz3nopen.SetContourLevel(0,4.61)

dcpz1a.SetContour(1)
dcpz1a.SetContourLevel(0,4.61)
dcpz2a.SetContour(1)
dcpz2a.SetContourLevel(0,4.61)
dcpz3a.SetContour(1)
dcpz3a.SetContourLevel(0,4.61)

dcpz1b.SetContour(1)
dcpz1b.SetContourLevel(0,4.61)
dcpz2b.SetContour(1)
dcpz2b.SetContourLevel(0,4.61)
dcpz3b.SetContour(1)
dcpz3b.SetContourLevel(0,4.61)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.35, 2.35, 0.65, 2.6)
h1.GetYaxis().SetTitle("#Deltam^{2}_{32} (eV^{2} #times 10^{-3})")
h1.GetXaxis().SetTitle("sin^{2}#theta_{23}")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().CenterTitle()
h1.GetYaxis().SetTitleOffset(1.7)
c1.Modified()

h_no.Draw("cont0 same")
h_no.SetContour(2)
h_no.SetContourLevel(0,0)
h_no.SetContourLevel(1,4.61)
colors = [ROOT.kYellow-7]
colors = array('i',colors)
ROOT.gStyle.SetPalette(1,colors)

#Not to plot, just for the legend
box1 = ROOT.TBox(41.1,-180,43.8,120)
box1.SetFillColor(ROOT.kYellow-7)
box1.SetLineColor(0)

if (alt==2):
    print("Drawing no-penalty contours")
    dcpz1nopen.Draw("cont3 same")
    dcpz2nopen.Draw("cont3 same")
    dcpz3nopen.Draw("cont3 same")
else:
    dcpz1.Draw("cont3 same")
    dcpz2.Draw("cont3 same")
    dcpz3.Draw("cont3 same")

s1 = ROOT.TMarker(0.58,2.451,29)
s1.Draw("same")
s2 = ROOT.TMarker(0.5,2.451,29)
s3 = ROOT.TMarker(0.42,2.451,29)

if (alt==1):
    print ("drawing alt contours")
    dcpz1a.Draw("cont3 same")
    dcpz2a.Draw("cont3 same")
    dcpz3a.Draw("cont3 same")
    s2.Draw("same")
    dcpz1b.Draw("cont3 same")
    dcpz2b.Draw("cont3 same")
    dcpz3b.Draw("cont3 same")
    s3.Draw("same")

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
if (alt==2):
    t1.AddText("sin^{2}2#theta_{13} = 0.088 unconstrained")
else:
    t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("90% C.L. (2 d.o.f.)")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.5,0.7,0.89,0.89)
#l1.AddEntry(dcpz1,"7 years (staged)","L")
#l1.AddEntry(dcpz2,"10 years (staged)","L")
#l1.AddEntry(dcpz3,"15 years (staged)","L")
l1.AddEntry(dcpz1,"336 kt-MW-years","L")
l1.AddEntry(dcpz2,"624 kt-MW-years","L")
l1.AddEntry(dcpz3,"1104 kt-MW-years","L")
l1.AddEntry(box1, "NuFIT 4.0 90% C.L.", "F")
l1.AddEntry(s1, "True Value","P")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")
ROOT.gPad.RedrawAxis()

if (alt ==2):
    outname = "plot_v4/bubbles/bubbles_atm_nopen_2019_v4_exp.eps"
    outname2 = "plot_v4/bubbles/bubbles_atm_nopen_2019_v4_exp.png"    
elif (alt == 1):
    outname = "plot_v4/bubbles/bubbles_atm_alt_2019_v4_exp.eps"
    outname2 = "plot_v4/bubbles/bubbles_atm_alt_2019_v4_exp.png"
else:
    outname = "plot_v4/bubbles/bubbles_atm_2019_v4_exp.eps"
    outname2 = "plot_v4/bubbles/bubbles_atm_2019_v4_exp.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

