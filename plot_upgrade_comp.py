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

fnom = ROOT.TFile("root_v4/staging_graphs_nomupgrade.root")
fnone = ROOT.TFile("root_v4/staging_graphs_noupgrade.root")
ffast2 = ROOT.TFile("root_v4/staging_graphs_fastupgrade2.root")
ffast4 = ROOT.TFile("root_v4/staging_graphs_fastupgrade4.root")

cpvbest_nom = fnom.Get("cpvbest")
cpvbest_none = fnone.Get("cpvbest")
cpvbest_fast2 = ffast2.Get("cpvbest")
cpvbest_fast4 = ffast4.Get("cpvbest")

cpvbest_none.SetFillColor(ROOT.kRed-10)
cpvbest_fast2.SetFillColor(ROOT.kCyan-3)
cpvbest_fast4.SetFillColor(ROOT.kCyan-10)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.0,0.0,15.0,12.0)
cpvbest_none.Draw("fsame")
cpvbest_fast4.Draw("fsame")
cpvbest_fast2.Draw("fsame")
cpvbest_nom.Draw("fsame")
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

t1 = ROOT.TPaveText(0.16,0.72,0.55,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.88,0.89)
l1.AddEntry(cpvbest_nom, "1.2#rightarrow2.4 MW (6 years)","F")
l1.AddEntry(cpvbest_none, "1.2 MW (no upgrade)","F")
l1.AddEntry(cpvbest_fast2, "2.4 MW (2 year delay)","F")
l1.AddEntry(cpvbest_fast4, "2.4 MW (4 year delay)","F")
l1.SetBorderSize(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,15.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,15.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestaging_maxcpv.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestaging_maxcpv.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)                               


cpv50_nom = fnom.Get("cpv50")
cpv50_none = fnone.Get("cpv50")
cpv50_fast2 = ffast2.Get("cpv50")
cpv50_fast4 = ffast4.Get("cpv50")

cpv50_nom.SetFillColor(ROOT.kPink-3)
cpv50_none.SetFillColor(ROOT.kRed-10)
cpv50_fast2.SetFillColor(ROOT.kCyan-3)
cpv50_fast4.SetFillColor(ROOT.kCyan-10)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0.0,0.0,15.0,8.0)
cpv50_none.Draw("fsame")
cpv50_fast4.Draw("fsame")
cpv50_fast2.Draw("fsame")
cpv50_nom.Draw("fsame")
h2.SetTitle("CP Violation Sensitivity")
h2.GetXaxis().SetTitle("Years")
h2.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.5)
h2.GetYaxis().CenterTitle()
c2.Modified()
l1.Draw("same")
line1.Draw("same")
line2.Draw("same")

t2 = ROOT.TPaveText(0.16,0.72,0.55,0.89,"NDC")
t2.AddText("DUNE Sensitivity (Staged)")
t2.AddText("All Systematics")
t2.AddText("Normal Ordering")
t2.AddText("50% of #delta_{CP} values")
t2.SetBorderSize(0)
t2.SetFillStyle(0)
t2.SetTextAlign(12)
t2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestaging_50pc.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestaging_50pc.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)                               

cpv75_nom = fnom.Get("cpv75")
cpv75_none = fnone.Get("cpv75")
cpv75_fast2 = ffast2.Get("cpv75")
cpv75_fast4 = ffast4.Get("cpv75")

cpv75_nom.SetFillColor(ROOT.kPink-3)
cpv75_none.SetFillColor(ROOT.kRed-10)
cpv75_fast2.SetFillColor(ROOT.kCyan-3)
cpv75_fast4.SetFillColor(ROOT.kCyan-10)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0.0,0.0,15.0,8.0)
cpv75_none.Draw("fsame")
cpv75_fast4.Draw("fsame")
cpv75_fast2.Draw("fsame")
cpv75_nom.Draw("fsame")
h3.SetTitle("CP Violation Sensitivity")
h3.GetXaxis().SetTitle("Years")
h3.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.5)
h3.GetYaxis().CenterTitle()
c3.Modified()
l1.Draw("same")
line1.Draw("same")
line2.Draw("same")

t3 = ROOT.TPaveText(0.16,0.72,0.55,0.89,"NDC")
t3.AddText("DUNE Sensitivity (Staged)")
t3.AddText("All Systematics")
t3.AddText("Normal Ordering")
t3.AddText("75% of #delta_{CP} values")
t3.SetBorderSize(0)
t3.SetFillStyle(0)
t3.SetTextAlign(12)
t3.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestaging_75pc.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestaging_75pc.png"
c3.SaveAs(outname)
c3.SaveAs(outname2)                               

