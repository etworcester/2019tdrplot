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

def fix (hist):

    nx = hist.GetNbinsX()
    xlo = hist.GetXaxis().GetBinLowEdge(1)
    xhi = hist.GetXaxis().GetBinLowEdge(nx) + hist.GetXaxis().GetBinWidth(nx)
    ny = hist.GetNbinsY()
    i = 1
    newy = []
    while i < ny+1:
        val = hist.GetYaxis().GetBinLowEdge(i)
        newy.append(math.sin(2*val)*math.sin(2*val))
        i+=1
    val = hist.GetYaxis().GetBinLowEdge(ny) + hist.GetYaxis().GetBinWidth(ny)
    newy.append(math.sin(2*val)*math.sin(2*val))
    newy = array('d',newy)
    newh = ROOT.TH2D("newh","title",nx,xlo,xhi,ny,newy)

    j = 1
    while j < ny+1:
        i = 1
        while i < nx+1:
            val = hist.GetBinContent(hist.GetBin(i,j))
            newh.SetBinContent(newh.GetBin(i,j), val)
            i += 1
        j += 1
    return newh

f1 = ROOT.TFile("root_v4/bubbles/asimov_deltapi-th13_ndfd7year_allsyst_nopen_asimov0_hie1.root")
rdcpz1 = f1.Get("deltapi_th13")

f2 = ROOT.TFile("root_v4/bubbles/asimov_deltapi-th13_ndfd10year_allsyst_nopen_asimov0_hie1.root")
rdcpz2 = f2.Get("deltapi_th13")

f3 = ROOT.TFile("root_v4/bubbles/asimov_deltapi-th13_ndfd15year_allsyst_nopen_asimov0_hie1.root")
rdcpz3 = f3.Get("deltapi_th13")

nufit = ROOT.TFile("root_v3/nufit_dcpvq13_contours_rotate.root")
h_no = nufit.Get("h_no")

dcpz1 = fix(rdcpz1)

dcpz2 = fix(rdcpz2)

dcpz3 = fix(rdcpz3)

dcpz1.SetLineWidth(3)
dcpz2.SetLineWidth(3)
dcpz3.SetLineWidth(3)

dcpz1.SetLineColor(ROOT.kBlue-7)

dcpz2.SetLineColor(ROOT.kOrange-3)

dcpz3.SetLineColor(ROOT.kGreen+2)

dcpz1.SetContour(1)
dcpz1.SetContourLevel(0,4.61)
dcpz2.SetContour(1)
dcpz2.SetContourLevel(0,4.61)
dcpz3.SetContour(1)
dcpz3.SetContourLevel(0,4.61)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1., 0.078, 1., 0.125)
h1.GetYaxis().SetTitle("sin^{2}2#theta_{13}")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
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

dcpz1.Draw("cont3 same")
dcpz2.Draw("cont3 same")
dcpz3.Draw("cont3 same")

dcptrue = (215.*math.pi/180 - 2*math.pi)/math.pi
print dcptrue
s1 = ROOT.TMarker(dcptrue,0.088,29)
s1.Draw("same")

t1 = ROOT.TPaveText(0.5,0.72,0.89,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("90% C.L. (2 d.o.f.)")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.5,0.55,0.89,0.72)
l1.AddEntry(dcpz1,"7 years (staged)","L")
l1.AddEntry(dcpz2,"10 years (staged)","L")
l1.AddEntry(dcpz3,"15 years (staged)","L")
l1.AddEntry(box1, "NuFIT 4.0 90% C.L.", "F")
l1.AddEntry(s1, "True Value","P")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")
ROOT.gPad.RedrawAxis()

outname = "plot_v4/bubbles/bubbles_q13_2019_v4_allislands.eps"
outname2 = "plot_v4/bubbles/bubbles_q13_2019_v4_allislands.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

