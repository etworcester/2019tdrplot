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
fnomramp = ROOT.TFile("root_v4/staging_graphs_rampcomm.root")
#fnone = ROOT.TFile("root_v4/staging_graphs_ramp_a.root")
#ffast2 = ROOT.TFile("root_v4/staging_graphs_ramp_b.root")
ffast4 = ROOT.TFile("root_v4/staging_graphs_fastrampcomm.root")

cpvbest_nom = fnom.Get("cpvbest")
cpvbest_nomramp = fnomramp.Get("cpvbest")
#cpvbest_none = fnone.Get("cpvbest")
#cpvbest_fast2 = ffast2.Get("cpvbest")
cpvbest_fast4 = ffast4.Get("cpvbest")

#cpvbest_none.SetLineColor(ROOT.kPink)
cpvbest_nom.SetLineColor(ROOT.kRed-10)
cpvbest_nomramp.SetLineColor(ROOT.kRed)
#cpvbest_fast2.SetLineColor(ROOT.kMagenta)
cpvbest_fast4.SetLineColor(ROOT.kCyan)

#cpvbest_none.SetLineWidth(4)
cpvbest_nom.SetLineWidth(4)
cpvbest_nomramp.SetLineWidth(4)
#cpvbest_fast2.SetLineWidth(4)
cpvbest_fast4.SetLineWidth(4)

cpvbest_nom.SetLineStyle(2)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.0,0.0,4.0,5.0)
cpvbest_nom.DrawGraph(101)
cpvbest_nomramp.DrawGraph(101)
#cpvbest_none.DrawGraph(101)
#cpvbest_fast2.DrawGraph(101)
cpvbest_fast4.DrawGraph(101)
ROOT.gPad.RedrawAxis()

h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.5,0.7,0.88,0.89)
l1.AddEntry(cpvbest_nom, "TDR Staging (no ramp)","L")
l1.AddEntry(cpvbest_nomramp, "Nominal PIP-II ramp","L")
#l1.AddEntry(cpvbest_none, "Scenario A (incl ramp)","L")
#l1.AddEntry(cpvbest_fast2, "Scenario B (incl ramp)","L")
l1.AddEntry(cpvbest_fast4, "Fast PIP-II ramp","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,4.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,4.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
#line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestagingrampcomm_maxcpv.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestagingrampcomm_maxcpv.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)                               


cpv50_nom = fnom.Get("cpv50")
cpv50_nomramp = fnomramp.Get("cpv50")
#cpv50_none = fnone.Get("cpv50")
#cpv50_fast2 = ffast2.Get("cpv50")
cpv50_fast4 = ffast4.Get("cpv50")

#cpv50_none.SetLineColor(ROOT.kPink)
cpv50_nom.SetLineColor(ROOT.kRed-10)
cpv50_nomramp.SetLineColor(ROOT.kRed)
#cpv50_fast2.SetLineColor(ROOT.kMagenta)
cpv50_fast4.SetLineColor(ROOT.kCyan)

#cpv50_none.SetLineWidth(4)
cpv50_nom.SetLineWidth(4)
cpv50_nomramp.SetLineWidth(4)
#cpv50_fast2.SetLineWidth(4)
cpv50_fast4.SetLineWidth(4)

cpv50_nom.SetLineStyle(2)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0.0,0.0,4.0,5.0)
#cpv50_none.DrawGraph(101)
cpv50_fast4.DrawGraph(101)
#cpv50_fast2.DrawGraph(101)
cpv50_nom.DrawGraph(101)
cpv50_nomramp.DrawGraph(101)
h2.SetTitle("CP Violation Sensitivity")
h2.GetXaxis().SetTitle("Years")
h2.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.5)
h2.GetYaxis().CenterTitle()
c2.Modified()
l1.Draw("same")
#line1.Draw("same")
#line2.Draw("same")
ROOT.gPad.RedrawAxis()

t2 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t2.AddText("DUNE Sensitivity (Staged)")
t2.AddText("All Systematics")
t2.AddText("Normal Ordering")
t2.AddText("50% of #delta_{CP} values")
t2.SetBorderSize(0)
t2.SetFillStyle(0)
t2.SetTextAlign(12)
t2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestagingrampcomm_50pc.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestagingrampcomm_50pc.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)                               

cpv75_nom = fnom.Get("cpv75")
cpv75_nomramp = fnomramp.Get("cpv75")
#cpv75_none = fnone.Get("cpv75")
#cpv75_fast2 = ffast2.Get("cpv75")
cpv75_fast4 = ffast4.Get("cpv75")

cpv75_nom.SetFillColor(ROOT.kPink-3)
cpv75_nomramp.SetFillColor(ROOT.kPink-3)
#cpv75_none.SetFillColor(ROOT.kRed-10)
#cpv75_fast2.SetFillColor(ROOT.kMagenta)
cpv75_fast4.SetFillColor(ROOT.kCyan-10)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0.0,0.0,4.0,4.0)
#cpv75_none.Draw("fsame")
cpv75_fast4.Draw("fsame")
#cpv75_fast2.Draw("fsame")
cpv75_nom.Draw("fsame")
h3.SetTitle("CP Violation Sensitivity")
h3.GetXaxis().SetTitle("Years")
h3.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.5)
h3.GetYaxis().CenterTitle()
c3.Modified()
l1.Draw("same")
line1.Draw("same")
#line2.Draw("same")

t3 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t3.AddText("DUNE Sensitivity (Staged)")
t3.AddText("All Systematics")
t3.AddText("Normal Ordering")
t3.AddText("75% of #delta_{CP} values")
t3.SetBorderSize(0)
t3.SetFillStyle(0)
t3.SetTextAlign(12)
t3.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestagingrampcomm_75pc.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestagingrampcomm_75pc.png"
c3.SaveAs(outname)
c3.SaveAs(outname2)                               

mh_nom = fnom.Get("mh100")
mh_nomramp = fnomramp.Get("mh100")
#mh_none = fnone.Get("mh100")
#mh_fast2 = ffast2.Get("mh100")
mh_fast4 = ffast4.Get("mh100")

#mh_none.SetLineColor(ROOT.kPink)
mh_nom.SetLineColor(ROOT.kRed-10)
mh_nomramp.SetLineColor(ROOT.kRed)
#mh_fast2.SetLineColor(ROOT.kMagenta)
mh_fast4.SetLineColor(ROOT.kCyan)

#mh_none.SetLineWidth(4)
mh_nom.SetLineWidth(4)
mh_nomramp.SetLineWidth(4)
#mh_fast2.SetLineWidth(4)
mh_fast4.SetLineWidth(4)

mh_nom.SetLineStyle(2)

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0.0,0.0,4.0,10.0)
#mh_none.DrawGraph(101)
mh_fast4.DrawGraph(101)
#mh_fast2.DrawGraph(101)
mh_nom.DrawGraph(101)
mh_nomramp.DrawGraph(101)
h4.SetTitle("Mass Ordering Sensitivity")
h4.GetXaxis().SetTitle("Years")
h4.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h4.GetYaxis().SetTitleOffset(1.5)
h4.GetYaxis().CenterTitle()
c4.Modified()
l1.Draw("same")
line1.Draw("same")
line2.Draw("same")
ROOT.gPad.RedrawAxis()

t4 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t4.AddText("DUNE Sensitivity (Staged)")
t4.AddText("All Systematics")
t4.AddText("Normal Ordering")
t4.AddText("100% of #delta_{CP} values")
t4.SetBorderSize(0)
t4.SetFillStyle(0)
t4.SetTextAlign(12)
t4.Draw("same")

outname = "plot_v4/exposures/mh_exp_comparestagingrampcomm_100pc.eps"
outname2 = "plot_v4/exposures/mh_exp_comparestagingrampcomm_100pc.png"
c4.SaveAs(outname)
c4.SaveAs(outname2)                               
