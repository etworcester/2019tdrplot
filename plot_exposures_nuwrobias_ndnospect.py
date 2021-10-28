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


myfile = ROOT.TFile("root_v4/nospect_graphs.root")
cpv_dcpmax_nom = myfile.Get("fullND_dcpmax")
cpv_dcpmax_nospect = myfile.Get("LArNoSpect_dcpmax")
cpv_dcpmax_LArND = myfile.Get("LArTMS_dcpmax")

cpv_dcpmax_nom.SetLineWidth(4)
cpv_dcpmax_nospect.SetLineWidth(4)
cpv_dcpmax_LArND.SetLineWidth(4)

cpv_dcpmax_nospect.SetLineStyle(3)
cpv_dcpmax_LArND.SetLineStyle(2)

cpv_dcpmax_nom.SetLineColor(ROOT.kOrange-3)
cpv_dcpmax_nospect.SetLineColor(ROOT.kOrange+3)
cpv_dcpmax_LArND.SetLineColor(ROOT.kOrange-5)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,200.0,6.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
cpv_dcpmax_nom.Draw("Lsame")
cpv_dcpmax_nospect.Draw("Lsame")
cpv_dcpmax_LArND.Draw("Lsame")

t1 = ROOT.TPaveText(0.16,0.68,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.52,0.68,0.89,0.89)
l1.AddEntry(cpv_dcpmax_nom, "Reference Near Detector","L")
l1.AddEntry(cpv_dcpmax_LArND,"ND-LAr + TMS","L")
l1.AddEntry(cpv_dcpmax_nospect,"ND-LAr (no spectrometer)","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,200.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1000.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
#line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_ndnospect_dcpmax.eps"
outname2 = "plot_v4/exposures/cpv_exp_ndnospect_dcpmax.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

myfile = ROOT.TFile("root_v4/nospect_graphs.root")
cpv_dcp50pct_nom = myfile.Get("fullND_dcp50pct")
cpv_dcp50pct_nospect = myfile.Get("LArNoSpect_dcp50pct")
cpv_dcp50pct_LArND = myfile.Get("LArTMS_dcp50pct")


cpv_dcp50pct_nom.SetLineWidth(4)
cpv_dcp50pct_nospect.SetLineWidth(4)
cpv_dcp50pct_LArND.SetLineWidth(4)

cpv_dcp50pct_nospect.SetLineStyle(3)
cpv_dcp50pct_LArND.SetLineStyle(2)

cpv_dcp50pct_nom.SetLineColor(ROOT.kOrange-3)
cpv_dcp50pct_nospect.SetLineColor(ROOT.kOrange+3)
cpv_dcp50pct_LArND.SetLineColor(ROOT.kOrange-5)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,1000.0,11.0)
h2.SetTitle("CP Violation Sensitivity")
h2.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h2.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
cpv_dcp50pct_nom.Draw("Lsame")
cpv_dcp50pct_nospect.Draw("Lsame")
cpv_dcp50pct_LArND.Draw("Lsame")

t2 = ROOT.TPaveText(0.16,0.68,0.5,0.89,"NDC")
t2.AddText("DUNE Sensitivity")
t2.AddText("All Systematics")
t2.AddText("Normal Ordering")
t2.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t2.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t2.AddText("50% of #delta_{CP} values")
t2.SetFillStyle(0)
t2.SetBorderSize(0)
t2.SetTextAlign(12)
t2.Draw("same")

l1.Draw("same")

line1 = ROOT.TLine(0.,3.,1000.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1000.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_ndnospect_dcp50pct.eps"
outname2 = "plot_v4/exposures/cpv_exp_ndnospect_dcp50pct.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)

