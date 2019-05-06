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

hier = sys.argv[1]
if (hier == 'no'):
      htext = "Normal Ordering"
elif (hier == 'io'):
      htext = "Inverted Ordering"
else:
      print "Must supply no or io!"
      exit()

f1text = "root/cpv_sens_ndfd_allsyst_th13.root"
f1 = ROOT.TFile(f1text)
cpv1 = f1.Get("sens_cpv_nh")

f2text = "root/cpv_sens_ndfd_allsyst_nopen.root"
f2 = ROOT.TFile(f2text)
cpv2 = f2.Get("sens_cpv_nh")

f3text = "root/cpv_sens_ndfdfull_allsyst_th13.root"
f3 = ROOT.TFile(f3text)
cpv3 = f3.Get("sens_cpv_nh")

f4text = "root/cpv_sens_ndfdfull_allsyst_nopen.root"
f4 = ROOT.TFile(f4text)
cpv4 = f4.Get("sens_cpv_nh")

graph_cpvrange1 = filldiff(cpv1,cpv2)

graph_cpvrange2 = filldiff(cpv3,cpv4)

cpv2.SetLineWidth(3)
cpv1.SetLineWidth(3)
cpv2.SetLineStyle(2)

cpv4.SetLineWidth(3)
cpv3.SetLineWidth(3)
cpv4.SetLineStyle(2)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
#c1.SetGridx(1)
#c1.SetGridy(1)
h1 = c1.DrawFrame(-1.0,0.0,1.0,10.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("#delta_{CP}/#pi")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_cpvrange1.SetFillColor(ROOT.kGreen-7)
graph_cpvrange1.Draw("F same")
graph_cpvrange2.SetFillColor(ROOT.kOrange-3)
#graph_cpvrange2.Draw("F same")
#graph_cpvrange3.SetFillColor(ROOT.kBlue-7)
#graph_cpvrange3.Draw("F same")
cpv2.Draw("L same")
cpv1.Draw("L same")
cpv4.Draw("L same")
cpv3.Draw("L same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.75,0.45,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText(htext)
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
if (hier == 'no'):
      t1.AddText("sin^{2}#theta_{23} = 0.580 #pm 0.035")
elif (hier == 'io'):
      t1.AddText("sin^{2}#theta_{23} = 0.583 #pm 0.034")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.6,0.72,0.89,0.89)
l1.AddEntry(graph_cpvrange1,"7 years (staged)", "F")
l1.AddEntry(graph_cpvrange2,"10 years (staged)", "F")
l1.AddEntry(cpv1,"Nominal analysis","L")
l1.AddEntry(cpv2,"#theta_{13} unconstrained","L")
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
outname = "plot/cpv_two_exps_varyconstr_"+hier+"_2019.png"
c1.SaveAs(outname)

