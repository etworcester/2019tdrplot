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

def filldiff(mm,up,down,mid):
      n = up.GetN()
      diffgraph = ROOT.TGraph(2*n)
      i = 0
      xup = ROOT.Double(-9.9)
      yup = ROOT.Double(-9.9)
      xlo = ROOT.Double(-9.9)
      ylo = ROOT.Double(-9.9)
      xmid = ROOT.Double(-9.9)
      ymid = ROOT.Double(-9.9)
      xmm = ROOT.Double(-9.9)
      ymm = ROOT.Double(-9.9)

      while i<n:
            up.GetPoint(i,xup,yup)
            mid.GetPoint(i,xmid,ymid)
            down.GetPoint(i,xlo,ylo)
            mm.GetPoint(i,xmm,ymm)
            yval = max(yup,ymid)
            yval = max(yval,ylo)
            yval = max(yval,ymm)

            diffgraph.SetPoint(i,xup,yval)

            up.GetPoint(n-i-1,xup,yup)
            down.GetPoint(n-i-1,xlo,ylo)
            mid.GetPoint(n-i-1,xmid,ymid)
            mm.GetPoint(n-i-1,xmm,ymm)            
            yval = min(yup,ymid)
            yval = min(yval,ylo)
            yval = min(yval,ymm)
            diffgraph.SetPoint(n+i,xlo,yval)

            i += 1
      return diffgraph
  
f1 = ROOT.TFile("root_v4/oa_variations_10year/cpv_sens_ndfd10year_allsyst_th13_asimov0_hie1_v4.root")
cpv1 = f1.Get("sens_cpv_nh")
f1m = ROOT.TFile("root_v4/oa_variations_10year/mh_sens_ndfd10year_allsyst_th13_asimov0_hie1_v4.root")
mh1 = f1m.Get("sens_mh_nh")

f2 = ROOT.TFile("root_v4/oa_variations_10year/cpv_sens_ndfd10year_allsyst_th13_asimov5_hie1_v4.root")
cpv2 = f2.Get("sens_cpv_nh")
f2m = ROOT.TFile("root_v4/oa_variations_10year/mh_sens_ndfd10year_allsyst_th13_asimov5_hie1_v4.root")
mh2 = f2m.Get("sens_mh_nh")

f3 = ROOT.TFile("root_v4/oa_variations_10year/cpv_sens_ndfd10year_allsyst_th13_asimov4_hie1_v4.root")
cpv3 = f3.Get("sens_cpv_nh")
f3m = ROOT.TFile("root_v4/oa_variations_10year/mh_sens_ndfd10year_allsyst_th13_asimov4_hie1_v4.root")
mh3 = f3m.Get("sens_mh_nh")

f4 = ROOT.TFile("root_v4/oa_variations_10year/cpv_sens_ndfd10year_allsyst_th13_asimov3_hie1_v4.root")
cpv4 = f4.Get("sens_cpv_nh")
f4m = ROOT.TFile("root_v4/oa_variations_10year/mh_sens_ndfd10year_allsyst_th13_asimov3_hie1_v4.root")
mh4 = f4m.Get("sens_mh_nh")

graph_cpvrange = filldiff(cpv1,cpv2,cpv3,cpv4)
graph_mhrange = filldiff(mh1,mh2,mh3,mh4)

cpv1.SetLineWidth(3)
cpv2.SetLineWidth(3)
cpv3.SetLineWidth(3)
cpv4.SetLineWidth(3)

cpv1.SetLineStyle(1)
cpv2.SetLineStyle(2)
cpv3.SetLineStyle(3)
cpv4.SetLineStyle(4)

cpv1.SetLineColor(ROOT.kCyan+3)
cpv2.SetLineColor(ROOT.kCyan+3)
cpv3.SetLineColor(ROOT.kCyan+3)
cpv4.SetLineColor(ROOT.kCyan+3)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-1.0,0.0,1.0,11.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_cpvrange.SetFillColor(ROOT.kCyan+1)
graph_cpvrange.SetLineColor(0)
graph_cpvrange.Draw("F same")
cpv1.Draw("L same")
cpv2.Draw("L same")
cpv3.Draw("L same")
cpv4.Draw("L same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.72,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.7,0.89,0.89)
l1.AddEntry(graph_cpvrange,"10 years (staged)","F")
l1.AddEntry(cpv3,"sin^{2}#theta_{23} = 0.418","L")
l1.AddEntry(cpv2,"sin^{2}#theta_{23} = 0.5","L")
l1.AddEntry(cpv1,"sin^{2}#theta_{23} = 0.580","L")
l1.AddEntry(cpv4,"sin^{2}#theta_{23} = 0.627","L")

l1.SetBorderSize(0)

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
t3sig.Draw("same")

t5sig = ROOT.TPaveText(-0.05,5.1,0.05,5.5)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
t5sig.Draw("same")

l1.SetFillColor(0)
l1.Draw("same")
outname = "plot_v4/vary_params/cpv_varyth23_2019_v4.eps"
outname2 = "plot_v4/vary_params/cpv_varyth23_2019_v4.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)


mh1.SetLineWidth(3)
mh2.SetLineWidth(3)
mh3.SetLineWidth(3)
mh4.SetLineWidth(3)

mh1.SetLineStyle(1)
mh2.SetLineStyle(2)
mh3.SetLineStyle(3)
mh4.SetLineStyle(4)

mh1.SetLineColor(ROOT.kCyan+3)
mh2.SetLineColor(ROOT.kCyan+3)
mh3.SetLineColor(ROOT.kCyan+3)
mh4.SetLineColor(ROOT.kCyan+3)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(-1.0,0.0,1.0,50.0)
h2.SetTitle("Mass Ordering Sensitivity")
h2.GetXaxis().SetTitle("#delta_{CP}/#pi")
h2.GetXaxis().CenterTitle()
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
graph_mhrange.SetFillColor(ROOT.kCyan+1)
graph_mhrange.Draw("F same")
mh1.Draw("L same")
mh2.Draw("L same")
mh3.Draw("L same")
mh4.Draw("L same")
ROOT.gPad.RedrawAxis()

t1.Draw("same")

l1.Draw("same")
outname = "plot_v4/vary_params/mh_varyth23_2019_v4.eps"
outname2 = "plot_v4/vary_params/mh_varyth23_2019_v4.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)

