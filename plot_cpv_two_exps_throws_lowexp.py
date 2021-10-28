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


f1text = "root_v4_lowexposure/CAFAna_throws_ndfd_66ktMWyr_NH_th13_BAND.root"
f1 = ROOT.TFile(f1text)
f2text = "root_v4_lowexposure/CAFAna_throws_ndfd_100ktMWyr_NH_th13_BAND.root"
f2 = ROOT.TFile(f2text)
if (hier == 'ih'):
      f1text = "root_v4_lowexposure/CAFAna_throws_ndfd_66ktMWyr_IH_th13_BAND.root"
      f1 = ROOT.TFile(f1text)
      f2text = "root_v4_lowexposure/CAFAna_throws_ndfd_100ktMWyr_IH_th13_BAND.root"
      f2 = ROOT.TFile(f2text)


cpv1 = f1.Get("cpv_throws_1sigma")
cpv2 = f2.Get("cpv_throws_1sigma")
cpv3 = f1.Get("mh_throws_1sigma")
cpv4 = f2.Get("mh_throws_1sigma")
      
cpv1.SetLineWidth(4)
cpv1.SetLineColor(ROOT.kBlue-7)
cpv2.SetLineWidth(4)
cpv2.SetLineColor(ROOT.kOrange-3)

cpv1.SetFillStyle(1001)
cpv2.SetFillStyle(1001)

cpv1.SetFillColorAlpha(ROOT.kBlue-7,0.5)
cpv2.SetFillColorAlpha(ROOT.kOrange-3,0.5)

cpv3.SetLineWidth(4)
cpv3.SetLineColor(ROOT.kBlue-7)
cpv4.SetLineWidth(4)
cpv4.SetLineColor(ROOT.kOrange-3)

cpv3.SetFillStyle(1001)
cpv4.SetFillStyle(1001)

cpv3.SetFillColorAlpha(ROOT.kBlue-7,0.5)
cpv4.SetFillColorAlpha(ROOT.kOrange-3,0.5)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.0,0.0,1.0,6.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sqrt{#Delta#chi^{2}_{#lower[-0.3]{#scale[0.7]{CPV}}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
cpv2.Draw("l e3 same")
cpv1.Draw("l e3 same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

band_dum = cpv2.Clone()
band_dum.SetFillColorAlpha(ROOT.kBlack,0.25)
band_dum.SetLineColor(0)
cpv_dum = cpv1.Clone()
cpv_dum.SetLineColor(ROOT.kBlack)
null = ROOT.TObject()

l1 = ROOT.TLegend(0.52,0.68,0.89,0.89)
l1.AddEntry(cpv1,"66 kt-MW-years", "L")
l1.AddEntry(cpv2,"100 kt-MW-years", "L")
l1.AddEntry(cpv_dum,"Median of Throws","L")
l1.AddEntry(band_dum, "1#sigma: Variations of","F")
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
#line2.Draw("same")

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
outname1 = "plot_v4/cpv/cpv_two_exps_throws_"+hier+"_2019_v4_lowexp.png"
outname2 = "plot_v4/cpv/cpv_two_exps_throws_"+hier+"_2019_v4_lowexp.eps"
c1.SaveAs(outname1)
c1.SaveAs(outname2)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(-1.0,0.0,1.0,20.0)
h2.SetTitle("Mass Ordering Sensitivity")
h2.GetXaxis().SetTitle("#delta_{CP}/#pi")
h2.GetXaxis().CenterTitle()
h2.GetYaxis().SetTitle("#sqrt{#Delta#chi^{2}_{#lower[-0.3]{#scale[0.7]{MO}}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
cpv4.Draw("l e3 same")
cpv3.Draw("l e3 same")

ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
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
outname1 = "plot_v4/mh/mh_two_exps_throws_"+hier+"_2019_v4_lowexp.png"
outname2 = "plot_v4/mh/mh_two_exps_throws_"+hier+"_2019_v4_lowexp.eps"
c2.SaveAs(outname1)
c2.SaveAs(outname2)


