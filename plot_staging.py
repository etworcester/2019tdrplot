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


f1 = ROOT.TFile("root_v4/staging_convert_fastrampcomm.root")
g = f1.Get("g_exp")

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.,0.,120.0,5.0)
h1.SetTitle("Staging Conversion")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("Run Time (years)")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
g.Draw("l")
ROOT.gPad.RedrawAxis()

c1.SaveAs("plot_v4/staging_convert_fastrampcomm.png")
