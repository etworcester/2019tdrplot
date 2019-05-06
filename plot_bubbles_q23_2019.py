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

pilist = ["0", "-0.5pi", "+0.5pi"]
ssth23list = ["0.42", "0.5", "0.58"]
list7yr = []
for pival in pilist:
    for ssth23 in ssth23list:
        f = ROOT.TFile("root_callum/asimov_deltapi-ssth23_ndfd7year_allsyst_th13_deltapi:"+pival+",ssth23:"+ssth23+"_hie1.root")
        h = f.Get("deltapi_ssth23")
        hc = h.Clone()
        hc.SetDirectory(0)
        list7yr.append(hc)
        f.Close()

list10yr = []
for pival in pilist:
    for ssth23 in ssth23list:
        f = ROOT.TFile("root_callum/asimov_deltapi-ssth23_ndfd10year_allsyst_th13_deltapi:"+pival+",ssth23:"+ssth23+"_hie1.root")
        h = f.Get("deltapi_ssth23")
        hc = h.Clone()
        hc.SetDirectory(0)
        list10yr.append(hc)
        f.Close()

list15yr = []
for pival in pilist:
    for ssth23 in ssth23list:
        f = ROOT.TFile("root_callum/asimov_deltapi-ssth23_ndfd15year_allsyst_th13_deltapi:"+pival+",ssth23:"+ssth23+"_hie1.root")
        h = f.Get("deltapi_ssth23")
        hc = h.Clone()
        hc.SetDirectory(0)
        list15yr.append(hc)
    

nufit = ROOT.TFile("root/nufit_dcpvq23_contours_rotate.root")
h_no = nufit.Get("h_no")

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.,0.35,1.,0.75)
h1.GetYaxis().SetTitle("sin^{2}#theta_{23}")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetYaxis().SetTitleOffset(1.7)
h1.GetXaxis().CenterTitle()
h1.GetYaxis().CenterTitle()
c1.Modified()

#Not to plot, just for the legend
box1 = ROOT.TBox(41.1,-180,43.8,120)
box1.SetFillColor(ROOT.kYellow-7)
box1.SetLineColor(0)

t1 = ROOT.TPaveText(0.16,0.75,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("90% C.L. (2 d.o.f.)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

h_no.Draw("cont0 same")
h_no.SetContour(2)
h_no.SetContourLevel(0,0)
h_no.SetContourLevel(1,4.61)
colors = [ROOT.kYellow-7]
colors = array('i',colors)
ROOT.gStyle.SetPalette(1,colors)

for plot in list7yr:
    plot.SetContour(1)
    plot.SetContourLevel(0,4.61)
    plot.SetLineWidth(3)
    plot.SetLineColor(ROOT.kGreen-7)
    plot.Draw("cont3 same")

for plot in list10yr:
    plot.SetContour(1)
    plot.SetContourLevel(0,4.61)
    plot.SetLineWidth(3)
    plot.SetLineColor(ROOT.kOrange-3)
    plot.Draw("cont3 same")

for plot in list15yr:
    plot.SetContour(1)
    plot.SetContourLevel(0,4.61)
    plot.SetLineWidth(3)
    plot.SetLineColor(ROOT.kBlue-7)
    plot.Draw("cont3 same")

s1 = ROOT.TMarker(-0.5,0.5,29)
s2 = ROOT.TMarker(0,0.5,29)
s3 = ROOT.TMarker(0.5,0.5,29)
s4 = ROOT.TMarker(-0.5,0.42,29)
s5 = ROOT.TMarker(0,0.42,29)
s6 = ROOT.TMarker(0.5,0.42,29)
s7 = ROOT.TMarker(-0.5,0.58,29)
s8 = ROOT.TMarker(0,0.58,29)
s9 = ROOT.TMarker(0.5,0.58,29)
s1.Draw("same")
s2.Draw("same")
s3.Draw("same")
s4.Draw("same")
s5.Draw("same")
s6.Draw("same")
s7.Draw("same")
s8.Draw("same")
s9.Draw("same")
    
l1 = ROOT.TLegend(0.6,0.7,0.89,0.89)
l1.AddEntry(list7yr[0],"7 years (staged)","L")
l1.AddEntry(list10yr[0],"10 years (staged)","L")
l1.AddEntry(list15yr[0],"15 years (staged)","L")
l1.AddEntry(box1, "NuFit 4.0 90% C.L.", "F")
l1.AddEntry(s1, "\"True\" Value","P")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

ROOT.gPad.RedrawAxis()

outname = "plot/bubbles/bubbles_q23_2019.eps"
outname2 = "plot/bubbles/bubbles_q23_2019.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)
