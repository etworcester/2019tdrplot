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

f1text = "root_callum/cpv_throw_ndfd7year_allsyst_th13_"+hiestr+"_stat:fake:start_v3_BAND.root"
f1 = ROOT.TFile(f1text)
band1 = f1.Get("throws_1sigma")
cpv1 = f1.Get("throws_median")
f1a = ROOT.TFile("root_callum/cpv_sens_ndfd_336kTMWyr_allsyst_th13_hie1_v3.root")
a1 = f1a.Get("sens_cpv_"+hier)


f2text = "root_callum/cpv_throw_ndfd10year_allsyst_th13_"+hiestr+"_stat:fake:start_v3_BAND.root"
f2 = ROOT.TFile(f2text)
band2 = f2.Get("throws_1sigma")
cpv2 = f2.Get("throws_median")
f2a = ROOT.TFile("root_callum/cpv_sens_ndfd_624kTMWyr_allsyst_th13_hie1_v3.root")
a2 = f2a.Get("sens_cpv_"+hier)


f3text = "root_callum/mh_throw_ndfd7year_allsyst_th13_"+hiestr+"_stat:fake:start_v3_BAND.root"
f3 = ROOT.TFile(f3text)
band3 = f3.Get("throws_1sigma")
cpv3 = f3.Get("throws_median")
f3a = ROOT.TFile("root_callum/mh_sens_ndfd_336kTMWyr_allsyst_th13_hie1_v3.root")
a3 = f3a.Get("sens_mh_"+hier)


f4text = "root_callum/mh_throw_ndfd10year_allsyst_th13_"+hiestr+"_stat:fake:start_v3_BAND.root"
f4 = ROOT.TFile(f4text)
band4 = f4.Get("throws_1sigma")
cpv4 = f4.Get("throws_median")
f4a = ROOT.TFile("root_callum/mh_sens_ndfd_624kTMWyr_allsyst_th13_hie1_v3.root")
a4 = f4a.Get("sens_mh_"+hier)

cpv1.SetLineWidth(4)
cpv1.SetLineColor(ROOT.kBlue-7)
cpv2.SetLineWidth(4)
cpv2.SetLineColor(ROOT.kOrange-3)

a1.SetLineWidth(4)
a1.SetLineStyle(2)
a1.SetLineColor(ROOT.kBlue-7)
a2.SetLineWidth(4)
a2.SetLineStyle(2)
a2.SetLineColor(ROOT.kOrange-7)

band1.SetFillStyle(1001)
band2.SetFillStyle(1001)

band1.SetFillColorAlpha(ROOT.kBlue-7,0.5)
band2.SetFillColorAlpha(ROOT.kOrange-3,0.5)

band1.SetLineColor(0)
band2.SetLineColor(0)

cpv3.SetLineWidth(4)
cpv3.SetLineColor(ROOT.kBlue-7)
cpv4.SetLineWidth(4)
cpv4.SetLineColor(ROOT.kOrange-3)

a3.SetLineWidth(4)
a3.SetLineStyle(2)
a3.SetLineColor(ROOT.kBlue-7)
a4.SetLineWidth(4)
a4.SetLineStyle(2)
a4.SetLineColor(ROOT.kOrange-7)

band3.SetFillStyle(1001)
band4.SetFillStyle(1001)

band3.SetFillColorAlpha(ROOT.kBlue-7,0.5)
band4.SetFillColorAlpha(ROOT.kOrange-3,0.5)

band3.SetLineColor(0)
band4.SetLineColor(0)

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
band2.Draw("e3 same")
band1.Draw("e3 same")
cpv1.Draw("same")
cpv2.Draw("same")
a1.Draw("same")
a2.Draw("same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23}: uniform NuFit 4.0")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

band_dum = band2.Clone()
band_dum.SetFillColorAlpha(ROOT.kBlack,0.25)
cpv_dum = cpv1.Clone()
cpv_dum.SetLineColor(ROOT.kBlack)
a_dum = a1.Clone()
a_dum.SetLineColor(ROOT.kBlack)
null = ROOT.TObject()

l1 = ROOT.TLegend(0.52,0.68,0.89,0.89)
l1.AddEntry(cpv1,"7 years (staged)", "L")
l1.AddEntry(cpv2,"10 years (staged)", "L")
l1.AddEntry(cpv_dum,"Median of Throws","L")
l1.AddEntry(a_dum,"Asimov Set","L")
l1.AddEntry(band_dum, "1#sigma variations of","F")
l1.AddEntry(null,"statistics, systematics,","")
l1.AddEntry(null,"and oscillation parameters","")
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
outname = "plot/cpv/cpv_two_exps_throws_"+hier+"_compareasimov_2019.png"
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
band4.Draw("e3 same")
band3.Draw("e3 same")
cpv3.Draw("same")
cpv4.Draw("same")
a3.Draw("same")
a4.Draw("same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23}: uniform NuFit 4.0")
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
outname = "plot/mh/mh_two_exps_throws_"+hier+"_compareasimov_2019.png"
c2.SaveAs(outname)


