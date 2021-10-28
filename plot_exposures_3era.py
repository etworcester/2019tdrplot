#!/usr/bin/env python

import sys
import math
import ctypes
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
      xup = ctypes.c_double(-9.9)
      yup = ctypes.c_double(-9.9)
      xlo = ctypes.c_double(-9.9)
      ylo = ctypes.c_double(-9.9)
      while i<n:
          up.GetPoint(i,xup,yup);
          down.GetPoint(n-i-1,xlo,ylo);
          diffgraph.SetPoint(i,xup,yup);
          diffgraph.SetPoint(n+i,xlo,ylo);
          i += 1
      return diffgraph;

def grange(g_in,ilo1,ihi1,ilo2,ihi2):
      print(g_in, ilo1, ihi1, ilo2, ihi2)
      n = g_in.GetN()
      g_out = ROOT.TGraph(ihi1-ilo1 + ihi2-ilo2);
      i = 0
      x = ctypes.c_double(-9.9)
      y = ctypes.c_double(-9.9)
      i = 0
      start=ilo1
      while (i+start)<ihi1:
          g_in.GetPoint(i+start,x,y)
          g_out.SetPoint(i,x,y)
          print(i, i+start, x, y)
          i += 1
      start = ilo2
      j = 0
      while (j+start)<ihi2:
            g_in.GetPoint(j+start,x,y)
            g_out.SetPoint(i,x,y)
            print(i, j+start, x, y)
            i += 1
            j+=1
      return g_out;

def gpoints(g_in,ilo1,ihi1):
      n = g_in.GetN()
      g_out = ROOT.TGraph(ihi1-ilo1);
      i = 0
      x = ctypes.c_double(-9.9)
      y = ctypes.c_double(-9.9)
      i = 0
      start=ilo1
      while (i+start)<ihi1:
          g_in.GetPoint(i+start,x,y)
          g_out.SetPoint(i,x,y)
          i += 1
      return g_out;


myfile = ROOT.TFile("root_v4/nospect_graphs.root")
cpv_dcpmax_nom = myfile.Get("fullND_dcpmax")
cpv_dcpmax_nospect = myfile.Get("LArNoSpect_dcpmax")
cpv_dcpmax_LArND = myfile.Get("LArTMS_dcpmax")

g_cpv_dcpmax = filldiff(cpv_dcpmax_nom,cpv_dcpmax_nospect)
g_cpv_dcpmax.SetFillColorAlpha(ROOT.kCyan-9, 0.7)
g_cpv_dcpmax.SetLineColor(0)
g_cpv_dcpmax_gray = g_cpv_dcpmax.Clone()
g_cpv_dcpmax_gray.SetFillColorAlpha(ROOT.kGray, 0.7)

myfile2 = ROOT.TFile("root_v4/exposure_graphs_notms_nh.root")
mh_nom = myfile2.Get("mhsig100_nom")
mh_nospect = myfile2.Get("mhsig100_notms")

cpv_dcpmax_nom.SetLineWidth(3)
cpv_dcpmax_nospect.SetLineWidth(3)
cpv_dcpmax_LArND.SetLineWidth(3)

cpv_dcpmax_nospect.SetLineStyle(3)
cpv_dcpmax_LArND.SetLineStyle(2)

cpv_dcpmax_nom.SetLineColor(ROOT.kCyan-3)
cpv_dcpmax_nospect.SetLineColor(ROOT.kCyan-3)
cpv_dcpmax_LArND.SetLineColor(ROOT.kCyan-3)

cpv_dcpmax_nom_gray = cpv_dcpmax_nom.Clone()
cpv_dcpmax_nospect_gray = cpv_dcpmax_nospect.Clone()
cpv_dcpmax_LArND_gray = cpv_dcpmax_LArND.Clone()

cpv_dcpmax_nom_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_nospect_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_LArND_gray.SetLineColor(ROOT.kGray+2)

cpv_dcp50pct_nom = myfile.Get("fullND_dcp50pct")
cpv_dcp50pct_nospect = myfile.Get("LArNoSpect_dcp50pct")
cpv_dcp50pct_LArND = myfile.Get("LArTMS_dcp50pct")

cpv_dcp50pct_nom.SetLineWidth(3)
cpv_dcp50pct_nospect.SetLineWidth(3)
cpv_dcp50pct_LArND.SetLineWidth(3)

cpv_dcp50pct_nospect.SetLineStyle(3)
cpv_dcp50pct_LArND.SetLineStyle(2)

cpv_dcp50pct_nom.SetLineColor(ROOT.kGreen-3)
cpv_dcp50pct_nospect.SetLineColor(ROOT.kGreen-3)
cpv_dcp50pct_LArND.SetLineColor(ROOT.kGreen-3)

g_cpv_dcp50pct = filldiff(cpv_dcp50pct_nom,cpv_dcp50pct_nospect)
g_cpv_dcp50pct.SetFillColorAlpha(ROOT.kGreen-9,0.7)
g_cpv_dcp50pct.SetLineColor(0)
g_cpv_dcp50pct_gray = g_cpv_dcp50pct.Clone()
g_cpv_dcp50pct_gray.SetFillColorAlpha(ROOT.kGray,0.7)

cpv_dcp50pct_nom_gray = cpv_dcp50pct_nom.Clone()
cpv_dcp50pct_nospect_gray = cpv_dcp50pct_nospect.Clone()
cpv_dcp50pct_LArND_gray = cpv_dcp50pct_LArND.Clone()

cpv_dcp50pct_nom_gray.SetLineColor(ROOT.kGray+2)
cpv_dcp50pct_nospect_gray.SetLineColor(ROOT.kGray+2)
cpv_dcp50pct_LArND_gray.SetLineColor(ROOT.kGray+2)

mh_nom.SetLineWidth(3)
mh_nospect.SetLineWidth(3)
mh_nospect.SetLineStyle(3)

mh_nom.SetLineColor(ROOT.kMagenta-3)
mh_nospect.SetLineColor(ROOT.kMagenta-3)

g_mh = filldiff(mh_nom,mh_nospect)
g_mh.SetFillColor(ROOT.kMagenta-9)
g_mh.SetLineColor(0)
g_mh_gray = g_mh.Clone()
g_mh_gray.SetFillColor(ROOT.kGray)

mh_nom_gray = mh_nom.Clone()
mh_nospect_gray = mh_nospect.Clone()

mh_nom_gray.SetLineColor(ROOT.kGray+2)
mh_nospect_gray.SetLineColor(ROOT.kGray+2)


#Set up range plots in an organized way

#CPVMax
g_cpv_dcpmax_col_range = grange(g_cpv_dcpmax,4,7,21,24)
g_cpv_dcpmax_col_range.SetFillColorAlpha(ROOT.kCyan-9,0.7)
g_cpv_dcpmax_gray_r1 = grange(g_cpv_dcpmax,0,5,23,28)
g_cpv_dcpmax_gray_r1.SetFillColorAlpha(ROOT.kGray,0.7)
g_cpv_dcpmax_gray_r1.SetLineColor(0)
g_cpv_dcpmax_gray_r2 = grange(g_cpv_dcpmax,6,14,14,22)
g_cpv_dcpmax_gray_r2.SetFillColorAlpha(ROOT.kGray,0.7)
g_cpv_dcpmax_gray_r2.SetLineColor(0)

cpv_dcpmax_nom_range = gpoints(cpv_dcpmax_nom,4,7)
cpv_dcpmax_nospect_range = gpoints(cpv_dcpmax_nospect,4,7)
cpv_dcpmax_lar_range = gpoints(cpv_dcpmax_LArND,4,7)
cpv_dcpmax_nom_r1_gray = gpoints(cpv_dcpmax_nom,0,5)
cpv_dcpmax_nospect_r1_gray = gpoints(cpv_dcpmax_nospect,0,5)
cpv_dcpmax_lar_r1_gray = gpoints(cpv_dcpmax_LArND,0,5)
cpv_dcpmax_nom_r2_gray = gpoints(cpv_dcpmax_nom,6,14)
cpv_dcpmax_nospect_r2_gray = gpoints(cpv_dcpmax_nospect,6,14)
cpv_dcpmax_lar_r2_gray = gpoints(cpv_dcpmax_LArND,6,14)

cpv_dcpmax_nom_range.SetLineColor(ROOT.kCyan-3)
cpv_dcpmax_nospect_range.SetLineColor(ROOT.kCyan-3)
cpv_dcpmax_lar_range.SetLineColor(ROOT.kCyan-3)
cpv_dcpmax_nospect_range.SetLineStyle(3)
cpv_dcpmax_lar_range.SetLineStyle(2)
cpv_dcpmax_nom_r1_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_nospect_r1_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_lar_r1_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_nospect_r1_gray.SetLineStyle(3)
cpv_dcpmax_lar_r1_gray.SetLineStyle(2)
cpv_dcpmax_nom_r2_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_nospect_r2_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_lar_r2_gray.SetLineColor(ROOT.kGray+2)
cpv_dcpmax_nospect_r2_gray.SetLineStyle(3)
cpv_dcpmax_lar_r2_gray.SetLineStyle(2)

#CPV50pct
g_cpv_dcp50pct_col_range = grange(g_cpv_dcp50pct,6,14,15,22)
g_cpv_dcp50pct_col_range.SetFillColorAlpha(ROOT.kGreen-9,0.7)
g_cpv_dcp50pct_range_gray = grange(g_cpv_dcp50pct,0,7,21,28)
g_cpv_dcp50pct_range_gray.SetFillColorAlpha(ROOT.kGray,0.7)
g_cpv_dcp50pct_range_gray.SetLineColor(0)

cpv_dcp50pct_nom_range = gpoints(cpv_dcp50pct_nom,6,14)
cpv_dcp50pct_nospect_range = gpoints(cpv_dcp50pct_nospect,6,14)
cpv_dcp50pct_lar_range = gpoints(cpv_dcp50pct_LArND,6,14)
cpv_dcp50pct_nom_range_gray = gpoints(cpv_dcp50pct_nom,0,7)
cpv_dcp50pct_nospect_range_gray = gpoints(cpv_dcp50pct_nospect,0,7)
cpv_dcp50pct_lar_range_gray = gpoints(cpv_dcp50pct_LArND,0,7)

cpv_dcp50pct_nom_range.SetLineColor(ROOT.kGreen-3)
cpv_dcp50pct_nospect_range.SetLineColor(ROOT.kGreen-3)
cpv_dcp50pct_lar_range.SetLineColor(ROOT.kGreen-3)
cpv_dcp50pct_nospect_range.SetLineStyle(3)
cpv_dcp50pct_lar_range.SetLineStyle(2)
cpv_dcp50pct_nom_range_gray.SetLineColor(ROOT.kGray+2)
cpv_dcp50pct_nospect_range_gray.SetLineColor(ROOT.kGray+2)
cpv_dcp50pct_lar_range_gray.SetLineColor(ROOT.kGray+2)
cpv_dcp50pct_nospect_range_gray.SetLineStyle(3)
cpv_dcp50pct_lar_range_gray.SetLineStyle(2)

#MH
g_mh_col_range = grange(g_mh,0,5,13,17)
g_mh_col_range.SetFillColor(ROOT.kMagenta-9)
g_mh_gray_range = grange(g_mh_gray,4,8,9,14)
g_mh_gray_range.SetFillColor(ROOT.kGray)
g_mh_gray_range.SetLineColor(0)

mh_nom_range = gpoints(mh_nom,0,5)
mh_nospect_range = gpoints(mh_nospect,0,5)
mh_nom_range_gray = gpoints(mh_nom,4,9)
mh_nospect_range_gray = gpoints(mh_nospect,4,9)

mh_nom_range.SetLineColor(ROOT.kMagenta-3)
mh_nospect_range.SetLineColor(ROOT.kMagenta-3)
mh_nospect_range.SetLineStyle(3)
mh_nom_range_gray.SetLineColor(ROOT.kGray+2)
mh_nospect_range_gray.SetLineColor(ROOT.kGray+2)
mh_nospect_range_gray.SetLineStyle(3)


c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,336.0,8.0)
h1.SetTitle("DUNE Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
g_cpv_dcpmax.Draw("Fsame")
cpv_dcpmax_nom.Draw("Lsame")
cpv_dcpmax_nospect.Draw("Lsame")
cpv_dcpmax_LArND.Draw("Lsame")

g_cpv_dcp50pct.Draw("Fsame")
cpv_dcp50pct_nom.Draw("Lsame")
cpv_dcp50pct_nospect.Draw("Lsame")
cpv_dcp50pct_LArND.Draw("Lsame")

g_mh.Draw("Fsame")
mh_nom.Draw("Lsame")
mh_nospect.Draw("Lsame")

b1 = ROOT.TBox(10,5.5,330,8.0)
b1.SetLineColor(0)
b1.SetFillColor(0)
b1.Draw("same")

t1 = ROOT.TPaveText(0.16,0.68,0.5,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.52,0.6,0.89,0.89)
l1.AddEntry(g_mh,"Mass Ordering (100% of #delta_{CP} values)","F")
l1.AddEntry(g_cpv_dcpmax,"CP Violation (#delta_{CP} = -#pi/2)","F")
l1.AddEntry(g_cpv_dcp50pct,"CP Violation (50% of #delta_{CP} values)","F")
l1.AddEntry(cpv_dcpmax_nom_gray, "Reference Near Detector","L")
l1.AddEntry(cpv_dcpmax_LArND_gray,"ND-LAr + TMS","L")
l1.AddEntry(cpv_dcpmax_nospect_gray,"ND-LAr (no spectrometer)","L")
l1.SetBorderSize(0)
l1.SetFillColor(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,336.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,336.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_3era_all.pdf"
c1.SaveAs(outname)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,336.0,8.0)
h2.SetTitle("DUNE Sensitivity")
h2.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()

#g_cpv_dcpmax_gray.Draw("Fsame")
#cpv_dcpmax_nom_gray.Draw("Lsame")
#cpv_dcpmax_nospect_gray.Draw("Lsame")
#cpv_dcpmax_LArND_gray.Draw("Lsame")

#g_cpv_dcp50pct_gray.Draw("Fsame")
#cpv_dcp50pct_nom_gray.Draw("Lsame")
#cpv_dcp50pct_nospect_gray.Draw("Lsame")
#cpv_dcp50pct_LArND_gray.Draw("Lsame")

g_mh_col_range.Draw("Fsame")
mh_nom_range.Draw("Lsame")
mh_nospect_range.Draw("Lsame")
g_mh_gray_range.Draw("Fsame")
mh_nom_range_gray.Draw("Lsame")
mh_nospect_range_gray.Draw("Lsame")

b1.Draw("same")
t1.Draw("same")


l2 = ROOT.TLegend(0.52,0.6,0.89,0.89)
l2.AddEntry(g_mh,"Mass Ordering (100% of #delta_{CP} values)","F")
l2.AddEntry(g_cpv_dcpmax_gray,"CP Violation (#delta_{CP} = -#pi/2)","F")
l2.AddEntry(g_cpv_dcp50pct_gray,"CP Violation (50% of #delta_{CP} values)","F")
l2.AddEntry(mh_nom, "Reference Near Detector","L")
l2.AddEntry(cpv_dcpmax_LArND_gray,"ND-LAr + TMS","L")
l2.AddEntry(mh_nospect,"ND-LAr (no spectrometer)","L")
l2.SetBorderSize(0)
l2.SetFillColor(0)
l2.Draw("same")

line1.Draw("same")
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_3era_r1.pdf"
c2.SaveAs(outname)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.0,336.0,8.0)
h3.SetTitle("DUNE Sensitivity")
h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h3.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h3.GetYaxis().SetTitleOffset(1.3)
h3.GetYaxis().CenterTitle()
c3.Modified()

#g_cpv_dcp50pct_gray.Draw("Fsame")
#cpv_dcp50pct_nom_gray.Draw("Lsame")
#cpv_dcp50pct_nospect_gray.Draw("Lsame")
#cpv_dcp50pct_LArND_gray.Draw("Lsame")

#g_mh_gray.Draw("Fsame")
#mh_nom_gray.Draw("Lsame")
#mh_nospect_gray.Draw("Lsame")

g_cpv_dcpmax_col_range.Draw("Fsame")
cpv_dcpmax_nom_range.Draw("Lsame")
cpv_dcpmax_nospect_range.Draw("Lsame")
cpv_dcpmax_lar_range.Draw("Lsame")

g_cpv_dcpmax_gray_r1.Draw("Fsame")
cpv_dcpmax_nom_r1_gray.Draw("Lsame")
cpv_dcpmax_lar_r1_gray.Draw("Lsame")
cpv_dcpmax_nospect_r1_gray.Draw("Lsame")

g_cpv_dcpmax_gray_r2.Draw("Fsame")
cpv_dcpmax_nom_r2_gray.Draw("Lsame")
cpv_dcpmax_lar_r2_gray.Draw("Lsame")
cpv_dcpmax_nospect_r2_gray.Draw("Lsame")

b1.Draw("same")
t1.Draw("same")

l3 = ROOT.TLegend(0.52,0.6,0.89,0.89)
l3.AddEntry(g_mh_gray,"Mass Ordering (100% of #delta_{CP} values)","F")
l3.AddEntry(g_cpv_dcpmax,"CP Violation (#delta_{CP} = -#pi/2)","F")
l3.AddEntry(g_cpv_dcp50pct_gray,"CP Violation (50% of #delta_{CP} values)","F")
l3.AddEntry(cpv_dcpmax_nom, "Reference Near Detector","L")
l3.AddEntry(cpv_dcpmax_LArND,"ND-LAr + TMS","L")
l3.AddEntry(cpv_dcpmax_nospect,"ND-LAr (no spectrometer)","L")
l3.SetBorderSize(0)
l3.SetFillColor(0)
l3.Draw("same")

line1.Draw("same")
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_3era_r2.pdf"
c3.SaveAs(outname)

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0,0.0,336.0,8.0)
h4.SetTitle("DUNE Sensitivity")
h4.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h4.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h4.GetYaxis().SetTitleOffset(1.3)
h4.GetYaxis().CenterTitle()
c4.Modified()

#g_cpv_dcp50pct_gray.Draw("Fsame")
#cpv_dcp50pct_nom_gray.Draw("Lsame")
#cpv_dcp50pct_nospect_gray.Draw("Lsame")
#cpv_dcp50pct_LArND_gray.Draw("Lsame")

#g_mh_gray.Draw("Fsame")
#mh_nom_gray.Draw("Lsame")
#mh_nospect_gray.Draw("Lsame")

g_cpv_dcp50pct_col_range.Draw("Fsame")
cpv_dcp50pct_nom_range.Draw("Lsame")
cpv_dcp50pct_nospect_range.Draw("Lsame")
cpv_dcp50pct_lar_range.Draw("Lsame")

g_cpv_dcp50pct_range_gray.Draw("Fsame")
cpv_dcp50pct_nom_range_gray.Draw("Lsame")
cpv_dcp50pct_lar_range_gray.Draw("Lsame")
cpv_dcp50pct_nospect_range_gray.Draw("Lsame")

b1.Draw("same")
t1.Draw("same")

l4 = ROOT.TLegend(0.52,0.6,0.89,0.89)
l4.AddEntry(g_mh_gray,"Mass Ordering (100% of #delta_{CP} values)","F")
l4.AddEntry(g_cpv_dcpmax_gray,"CP Violation (#delta_{CP} = -#pi/2)","F")
l4.AddEntry(g_cpv_dcp50pct,"CP Violation (50% of #delta_{CP} values)","F")
l4.AddEntry(cpv_dcp50pct_nom, "Reference Near Detector","L")
l4.AddEntry(cpv_dcp50pct_LArND,"ND-LAr + TMS","L")
l4.AddEntry(cpv_dcp50pct_nospect,"ND-LAr (no spectrometer)","L")
l4.SetBorderSize(0)
l4.SetFillColor(0)
l4.Draw("same")

line1.Draw("same")
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_3era_r3.pdf"
c4.SaveAs(outname)

