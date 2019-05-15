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


hier = sys.argv[1]
if (hier == 'nh'):
      htext = "Normal Ordering"
      hiestr = "hie1"
elif (hier == 'ih'):
      htext = "Inverted Ordering"
      hiestr = "hie-1"
else:
      print "Must supply nh or ih!"
      exit()

f1text = "root_callum/cpv_throw_ndfd7year_allsyst_th13_"+hiestr+"_stat:start_v3_BAND.root"
f1 = ROOT.TFile(f1text)
band1 = f1.Get("throws_1sigma")
band1a = f1.Get("throws_2sigma")
cpv1 = f1.Get("throws_median")
f1a = ROOT.TFile("root_callum/cpv_sens_ndfd_336kTMWyr_allsyst_th13_hie1_v3.root")
a1 = f1a.Get("sens_cpv_"+hier)

f2text = "root_callum/cpv_throw_ndfd10year_allsyst_th13_"+hiestr+"_stat:start_v3_BAND.root"
f2 = ROOT.TFile(f2text)
band2 = f2.Get("throws_1sigma")
band2a = f2.Get("throws_2sigma")
cpv2 = f2.Get("throws_median")
f2a = ROOT.TFile("root_callum/cpv_sens_ndfd_624kTMWyr_allsyst_th13_hie1_v3.root")
a2 = f2a.Get("sens_cpv_"+hier)

f3text = "root_callum/mh_throw_ndfd7year_allsyst_th13_"+hiestr+"_stat:start_v3_BAND.root"
f3 = ROOT.TFile(f3text)
band3 = f3.Get("throws_1sigma")
band3a = f3.Get("throws_2sigma")
cpv3 = f3.Get("throws_median")
f3a = ROOT.TFile("root_callum/mh_sens_ndfd_336kTMWyr_allsyst_th13_hie1_v3.root")
a3 = f3a.Get("sens_mh_"+hier)

f4text = "root_callum/mh_throw_ndfd10year_allsyst_th13_"+hiestr+"_stat:start_v3_BAND.root"
f4 = ROOT.TFile(f4text)
band4 = f4.Get("throws_1sigma")
band4a = f4.Get("throws_2sigma")
cpv4 = f4.Get("throws_median")
f4a = ROOT.TFile("root_callum/mh_sens_ndfd_624kTMWyr_allsyst_th13_hie1_v3.root")
a4 = f4a.Get("sens_mh_"+hier)

a2.SetLineWidth(4)
a2.SetLineColor(ROOT.kBlue)

band2.SetFillStyle(1001)
band2a.SetFillStyle(1001)
band2.SetFillColor(ROOT.kGreen)
band2a.SetFillColor(ROOT.kYellow)

band2.SetLineColor(0)
band2a.SetLineColor(0)

a4.SetLineWidth(4)
a4.SetLineColor(ROOT.kBlue)

band4.SetFillStyle(1001)
band4a.SetFillStyle(1001)

band4.SetFillColor(ROOT.kGreen)
band4a.SetFillColor(ROOT.kYellow)

band4.SetLineColor(0)
band4a.SetLineColor(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.0,0.0,1.0,11.5)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
band2a.Draw("e3 same")
band2.Draw("e3 same")
a2.Draw("same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.52,0.68,0.89,0.89)
l1.AddEntry(a2,"10 years (staged, Asimov)", "L")
l1.AddEntry(band2, "1#sigma stat. variations","F")
l1.AddEntry(band2a, "2#sigma stat. variations","F")
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
outname = "plot/cpv/cpv_10yr_throws_"+hier+"_stats_2019.png"
c1.SaveAs(outname)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(-1.0,0.0,1.0,40.0)
h2.SetTitle("Mass Ordering Sensitivity")
h2.GetXaxis().SetTitle("#delta_{CP}/#pi")
h2.GetXaxis().CenterTitle()
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
band4a.Draw("e3 same")
band4.Draw("e3 same")
a4.Draw("same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

line2 = ROOT.TLine(-1.0,5.,1.0,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

l1.SetFillColor(0)
l1.Draw("same")
outname = "plot/mh/mh_10yr_throws_"+hier+"_stats_2019.png"
c2.SaveAs(outname)


