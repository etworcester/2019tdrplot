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

f1 = ROOT.TFile("root_callum/cpv_sens_ndfd_624kTMWyr_allsyst_th13_hie1_v3.root")
anom = f1.Get("sens_cpv_"+hier)
f1a = ROOT.TFile("root_chris/cpv_res_tdr_minus1to1.root")
idnom = f1a.Get("th13_10yr")

r1s = ROOT.TGraphSmooth("normal")
dnom = r1s.SmoothKern(idnom,"normal",0.25) 

f2 = ROOT.TFile("root_callum/cpv_sens_fd_624kTMWyr_nosyst_th13_hie1_asimov0_v3.root")
anosyst = f2.Get("sens_cpv_"+hier)

f3 = ROOT.TFile("root_chris/nuwro_bias_fdOnly.root")
afdonly = f3.Get("cpv_NuWroBias_68pct")
idfdonly = f3.Get("dcp_NuWroBias_68pct")
idnosyst = f3.Get("dcp_nosyst")

r2s = ROOT.TGraphSmooth("normal")
dnosyst = r2s.SmoothKern(idnosyst,"normal",0.25) 
r3s = ROOT.TGraphSmooth("normal")
dfdonly = r3s.SmoothKern(idfdonly,"normal",0.25) 

f4 = ROOT.TFile("root_callum/cpv_sens_fd_624kTMWyr_allsyst_th13_hie1_asimov0_v3.root")
afdonly_w = f4.Get("sens_cpv_"+hier)

f5 = ROOT.TFile("root_chris/nuwro_bias_gif.root")
afdonly5 = f5.Get("cpv_gif_05")
afdonly10 = f5.Get("cpv_gif_10")
idfdonly_w = f5.Get("dcp_gif_00")
idfdonly5 = f5.Get("dcp_gif_05")
idfdonly10 = f5.Get("dcp_gif_10")

r4s = ROOT.TGraphSmooth("normal")
dfdonly_w = r4s.SmoothKern(idfdonly_w,"normal",0.25) 
r5s = ROOT.TGraphSmooth("normal")
dfdonly5 = r5s.SmoothKern(idfdonly5,"normal",0.25) 
r6s = ROOT.TGraphSmooth("normal")
dfdonly10 = r6s.SmoothKern(idfdonly10,"normal",0.25) 

realband = filldiff(afdonly,afdonly5)
realband.SetLineColor(0)
realband.SetFillColorAlpha(ROOT.kOrange-5,0.25)

dband = filldiff(dfdonly5,dfdonly)
dband.SetLineColor(0)
dband.SetFillColorAlpha(ROOT.kOrange-5,0.25)

anom.SetLineWidth(4)
anom.SetLineColor(ROOT.kOrange-3)
dnom.SetLineWidth(4)
dnom.SetLineColor(ROOT.kOrange-3)

anosyst.SetLineWidth(4)
anosyst.SetLineColor(ROOT.kOrange-3)
anosyst.SetLineStyle(2)
dnosyst.SetLineWidth(4)
dnosyst.SetLineColor(ROOT.kOrange-3)
dnosyst.SetLineStyle(2)

afdonly.SetLineWidth(4)
afdonly.SetLineColor(ROOT.kOrange+3)

dfdonly.SetLineWidth(4)
dfdonly.SetLineColor(ROOT.kOrange+3)

afdonly5.SetLineWidth(4)
afdonly5.SetLineColor(ROOT.kOrange-7)
afdonly10.SetLineWidth(4)
afdonly10.SetLineColor(ROOT.kOrange-5)
dfdonly5.SetLineWidth(4)
dfdonly5.SetLineColor(ROOT.kOrange-7)
dfdonly10.SetLineWidth(4)
dfdonly10.SetLineColor(ROOT.kOrange-5)

afdonly_w.SetLineWidth(4)
afdonly_w.SetLineColor(ROOT.kOrange+3)
afdonly_w.SetLineStyle(3)
dfdonly_w.SetLineWidth(4)
dfdonly_w.SetLineColor(ROOT.kOrange+3)
dfdonly_w.SetLineStyle(3)

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
realband.Draw("fsame")
anom.Draw("same")
anosyst.Draw("same")
afdonly.Draw("same")
afdonly5.Draw("same")
#afdonly10.Draw("same")
afdonly_w.Draw("same")
ROOT.gPad.RedrawAxis()

t1 = ROOT.TPaveText(0.16,0.7,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.AddText("10 years (staged)")      
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

null = ROOT.TObject()
l1 = ROOT.TLegend(0.52,0.65,0.89,0.89)
l1.AddEntry(anosyst,"No systematics", "L")
l1.AddEntry(anom,"Nominal Sensitivity", "L")
l1.AddEntry(null,"FD Only:","")
l1.AddEntry(afdonly_w,"Known Perfect Model", "L")
l1.AddEntry(afdonly,"1 Bias","L")
l1.AddEntry(afdonly5,"5 Biases","L")
#l1.AddEntry(afdonly10,"10 Biases","L")
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
outname = "plot/cpv/cpv_bias_notgif_2019.png"
c1.SaveAs(outname)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(-1.0,0.0,1.0,80.0)
h2.SetTitle("")
h2.GetXaxis().SetTitle("#delta_{CP}/#pi")
h2.GetXaxis().CenterTitle()
h2.GetYaxis().SetTitle("#delta_{CP} Resolution (degrees)")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
dband.Draw("fsame")
dnom.Draw("same")
dnosyst.Draw("same")
dfdonly.Draw("same")
dfdonly5.Draw("same")
dfdonly10.Draw("same")
dfdonly_w.Draw("same")
ROOT.gPad.RedrawAxis()

t1.Draw("same")
l1.Draw("same")
outname = "plot/res/dcpres_bias_notgif_2019.png"
c2.SaveAs(outname)
