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
            print i, yup, ymid, ylo, ymm, yval

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

hier = sys.argv[1]
if (hier == 'no'):
      htext = "Normal Ordering"
elif (hier == 'io'):
      htext = "Inverted Ordering"
else:
      print "Must supply no or io!"
      exit()

f1text = "root/cpv_sens_aset0_th23pen0_exp7yr.root"
f1 = ROOT.TFile(f1text)
cpv1 = f1.Get("sens_cpv_nh")

f1lotext = "root/cpv_sens_aset1_th23pen0_exp7yr.root"
f1lo = ROOT.TFile(f1lotext)
cpv1lo = f1lo.Get("sens_cpv_nh")

f1hitext = "root/cpv_sens_aset2_th23pen0_exp7yr.root"
f1hi = ROOT.TFile(f1hitext)
cpv1hi = f1hi.Get("sens_cpv_nh")

f1mmtext = "root/cpv_sens_aset3_th23pen0_exp7yr.root"
f1mm = ROOT.TFile(f1mmtext)
cpv1mm = f1mm.Get("sens_cpv_nh")

f1mintext = "root/cpv_sens_aset4_th23pen0_exp7yr.root"
f1min = ROOT.TFile(f1mintext)
cpv1min = f1min.Get("sens_cpv_nh")

f1maxtext = "root/cpv_sens_aset5_th23pen0_exp7yr.root"
f1max = ROOT.TFile(f1maxtext)
cpv1max = f1max.Get("sens_cpv_nh")

f3text = "root/cpv_sens_aset0_th23pen0_exp10yr.root"
f3 = ROOT.TFile(f3text)
cpv3 = f3.Get("sens_cpv_nh")

f3lotext = "root/cpv_sens_aset1_th23pen0_exp10yr.root"
f3lo = ROOT.TFile(f3lotext)
cpv3lo = f3lo.Get("sens_cpv_nh")

f3hitext = "root/cpv_sens_aset2_th23pen0_exp10yr.root"
f3hi = ROOT.TFile(f3hitext)
cpv3hi = f3hi.Get("sens_cpv_nh")

f3mmtext = "root/cpv_sens_aset3_th23pen0_exp10yr.root"
f3mm = ROOT.TFile(f3mmtext)
cpv3mm = f3mm.Get("sens_cpv_nh")

f3mintext = "root/cpv_sens_aset4_th23pen0_exp10yr.root"
f3min = ROOT.TFile(f3mintext)
cpv3min = f3min.Get("sens_cpv_nh")

f3maxtext = "root/cpv_sens_aset5_th23pen0_exp10yr.root"
f3max = ROOT.TFile(f3maxtext)
cpv3max = f3max.Get("sens_cpv_nh")


graph_cpvrange1 = filldiff(cpv1mm,cpv1max,cpv1min,cpv1)
graph_cpvrange1_90 = filldiff(cpv1lo,cpv1lo,cpv1hi,cpv1)

graph_cpvrange3 = filldiff(cpv3mm,cpv3max,cpv3min,cpv3)
graph_cpvrange3_90 = filldiff(cpv3lo,cpv3lo,cpv3hi,cpv3)


cpv1.SetLineWidth(3)
cpv1.SetLineColor(ROOT.kGreen-1)
#cpv1.SetLineStyle(2)

cpv3.SetLineWidth(3)
cpv3.SetLineColor(ROOT.kOrange+8)
#cpv3.SetLineStyle(2)

cpv3hi.SetLineWidth(3)

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
graph_cpvrange1.SetFillColor(ROOT.kGreen-7)
graph_cpvrange1_90.SetFillColor(ROOT.kGreen-2)
graph_cpvrange1.SetLineWidth(0)
graph_cpvrange1_90.SetLineWidth(0)
graph_cpvrange1.Draw("F same")
graph_cpvrange1_90.Draw("F same")
#cpv1.Draw("L same")


graph_cpvrange3.SetFillColor(ROOT.kOrange-2)
graph_cpvrange3_90.SetFillColor(ROOT.kOrange-3)
graph_cpvrange3.SetLineWidth(0)
graph_cpvrange3_90.SetLineWidth(0)
graph_cpvrange3.Draw("F same")
graph_cpvrange3_90.Draw("F same")
#cpv3.Draw("L same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.75,0.53,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("#theta_{23}: NuFit4.0 (90% C.L. range)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
l1.AddEntry(graph_cpvrange1,"7 years (staged)", "F")
l1.AddEntry(graph_cpvrange3,"10 years (staged)", "F")
if (hier == 'no'):
      l1.AddEntry(cpv1,"sin^{2}#theta_{23} = 0.580 #pm 0.035", "L")
elif (hier == 'io'):
      l1.AddEntry(cpv1,"sin^{2}#theta_{23} = 0.583 #pm 0.034", "L")      
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
outname = "plot/cpv_two_exps_th23band_"+hier+"_2019alt4.png"
c1.SaveAs(outname)


