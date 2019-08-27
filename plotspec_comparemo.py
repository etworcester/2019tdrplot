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

def geterrors(h):
    i = 0
    while i < h.GetNbinsX():
        err = math.sqrt(h.GetBinContent(i))
        h.SetBinError(i,err)
        i+=1

    
specfile = ROOT.TFile("root_v3/spec_hist_v3_wt.root")

#Appearance FHC
h = specfile.Get("nue_fhc_nh_0pi").Rebin(2)
h_sig = specfile.Get("nue_fhc_sig_nh_0pi").Rebin(2)
h_sig_nu = specfile.Get("nue_fhc_sig_nu_nh_0pi").Rebin(2)
h_sig_anu = specfile.Get("nue_fhc_sig_anu_nh_0pi").Rebin(2)
h_beamnue = specfile.Get("nue_fhc_beambg_nh_0pi").Rebin(2)
h_numu = specfile.Get("nue_fhc_numubg_nh_0pi").Rebin(2)
h_nutau = specfile.Get("nue_fhc_nutaubg_nh_0pi").Rebin(2)
h_NC = specfile.Get("nue_fhc_ncbg_nh_0pi").Rebin(2)

geterrors(h)

h.SetLineColor(ROOT.kBlack)
h_beamnue.SetLineColor(ROOT.kBlue)
h_numu.SetLineColor(ROOT.kMagenta)
h_nutau.SetLineColor(ROOT.kCyan)
h_NC.SetLineColor(ROOT.kGreen)

h_beamnue.SetFillStyle(1001)
h_numu.SetFillStyle(1001)
h_nutau.SetFillStyle(1001)
h_NC.SetFillStyle(1001)

h_beamnue.SetFillColor(ROOT.kBlue)
h_numu.SetFillColor(ROOT.kMagenta)
h_nutau.SetFillColor(ROOT.kCyan)
h_NC.SetFillColor(ROOT.kGreen)

h.SetLineWidth(3)
h_beamnue.SetLineWidth(3)
h_numu.SetLineWidth(3)
h_nutau.SetLineWidth(3)
h_NC.SetLineWidth(3)

hs = ROOT.THStack("hs","Stacked spectrum")
hs.Add(h_beamnue,"HIST")
hs.Add(h_NC,"HIST")
hs.Add(h_numu,"HIST")
hs.Add(h_nutau,"HIST")

#Appearance FHC (IO)
hio = specfile.Get("nue_fhc_ih_0pi").Rebin(2)

hio.SetLineColor(ROOT.kBlack)
hio.SetLineWidth(3)
hio.SetLineStyle(2)

t1 = ROOT.TPaveText(0.55,0.73,0.89,0.89,"NDC")
t1.AddText("DUNE #nu_{e} Appearance")
#t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = 0, sin^{2}2#theta_{13} = 0.088")
t1.AddText("sin^{2}#theta_{23} = 0.580")
t1.AddText("3.5 years (staged)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
l1.AddEntry(h,"Signal (#nu_{e} + #bar{#nu}_{e}) CC", "L")
l1.AddEntry(h_beamnue, "Beam (#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_numu, "(#nu_{#mu} + #bar{#nu}_{#mu}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")
l1.SetFillColor(0)
l1.SetBorderSize(0)

l2 = ROOT.TLegend(0.18,0.79,0.5,0.89)
l2.AddEntry(h,"Normal Ordering","L")
l2.AddEntry(hio,"Inverted Ordering","L")
l2.SetFillStyle(0)
l2.SetBorderSize(0)


c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,175.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
h.Draw("HIST,same")
hs.Draw("same")
hio.Draw("HIST,same")
t1.Draw("same")
l1.Draw("same")
l2.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot_v3/spec_app_nu_comparemo.eps")
c1.SaveAs("plot_v3/spec_app_nu_comparemo.png")

#Appearance RHC
h = specfile.Get("nue_rhc_nh_0pi").Rebin(2)
h_sig = specfile.Get("nue_rhc_sig_nh_0pi").Rebin(2)
h_sig_nu = specfile.Get("nue_rhc_sig_nu_nh_0pi").Rebin(2)
h_sig_anu = specfile.Get("nue_rhc_sig_anu_nh_0pi").Rebin(2)
h_beamnue = specfile.Get("nue_rhc_beambg_nh_0pi").Rebin(2)
h_numu = specfile.Get("nue_rhc_numubg_nh_0pi").Rebin(2)
h_nutau = specfile.Get("nue_rhc_nutaubg_nh_0pi").Rebin(2)
h_NC = specfile.Get("nue_rhc_ncbg_nh_0pi").Rebin(2)

geterrors(h)

h.SetLineColor(ROOT.kBlack)
h_beamnue.SetLineColor(ROOT.kBlue)
h_numu.SetLineColor(ROOT.kMagenta)
h_nutau.SetLineColor(ROOT.kCyan)
h_NC.SetLineColor(ROOT.kGreen)

h_beamnue.SetFillStyle(1001)
h_numu.SetFillStyle(1001)
h_nutau.SetFillStyle(1001)
h_NC.SetFillStyle(1001)

h_beamnue.SetFillColor(ROOT.kBlue)
h_numu.SetFillColor(ROOT.kMagenta)
h_nutau.SetFillColor(ROOT.kCyan)
h_NC.SetFillColor(ROOT.kGreen)

h.SetLineWidth(3)
h_beamnue.SetLineWidth(3)
h_numu.SetLineWidth(3)
h_nutau.SetLineWidth(3)
h_NC.SetLineWidth(3)

hs = ROOT.THStack("hs","Stacked spectrum")
hs.Add(h_beamnue,"HIST")
hs.Add(h_NC,"HIST")
hs.Add(h_numu,"HIST")
hs.Add(h_nutau,"HIST")

hio = specfile.Get("nue_rhc_ih_0pi").Rebin(2)
hio.SetLineColor(ROOT.kBlack)
hio.SetLineWidth(3)
hio.SetLineStyle(2)

t1 = ROOT.TPaveText(0.55,0.73,0.89,0.89,"NDC")
t1.AddText("DUNE #bar{#nu}_{e} Appearance")
#t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = 0, sin^{2}2#theta_{13} = 0.088")
t1.AddText("sin^{2}#theta_{23} = 0.580")
t1.AddText("3.5 years (staged)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
l1.AddEntry(h,"Signal (#nu_{e} + #bar{#nu}_{e}) CC", "L")
l1.AddEntry(h_beamnue, "Beam (#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_numu, "(#nu_{#mu} + #bar{#nu}_{#mu}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")
l1.SetFillColor(0)
l1.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,75.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
h.Draw("HIST,same")
hs.Draw("same")
hio.Draw("HIST,same")
t1.Draw("same")
l1.Draw("same")
l2.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot_v3/spec_app_anu_comparemo.eps")
c1.SaveAs("plot_v3/spec_app_anu_comparemo.png")

