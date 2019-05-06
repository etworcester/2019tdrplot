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

specfile_cafana = ROOT.TFile("root/spec_hist.root")
specfile_globes = ROOT.TFile("/Users/etw/Documents/DUNE/work/lblpwgtools/code/plot/root/globes_numu_unosc_tdrbeam.root")

#Appearance FHC
h = specfile_cafana.Get("numu_fhc_unosc_sig")
h.Rebin()
s = h.Clone()
s.Scale(0.95)
s.SetLineStyle(2)

g = specfile_globes.Get("h")
g.SetLineColor(ROOT.kRed)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,2500.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)

h.Draw("same")
g.Draw("same")
s.Draw("same")

c1.SaveAs("plot/checknorm_globes_cafana.png")
