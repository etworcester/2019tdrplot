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


myfile = ROOT.TFile("root_v4/bias_graphs_nd_day1.root")
cpv_dcpmax_nom = myfile.Get("cpv_dcpmax_fullND")
cpv_dcpmax_noND_1nw = myfile.Get("cpv_dcpmax_01NuWros_noND")
cpv_dcpmax_noND_5nw = myfile.Get("cpv_dcpmax_03NuWros_noND")
cpv_dcpmax_LArND_1nw = myfile.Get("cpv_dcpmax_01NuWros_LArND")
cpv_dcpmax_LArND_5nw = myfile.Get("cpv_dcpmax_03NuWros_LArND")

cpv_dcpmax_nom.SetLineWidth(4)
cpv_dcpmax_noND_1nw.SetLineWidth(4)
cpv_dcpmax_noND_5nw.SetLineWidth(4)
cpv_dcpmax_LArND_1nw.SetLineWidth(4)
cpv_dcpmax_LArND_5nw.SetLineWidth(4)

band_noND = filldiff(cpv_dcpmax_noND_1nw, cpv_dcpmax_noND_5nw)
band_LArND = filldiff(cpv_dcpmax_LArND_1nw, cpv_dcpmax_LArND_5nw)

band_noND.SetFillColorAlpha(ROOT.kOrange+3,0.25)
band_LArND.SetFillColorAlpha(ROOT.kOrange-5,0.25)

cpv_dcpmax_nom.SetLineColor(ROOT.kOrange-3)
cpv_dcpmax_noND_1nw.SetLineColor(ROOT.kOrange+3)
cpv_dcpmax_noND_5nw.SetLineColor(ROOT.kOrange+3)
cpv_dcpmax_noND_1nw.SetLineStyle(2)
cpv_dcpmax_noND_5nw.SetLineStyle(3)
cpv_dcpmax_LArND_1nw.SetLineColor(ROOT.kOrange-5)
cpv_dcpmax_LArND_5nw.SetLineColor(ROOT.kOrange-5)
cpv_dcpmax_LArND_1nw.SetLineStyle(2)
cpv_dcpmax_LArND_5nw.SetLineStyle(3)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1000.0,12.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
band_noND.Draw("Fsame")
band_LArND.Draw("Fsame")
cpv_dcpmax_nom.Draw("Lsame")
cpv_dcpmax_noND_1nw.Draw("Lsame")
cpv_dcpmax_noND_5nw.Draw("Lsame")
cpv_dcpmax_LArND_1nw.Draw("Lsame")
cpv_dcpmax_LArND_5nw.Draw("Lsame")

t1 = ROOT.TPaveText(0.16,0.68,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

dum1 = cpv_dcpmax_noND_1nw.Clone()
dum5 = cpv_dcpmax_noND_5nw.Clone()
dum1.SetLineColor(ROOT.kGray+2)
dum5.SetLineColor(ROOT.kGray+2)
band_noND.SetLineColor(0)
band_LArND.SetLineColor(0)

l1 = ROOT.TLegend(0.57,0.68,0.89,0.89)
l1.AddEntry(cpv_dcpmax_nom, "Full ND","L")
l1.AddEntry(band_LArND,"Day 1 ND","F")
l1.AddEntry(band_noND,"No/Minimal ND","F")
l1.AddEntry(dum1,"1 Bias","L")
l1.AddEntry(dum5,"3 Biases","L")
#l1.AddEntry(graph_cpvrange50, "50% of #delta_{CP} values","F")
#l1.AddEntry(graph_cpvrange75, "75% of #delta_{CP} values","F")
#l1.AddEntry(g_cpvsig_75_hi,"Nominal Analysis","L")
#l1.AddEntry(g_cpvsig_75_lo,"#theta_{13} unconstrained","L")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,1000.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1000.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_nuwrobias_nd_max_2019_v4_30jan.eps"
outname2 = "plot_v4/exposures/cpv_exp_nuwrobias_nd_max_2019_v4_30jan.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

cpv_dcp50pct_nom = myfile.Get("cpv_dcp50pct_fullND")
cpv_dcp50pct_noND_1nw = myfile.Get("cpv_dcp50pct_01NuWros_noND")
cpv_dcp50pct_noND_5nw = myfile.Get("cpv_dcp50pct_03NuWros_noND")
cpv_dcp50pct_LArND_1nw = myfile.Get("cpv_dcp50pct_01NuWros_LArND")
cpv_dcp50pct_LArND_5nw = myfile.Get("cpv_dcp50pct_03NuWros_LArND")

cpv_dcp50pct_nom.SetLineWidth(4)
cpv_dcp50pct_noND_1nw.SetLineWidth(4)
cpv_dcp50pct_noND_5nw.SetLineWidth(4)
cpv_dcp50pct_LArND_1nw.SetLineWidth(4)
cpv_dcp50pct_LArND_5nw.SetLineWidth(4)

cpv_dcp50pct_nom.SetLineWidth(4)
cpv_dcp50pct_noND_1nw.SetLineWidth(4)
cpv_dcp50pct_noND_5nw.SetLineWidth(4)
cpv_dcp50pct_LArND_1nw.SetLineWidth(4)
cpv_dcp50pct_LArND_5nw.SetLineWidth(4)

band_50pct_noND = filldiff(cpv_dcp50pct_noND_1nw, cpv_dcp50pct_noND_5nw)
band_50pct_LArND = filldiff(cpv_dcp50pct_LArND_1nw, cpv_dcp50pct_LArND_5nw)

band_50pct_noND.SetFillColorAlpha(ROOT.kOrange+3,0.25)
band_50pct_LArND.SetFillColorAlpha(ROOT.kOrange-5,0.25)

cpv_dcp50pct_nom.SetLineColor(ROOT.kOrange-3)
cpv_dcp50pct_noND_1nw.SetLineColor(ROOT.kOrange+3)
cpv_dcp50pct_noND_5nw.SetLineColor(ROOT.kOrange+3)
cpv_dcp50pct_noND_1nw.SetLineStyle(2)
cpv_dcp50pct_noND_5nw.SetLineStyle(3)
cpv_dcp50pct_LArND_1nw.SetLineColor(ROOT.kOrange-5)
cpv_dcp50pct_LArND_5nw.SetLineColor(ROOT.kOrange-5)
cpv_dcp50pct_LArND_1nw.SetLineStyle(2)
cpv_dcp50pct_LArND_5nw.SetLineStyle(3)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,1000.0,12.0)
h2.SetTitle("CP Violation Sensitivity")
h2.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h2.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
band_50pct_noND.Draw("Fsame")
band_50pct_LArND.Draw("Fsame")
cpv_dcp50pct_nom.Draw("Lsame")
cpv_dcp50pct_noND_1nw.Draw("Lsame")
cpv_dcp50pct_noND_5nw.Draw("Lsame")
cpv_dcp50pct_LArND_1nw.Draw("Lsame")
cpv_dcp50pct_LArND_5nw.Draw("Lsame")

t2 = ROOT.TPaveText(0.16,0.68,0.6,0.89,"NDC")
t2.AddText("DUNE Sensitivity")
t2.AddText("All Systematics")
t2.AddText("Normal Ordering")
t2.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t2.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t2.AddText("50% of #delta_{CP} values")
t2.SetFillStyle(0)
t2.SetBorderSize(0)
t2.SetTextAlign(12)
t2.Draw("same")

band_50pct_noND.SetLineWidth(0)
band_50pct_LArND.SetLineWidth(0)

l1.Draw("same")

line1 = ROOT.TLine(0.,3.,1000.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1000.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

outname = "plot_v4/exposures/cpv_exp_nuwrobias_nd_50pc_2019_v4_30jan.eps"
outname2 = "plot_v4/exposures/cpv_exp_nuwrobias_nd_50pc_2019_v4_30jan.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)

myfile2 = ROOT.TFile("root_v4/exposure_graphs_nh.root")
res_dcpmax_nom = myfile2.Get("dcpresneg_th13pen")

myfile3 = ROOT.TFile("root_v4/res_vs_exposure_nd.root")
res_dcpmax_noND_1nw = myfile3.Get("dcp_res_asimov11_noND_01bias")
res_dcpmax_noND_5nw = myfile3.Get("dcp_res_asimov11_noND_03bias")
res_dcpmax_LArND_1nw = myfile3.Get("dcp_res_asimov11_LArND_01bias")
res_dcpmax_LArND_5nw = myfile3.Get("dcp_res_asimov11_LArND_03bias")

res_dcpmax_nom.SetLineWidth(4)
res_dcpmax_noND_1nw.SetLineWidth(4)
res_dcpmax_noND_5nw.SetLineWidth(4)
res_dcpmax_LArND_1nw.SetLineWidth(4)
res_dcpmax_LArND_5nw.SetLineWidth(4)

band_resmax_noND = filldiff(res_dcpmax_noND_5nw, res_dcpmax_noND_1nw)
band_resmax_LArND = filldiff(res_dcpmax_LArND_5nw, res_dcpmax_LArND_1nw)

band_resmax_noND.SetFillColorAlpha(ROOT.kOrange+3,0.25)
band_resmax_LArND.SetFillColorAlpha(ROOT.kOrange-5,0.25)

res_dcpmax_nom.SetLineColor(ROOT.kOrange-3)
res_dcpmax_noND_1nw.SetLineColor(ROOT.kOrange+3)
res_dcpmax_noND_5nw.SetLineColor(ROOT.kOrange+3)
res_dcpmax_noND_1nw.SetLineStyle(2)
res_dcpmax_noND_5nw.SetLineStyle(3)
res_dcpmax_LArND_1nw.SetLineColor(ROOT.kOrange-5)
res_dcpmax_LArND_5nw.SetLineColor(ROOT.kOrange-5)
res_dcpmax_LArND_1nw.SetLineStyle(2)
res_dcpmax_LArND_5nw.SetLineStyle(3)

c3 = ROOT.TCanvas("c3","c3",800,800)
c3.SetLeftMargin(0.15)
h3 = c3.DrawFrame(0,0.0,1500.0,80.0)
h3.SetTitle("")
h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h3.GetYaxis().SetTitle("#delta_{cp} resolution (degrees)")
h3.GetYaxis().SetTitleOffset(1.3)
h3.GetYaxis().CenterTitle()
c3.Modified()
band_resmax_noND.Draw("Fsame")
band_resmax_LArND.Draw("Fsame")
res_dcpmax_nom.Draw("Lsame")
res_dcpmax_noND_1nw.Draw("Lsame")
res_dcpmax_noND_5nw.Draw("Lsame")
res_dcpmax_LArND_1nw.Draw("Lsame")
res_dcpmax_LArND_5nw.Draw("Lsame")

t1 = ROOT.TPaveText(0.16,0.68,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1.Draw("same")


outname = "plot_v4/res/dcpres_exp_nuwrobias_nd_max_2019_v4.eps"
outname2 = "plot_v4/res/dcpres_exp_nuwrobias_nd_max_2019_v4.png"
c3.SaveAs(outname)
c3.SaveAs(outname2)


res_dcpz_nom = myfile2.Get("dcpres0_th13pen")
res_dcpz_noND_1nw = myfile3.Get("dcp_res_asimov10_noND_01bias")
res_dcpz_noND_5nw = myfile3.Get("dcp_res_asimov10_noND_03bias")
res_dcpz_LArND_1nw = myfile3.Get("dcp_res_asimov10_LArND_01bias")
res_dcpz_LArND_5nw = myfile3.Get("dcp_res_asimov10_LArND_03bias")

res_dcpz_nom.SetLineWidth(4)
res_dcpz_noND_1nw.SetLineWidth(4)
res_dcpz_noND_5nw.SetLineWidth(4)
res_dcpz_LArND_1nw.SetLineWidth(4)
res_dcpz_LArND_5nw.SetLineWidth(4)

band_resz_noND = filldiff(res_dcpz_noND_5nw, res_dcpz_noND_1nw)
band_resz_LArND = filldiff(res_dcpz_LArND_5nw, res_dcpz_LArND_1nw)

band_resz_noND.SetFillColorAlpha(ROOT.kOrange+3,0.25)
band_resz_LArND.SetFillColorAlpha(ROOT.kOrange-5,0.25)

res_dcpz_nom.SetLineColor(ROOT.kOrange-3)
res_dcpz_noND_1nw.SetLineColor(ROOT.kOrange+3)
res_dcpz_noND_5nw.SetLineColor(ROOT.kOrange+3)
res_dcpz_noND_1nw.SetLineStyle(2)
res_dcpz_noND_5nw.SetLineStyle(3)
res_dcpz_LArND_1nw.SetLineColor(ROOT.kOrange-5)
res_dcpz_LArND_5nw.SetLineColor(ROOT.kOrange-5)
res_dcpz_LArND_1nw.SetLineStyle(2)
res_dcpz_LArND_5nw.SetLineStyle(3)

c4 = ROOT.TCanvas("c4","c4",800,800)
c4.SetLeftMargin(0.15)
h4 = c4.DrawFrame(0,0.0,1500.0,80.0)
h4.SetTitle("")
h4.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h4.GetYaxis().SetTitle("#delta_{cp} resolution (degrees)")
h4.GetYaxis().SetTitleOffset(1.3)
h4.GetYaxis().CenterTitle()
c4.Modified()
band_resz_noND.Draw("Fsame")
band_resz_LArND.Draw("Fsame")
res_dcpz_nom.Draw("Lsame")
res_dcpz_noND_1nw.Draw("Lsame")
res_dcpz_noND_5nw.Draw("Lsame")
res_dcpz_LArND_1nw.Draw("Lsame")
res_dcpz_LArND_5nw.Draw("Lsame")

t1 = ROOT.TPaveText(0.16,0.68,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("#delta_{CP} = 0")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1.Draw("same")


outname = "plot_v4/res/dcpres_exp_nuwrobias_nd_zero_2019_v4.eps"
outname2 = "plot_v4/res/dcpres_exp_nuwrobias_nd_zero_2019_v4.png"
c4.SaveAs(outname)
c4.SaveAs(outname2)

c5 = ROOT.TCanvas("c5","c5",800,800)
c5.SetLeftMargin(0.15)
h5 = c5.DrawFrame(0,0.0,200.0,8.0)
h5.SetTitle("Early CP Violation Sensitivity")
h5.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h5.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h5.GetYaxis().SetTitleOffset(1.3)
h5.GetYaxis().CenterTitle()
c1.Modified()
band_noND.Draw("Fsame")
band_LArND.Draw("Fsame")
cpv_dcpmax_nom.Draw("Lsame")
cpv_dcpmax_noND_1nw.Draw("Lsame")
cpv_dcpmax_noND_5nw.Draw("Lsame")
cpv_dcpmax_LArND_1nw.Draw("Lsame")
cpv_dcpmax_LArND_5nw.Draw("Lsame")

t1 = ROOT.TPaveText(0.16,0.68,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText("Normal Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
t1.AddText("#delta_{CP} = -#pi/2")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

t1.Draw("same")
l1.Draw("same")

line1a = ROOT.TLine(0.,3.,200.,3.)
line1a.SetLineStyle(2)
line1a.SetLineWidth(3)
line1a.Draw("same")

line2a = ROOT.TLine(0.0,5.,200.,5.)
line2a.SetLineStyle(2)
line2a.SetLineWidth(3)
line2a.Draw("same")


outname = "plot_v4/exposures/cpv_exp_nuwrobias_ndearly_max_2019_v4_30jan.eps"
outname2 = "plot_v4/exposures/cpv_exp_nuwrobias_ndearly_max_2019_v4_30jan.png"
c5.SaveAs(outname)
c5.SaveAs(outname2)
