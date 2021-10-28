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
f10 = ROOT.TFile("root_v4/staging_graphs_10kt.root")
f20 = ROOT.TFile("root_v4/staging_graphs_20kt.root")

cpvbest_nom = fnom.Get("cpvbest")
cpvbest_10 = f10.Get("cpvbest")
cpvbest_20 = f20.Get("cpvbest")

cpvbest_20.SetFillColor(ROOT.kCyan-3)
cpvbest_20.SetLineColor(ROOT.kCyan-3)
cpvbest_20.SetLineWidth(4)
cpvbest_10.SetFillColor(ROOT.kCyan-3)
cpvbest_10.SetLineColor(ROOT.kCyan-3)
cpvbest_10.SetLineStyle(2)
cpvbest_10.SetLineWidth(4)
cpvbest_nom.SetFillColor(ROOT.kPink-3)
cpvbest_nom.SetLineColor(ROOT.kPink-3)
cpvbest_nom.SetLineWidth(4)


c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.0,0.0,15.0,10.0)
#cpvbest_10.Draw("fsame")
#cpvbest_20.Draw("fsame")
#cpvbest_nom.Draw("fsame")
cpvbest_10.DrawGraph(61)
cpvbest_20.DrawGraph(61)
cpvbest_nom.DrawGraph(61)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("Varying FD Mass")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

null = ROOT.TObject()

l1 = ROOT.TLegend(0.5,0.7,0.88,0.89)
l1.AddEntry(cpvbest_nom, "Nominal Staging:","L")
l1.AddEntry(null,"40 kt (fiducial) FD (3 years)","")
l1.AddEntry(null,"1.2 MW -> 2.4 MW (6 years)","")
l1.AddEntry(cpvbest_10, "10 kt (fiducial) FD","L")
l1.AddEntry(cpvbest_20, "20 kt (fiducial) FD","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,15.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,15.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

hk = ROOT.TMarker(3.5,5.0, 29)
hk.SetMarkerSize(3.)
#hk.Draw("P")

hktext = ROOT.TPaveText(2.0,5.,5.0,6.)
hktext.AddText("HyperK 5#sigma")
hktext.SetBorderSize(0)
hktext.SetFillStyle(0)
#hktext.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestartmass_maxcpv.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestartmass_maxcpv.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)                               

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.0,0.0,5.0,5.0)
cpvbest_10.DrawGraph(61)
cpvbest_20.DrawGraph(61)
#cpvbest_nom.DrawGraph(61)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("Varying FD Mass")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

null = ROOT.TObject()

l1 = ROOT.TLegend(0.5,0.8,0.88,0.89)
#l1.AddEntry(cpvbest_nom, "Nominal Staging:","L")
#l1.AddEntry(null,"40 kt (fiducial) FD (3 years)","")
l1.AddEntry(cpvbest_10, "10 kt (fiducial) FD","L")
l1.AddEntry(cpvbest_20, "20 kt (fiducial) FD","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,5.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,5.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
#line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestartmassearly_maxcpv_only1020.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestartmassearly_maxcpv_only1020.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)                               

cpv50_nom = fnom.Get("cpv50")
cpv50_10 = f10.Get("cpv50")
cpv50_20 = f20.Get("cpv50")

cpv50_20.SetFillColor(ROOT.kCyan-3)
cpv50_20.SetLineColor(ROOT.kCyan-3)
cpv50_20.SetLineWidth(4)
cpv50_10.SetFillColor(ROOT.kCyan-3)
cpv50_10.SetLineColor(ROOT.kCyan-3)
cpv50_10.SetLineStyle(2)
cpv50_10.SetLineWidth(4)
cpv50_nom.SetFillColor(ROOT.kPink-3)
cpv50_nom.SetLineColor(ROOT.kPink-3)
cpv50_nom.SetLineWidth(4)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.0,0.0,5.0,5.0)
cpv50_10.DrawGraph(61)
cpv50_20.DrawGraph(61)
cpv50_nom.DrawGraph(61)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("Varying FD Mass")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("50% of #delta_{CP} values")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

null = ROOT.TObject()

l1 = ROOT.TLegend(0.5,0.7,0.88,0.89)
l1.AddEntry(cpvbest_nom, "Nominal Staging:","L")
l1.AddEntry(null,"40 kt (fiducial) FD (3 years)","")
l1.AddEntry(cpvbest_10, "10 kt (fiducial) FD","L")
l1.AddEntry(cpvbest_20, "20 kt (fiducial) FD","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1.Draw("same")

#line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_comparestartmassearly_cpv50.eps"
outname2 = "plot_v4/exposures/cpv_exp_comparestartmassearly_cpv50.png"
c3.SaveAs(outname)
c3.SaveAs(outname2)                               

mh_nom = fnom.Get("mh100")
mh_10 = f10.Get("mh100")
mh_20 = f20.Get("mh100")

mh_20.SetFillColor(ROOT.kCyan-3)
mh_20.SetLineColor(ROOT.kCyan-3)
mh_20.SetLineWidth(4)
mh_10.SetFillColor(ROOT.kCyan-3)
mh_10.SetLineColor(ROOT.kCyan-3)
mh_10.SetLineStyle(2)
mh_10.SetLineWidth(4)
mh_nom.SetFillColor(ROOT.kPink-3)
mh_nom.SetLineColor(ROOT.kPink-3)
mh_nom.SetLineWidth(4)

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0,0.0,7.0,15.0)
h4.SetTitle("Mass Ordering Sensitivity")
h4.GetXaxis().SetTitle("Years")
h4.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h4.GetYaxis().SetTitleOffset(1.5)
h4.GetYaxis().CenterTitle()
c4.Modified()

mh_10.DrawGraph(61)
mh_20.DrawGraph(61)
mh_nom.DrawGraph(61)

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("Varying FD Mass")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("100% of #delta_{CP} values")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1.Draw("same")

line3 = ROOT.TLine(0.0,5.,7.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot_v4/exposures/mh_exp_staging_comparestartmass.eps"
outname2 = "plot_v4/exposures/mh_exp_staging_comparestartmass.png"
c4.SaveAs(outname)
c4.SaveAs(outname2)                               


