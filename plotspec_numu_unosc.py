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

    
specfile = ROOT.TFile("root_v4/spec_hist_v4_wt.root")

#Disappearance FHC
h = specfile.Get("numu_fhc_nh_0pi").Rebin(2)
h_ws = specfile.Get("numu_fhc_wsbg_nh_0pi").Rebin(2)
h_nutau = specfile.Get("numu_fhc_nutaubg_nh_0pi").Rebin(2)
h_NC = specfile.Get("numu_fhc_ncbg_nh_0pi").Rebin(2)
h_sig = specfile.Get("numu_fhc_sig_nh_0pi").Rebin(2)
h_nue = specfile.Get("numu_fhc_nuebg_nh_0pi").Rebin(2)

h_unosc = specfile.Get("numu_fhc_unosc_sig").Rebin(2)

geterrors(h)

h.SetLineWidth(3)
h_ws.SetLineWidth(3)
h_nutau.SetLineWidth(3)
h_NC.SetLineWidth(3)
h_nue.SetLineWidth(3)
h_unosc.SetLineWidth(3)

h_ws.SetFillStyle(1001)
h_nutau.SetFillStyle(1001)
h_NC.SetFillStyle(1001)
h_nue.SetFillStyle(1001)

h_ws.SetLineColor(ROOT.kMagenta)
h_nutau.SetLineColor(ROOT.kCyan)
h_NC.SetLineColor(ROOT.kGreen)
h_nue.SetLineColor(ROOT.kBlue)

h_unosc.SetLineStyle(2)

h_ws.SetFillColor(ROOT.kMagenta)
h_nutau.SetFillColor(ROOT.kCyan)
h_NC.SetFillColor(ROOT.kGreen)
h_nue.SetFillColor(ROOT.kBlue)

hs = ROOT.THStack("hs","Stacked spectrum")
hs.Add(h_nutau,"HIST")
hs.Add(h_nue,"HIST")
hs.Add(h_NC,"HIST")
hs.Add(h_ws,"HIST")

nNC = h_NC.Integral(h_NC.FindBin(0.51),h_NC.FindBin(7.99))
nnutau = h_nutau.Integral(h_nutau.FindBin(0.51),h_nutau.FindBin(7.99))
nws = h_ws.Integral(h_ws.FindBin(0.51),h_ws.FindBin(7.99))
nsig = h_sig.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
nnue = h_nue.Integral(h_nue.FindBin(0.51),h_nue.FindBin(7.99))
nsig2 = h.Integral(h.FindBin(0.51),h.FindBin(7.99)) - nNC - nnutau - nws -nnue

print "Signal: ", nsig, nsig2
print "NC: ", nNC
print "nutau: ", nnutau
print "wrong sign: ", nws
print "nue: ", nnue

t1 = ROOT.TPaveText(0.55,0.7,0.89,0.89,"NDC")
t1.AddText("DUNE #nu_{#mu} Disappearance")
t1.AddText("sin^{2}#theta_{23} = 0.580")
t1.AddText("#Deltam^{2}_{32} = 2.451 #times 10^{-3} eV^{2}")
t1.AddText("3.5 years (staged)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
l1.AddEntry(h_unosc,"Unoscillated #nu_{#mu}","L") 
l1.AddEntry(h,"Signal #nu_{#mu} CC", "L")
l1.AddEntry(h_ws,"#bar{#nu}_{#mu} CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_nue, "(#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")

l1.SetFillColor(0)
l1.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,2000.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
h_unosc.Draw("HIST same")
hs.Draw("same")
h.Draw("HIST,same")
t1.Draw("same")
l1.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot_v4/spec_dis_nu_no_unosc.eps")
c1.SaveAs("plot_v4/spec_dis_nu_no_unosc.png")


# #Disappearance RHC
# h = specfile.Get("numu_rhc_nh_0pi").Rebin(2)
# h_ws = specfile.Get("numu_rhc_wsbg_nh_0pi").Rebin(2)
# h_nutau = specfile.Get("numu_rhc_nutaubg_nh_0pi").Rebin(2)
# h_NC = specfile.Get("numu_rhc_ncbg_nh_0pi").Rebin(2)
# h_sig = specfile.Get("numu_rhc_sig_nh_0pi").Rebin(2)
# h_nue = specfile.Get("numu_rhc_nuebg_nh_0pi").Rebin(2)
# h_unosc = specfile.Get("numu_rhc_unosc_sig")
# geterrors(h)

# h.SetLineWidth(3)
# h_ws.SetLineWidth(3)
# h_nutau.SetLineWidth(3)
# h_NC.SetLineWidth(3)
# h_nue.SetLineWidth(3)
# h_unosc.SetLineWidth(3)

# h_ws.SetFillStyle(1001)
# h_nutau.SetFillStyle(1001)
# h_NC.SetFillStyle(1001)
# h_nue.SetFillStyle(1001)

# h_ws.SetLineColor(ROOT.kMagenta)
# h_nutau.SetLineColor(ROOT.kCyan)
# h_NC.SetLineColor(ROOT.kGreen)
# h_nue.SetLineColor(ROOT.kBlue)

# h_unosc.SetLineStyle(2)

# h_ws.SetFillColor(ROOT.kMagenta)
# h_nutau.SetFillColor(ROOT.kCyan)
# h_NC.SetFillColor(ROOT.kGreen)
# h_nue.SetFillColor(ROOT.kBlue)

# hs = ROOT.THStack("hs","Stacked spectrum")
# hs.Add(h_nutau,"HIST")
# hs.Add(h_nue,"HIST")
# hs.Add(h_NC,"HIST")
# hs.Add(h_ws,"HIST")

# nNC = h_NC.Integral(h_NC.FindBin(0.51),h_NC.FindBin(7.99))
# nnutau = h_nutau.Integral(h_nutau.FindBin(0.51),h_nutau.FindBin(7.99))
# nws = h_ws.Integral(h_ws.FindBin(0.51),h_ws.FindBin(7.99))
# nsig = h_sig.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
# nnue = h_nue.Integral(h_nue.FindBin(0.51),h_nue.FindBin(7.99))
# nsig2 = h.Integral(h.FindBin(0.51),h.FindBin(7.99)) - nNC - nnutau - nws -nnue

# print "Signal: ", nsig, nsig2
# print "NC: ", nNC
# print "nutau: ", nnutau
# print "wrong sign: ", nws
# print "nue: ", nnue

# t1 = ROOT.TPaveText(0.55,0.7,0.89,0.89,"NDC")
# t1.AddText("DUNE #bar{#nu}_{#mu} Disappearance")
# t1.AddText("sin^{2}#theta_{23} = 0.580")
# t1.AddText("#Deltam^{2}_{32} = 2.451 #times 10^{-3} eV^{2}")
# t1.AddText("3.5 years (staged)")
# t1.SetFillColor(0)
# t1.SetBorderSize(0)
# t1.SetTextAlign(12)

# l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
# l1.AddEntry(h_unosc,"Unoscillated #bar{#nu}_{#mu} + #nu_{#mu}","L")
# l1.AddEntry(h,"Signal #bar{#nu}_{#mu} CC", "L")
# l1.AddEntry(h_ws,"#nu_{#mu} CC", "F")
# l1.AddEntry(h_NC, "NC", "F")
# l1.AddEntry(h_nue, "(#nu_{e} + #bar{#nu}_{e}) CC", "F")
# l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")

# l1.SetFillColor(0)
# l1.SetBorderSize(0)

# c1 = ROOT.TCanvas("c1","c1",800,800)
# c1.SetLeftMargin(0.15)
# h1 = c1.DrawFrame(0.5,0.,8.,350.)
# h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
# h1.GetYaxis().SetTitle("Events per 0.25 GeV")
# h1.GetYaxis().SetTitleOffset(1.5)
# hs.SetTitle("")
# hs.Draw("same")
# h_unosc.Draw("HIST,same")
# h.Draw("HIST,same")
# t1.Draw("same")
# l1.Draw("same")
# ROOT.gPad.RedrawAxis()
# c1.SaveAs("plot_v3/spec_dis_anu_no_unosc.eps")
# c1.SaveAs("plot_v3/spec_dis_anu_no_unosc.png")


