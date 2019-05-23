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

def filldiff(up,down):
      n = up.GetN()
      diffgraph = ROOT.TGraph(2*n);
      i = 0
      xup = ROOT.Double(-9.9)
      yup = ROOT.Double(-9.9)
      xlo = ROOT.Double(-9.9)
      ylo = ROOT.Double(-9.9)
      while i<n:
          up.GetPoint(i,xup,yup);
          down.GetPoint(n-i-1,xlo,ylo);
          diffgraph.SetPoint(i,xup,yup);
          diffgraph.SetPoint(n+i,xlo,ylo);
          i += 1
      return diffgraph;

f1 = ROOT.TFile("root_callum/cpv_sens_ndfd_624kTMWyr_allsyst_th13_hie1_v3.root")
anom = f1.Get("sens_cpv_nh")

f2 = ROOT.TFile("root_callum/cpv_sens_fd_624kTMWyr_nosyst_th13_hie1_asimov0_v3.root")
anosyst = f2.Get("sens_cpv_nh")

f3 = ROOT.TFile("root_cdrsysts/cpv_sens_aset0_exp624.root")
acdr = f3.Get("sens_cpv_nh")

f4 = ROOT.TFile("root_cdrsysts/cpv_sens_aset0_exp624_1pc.root")
acdr_1pc = f4.Get("sens_cpv_nh")

f5 = ROOT.TFile("root_cdrsysts/cpv_sens_aset0_exp624_3pc.root")
acdr_3pc = f5.Get("sens_cpv_nh")

band = filldiff(acdr_1pc,acdr_3pc)
band.SetLineColor(0)
band.SetFillStyle(1001)
band.SetFillColorAlpha(ROOT.kOrange-4,0.5)

anom.SetLineWidth(4)
anom.SetLineColor(ROOT.kOrange-3)

anosyst.SetLineWidth(4)
anosyst.SetLineColor(ROOT.kOrange+3)

acdr.SetLineWidth(4)
acdr.SetLineColor(ROOT.kOrange-3)
acdr.SetLineStyle(2)

acdr_1pc.SetLineWidth(4)
acdr_1pc.SetLineColor(ROOT.kOrange-3)
acdr_1pc.SetLineStyle(3)

acdr_3pc.SetLineWidth(4)
acdr_3pc.SetLineColor(ROOT.kOrange-3)
acdr_3pc.SetLineStyle(4)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.0,0.0,1.0,10.5)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
band.Draw("Fsame")
anom.Draw("same")
anosyst.Draw("same")
acdr.Draw("same")
#acdr_1pc.Draw("same")
#acdr_3pc.Draw("same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("10 years (staged)")      
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

null = ROOT.TObject()
l1 = ROOT.TLegend(0.52,0.72,0.89,0.89)
l1.AddEntry(anosyst,"No systematics", "L")
l1.AddEntry(anom,"TDR Nominal:", "L")
l1.AddEntry(null,"All Systematics","")
#l1.AddEntry(acdr_1pc,"5% #oplus 1% Norm. Syst.","L")
l1.AddEntry(acdr,"CDR-Style Nominal:","L")
l1.AddEntry(null,"5% #oplus 2% Norm. Unc.","")
#l1.AddEntry(acdr_3pc,"5% #oplus 3% Norm. Syst.","L")
l1.AddEntry(band,"5% #oplus 1-3% Norm. Unc.","F")
l1.SetBorderSize(0)
l1.SetFillStyle(0)

line1 = ROOT.TLine(-1.0,3.,1.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(-1.0,5.,1.0,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(-0.05,3.1,0.05,3.5)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetBorderSize(0)
#t3sig.Draw("same")

t5sig = ROOT.TPaveText(-0.05,5.1,0.05,5.5)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
#t5sig.Draw("same")

l1.SetFillColor(0)
l1.Draw("same")
outname = "plot/cpv/cpv_cdrsyst_10yr_alt_2019.png"
c1.SaveAs(outname)
