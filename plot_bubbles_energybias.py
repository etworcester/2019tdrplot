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

f = ROOT.TFile("root_cris/nominal_EDepsRec_ssth23_dmsq32NHscaled_fd7year_ndconstraint_allsyst_nopen_hie1.root")
hnom = f.Get("ssth23_dmsq32NHscaled")

f2 = ROOT.TFile("root_cris/missingProtonEnergy_EDepsRec_ssth23_dmsq32NHscaled_fd7year_ndconstraint_allsyst_nopen_hie1.root")
hbias = f2.Get("ssth23_dmsq32NHscaled")

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.35,2.35,0.65,2.55)
h1.GetXaxis().SetTitle("sin^{2}#theta_{23}")
h1.GetYaxis().SetTitle("#Deltam^{2}_{32} (eV^{2} x 10^{-3})")
h1.GetYaxis().SetTitleOffset(1.7)
h1.GetXaxis().CenterTitle()
h1.GetYaxis().CenterTitle()
c1.Modified()


t1 = ROOT.TPaveText(0.16,0.65,0.55,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 unconstrained")
t1.AddText("90% C.L. (2 d.o.f.)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

hnom.SetContour(1)
hnom.SetContourLevel(0,4.61)
hnom.SetLineWidth(3)
hnom.SetLineColor(ROOT.kBlue-7)
hnom.SetLineStyle(3)
hnom.Draw("cont3 same")

hbias.SetContour(1)
hbias.SetContourLevel(0,4.61)
hbias.SetLineWidth(3)
hbias.SetLineColor(ROOT.kBlue-7)
hbias.SetFillColor(ROOT.kBlue-7)
hbias.SetFillStyle(1001)
hbias.Draw("cont same")
hbias.Draw("cont3 same")

s1 = ROOT.TMarker(0.58,2.45,29)
s1.Draw("same")

hdum = hnom.Clone()
hdum.SetLineColor(ROOT.kBlack)
hbias_dum = hbias.Clone()
hbias_dum.SetFillColorAlpha(ROOT.kBlack,0.25)
hbias_dum.SetLineColor(0)

null = ROOT.TObject()
l1 = ROOT.TLegend(0.55,0.63,0.89,0.89)
l1.AddEntry(hbias,"7 years (staged)","F")
l1.AddEntry(hbias,"7 years (staged)","F")
l1.AddEntry(hbias,"7 years (staged)","F")
l1.AddEntry(hdum,"Nominal Fit","L")
l1.AddEntry(hbias_dum,"On-axis Only Example:","F")
l1.AddEntry(null,"Shifted visible energy","")
l1.AddEntry(s1, "\"True\" Value","P")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

ROOT.gPad.RedrawAxis()

outname = "plot/bubbles/bubbles_energybias.eps"
outname2 = "plot/bubbles/bubbles_enerbybias.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)
