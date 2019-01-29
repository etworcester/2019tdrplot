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

    
specfile = ROOT.TFile("root/spec_hist_v3_wt.root")

#Appearance FHC
h = specfile.Get("nue_fhc_ih_0pi").Rebin(2)
h_sig = specfile.Get("nue_fhc_sig_ih_0pi").Rebin(2)
h_sig_nu = specfile.Get("nue_fhc_sig_nu_ih_0pi").Rebin(2)
h_sig_anu = specfile.Get("nue_fhc_sig_anu_ih_0pi").Rebin(2)
h_beamnue = specfile.Get("nue_fhc_beambg_ih_0pi").Rebin(2)
h_numu = specfile.Get("nue_fhc_numubg_ih_0pi").Rebin(2)
h_nutau = specfile.Get("nue_fhc_nutaubg_ih_0pi").Rebin(2)
h_NC = specfile.Get("nue_fhc_ncbg_ih_0pi").Rebin(2)

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

nNC = h_NC.Integral(h_NC.FindBin(0.51),h_NC.FindBin(7.99))
nnumu = h_numu.Integral(h_numu.FindBin(0.51),h_numu.FindBin(7.99))
nnutau = h_nutau.Integral(h_nutau.FindBin(0.51),h_nutau.FindBin(7.99))
nbeamnue = h_beamnue.Integral(h_beamnue.FindBin(0.51),h_beamnue.FindBin(7.99))
nsig = h_sig.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
nsig2 = h.Integral(h.FindBin(0.51),h.FindBin(7.99)) - nNC - nnumu - nnutau - nbeamnue
nsig_nu = h_sig_nu.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
nsig_anu = h_sig_anu.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
ntot = h.Integral()

print "Signal: ", nsig, nsig2
print "Signal (nu): ", nsig_nu
print "Signal (anu): ", nsig_anu
print "NC: ", nNC
print "numu: ", nnumu
print "nutau: ", nnutau
print "beam nue: ", nbeamnue
print "Total all energies: ", ntot

t1 = ROOT.TPaveText(0.55,0.7,0.89,0.89,"NDC")
t1.AddText("DUNE #nu_{e} Appearance")
t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = 0, sin^{2}2#theta_{13} = 0.088")
t1.AddText("sin^{2}#theta_{23} = 0.580")
t1.AddText("3.5 years (staged)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
l1.AddEntry(h,"Signal (#nu_{e} + #bar{#nu}_{e}) CC", "LE")
l1.AddEntry(h_beamnue, "Beam (#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_numu, "(#nu_{#mu} + #bar{#nu}_{#mu}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")
l1.SetFillColor(0)
l1.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,175.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
h.Draw("HIST,same")
h.Draw("E,same")
hs.Draw("same")
t1.Draw("same")
l1.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot/spec_app_nu_ih.eps")

#Appearance RHC
h = specfile.Get("nue_rhc_ih_0pi").Rebin(2)
h_sig = specfile.Get("nue_rhc_sig_ih_0pi").Rebin(2)
h_sig_nu = specfile.Get("nue_rhc_sig_nu_ih_0pi").Rebin(2)
h_sig_anu = specfile.Get("nue_rhc_sig_anu_ih_0pi").Rebin(2)
h_beamnue = specfile.Get("nue_rhc_beambg_ih_0pi").Rebin(2)
h_numu = specfile.Get("nue_rhc_numubg_ih_0pi").Rebin(2)
h_nutau = specfile.Get("nue_rhc_nutaubg_ih_0pi").Rebin(2)
h_NC = specfile.Get("nue_rhc_ncbg_ih_0pi").Rebin(2)

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

nNC = h_NC.Integral(h_NC.FindBin(0.51),h_NC.FindBin(7.99))
nnumu = h_numu.Integral(h_numu.FindBin(0.51),h_numu.FindBin(7.99))
nnutau = h_nutau.Integral(h_nutau.FindBin(0.51),h_nutau.FindBin(7.99))
nbeamnue = h_beamnue.Integral(h_beamnue.FindBin(0.51),h_beamnue.FindBin(7.99))
nsig = h_sig.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
nsig_nu = h_sig_nu.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
nsig_anu = h_sig_anu.Integral(h_sig.FindBin(0.51),h_sig.FindBin(7.99))
nsig2 = h.Integral(h.FindBin(0.51),h.FindBin(7.99)) - nNC - nnumu - nnutau - nbeamnue
ntot = h.Integral()

print "Signal: ", nsig, nsig2
print "Signal (nu): ", nsig_nu
print "Signal (anu): ", nsig_anu
print "NC: ", nNC
print "numu: ", nnumu
print "nutau: ", nnutau
print "beam nue: ", nbeamnue
print "Total all energies: ", ntot

t1 = ROOT.TPaveText(0.55,0.7,0.89,0.89,"NDC")
t1.AddText("DUNE #bar{#nu}_{e} Appearance")
t1.AddText("Normal Ordering")
t1.AddText("#delta_{CP} = 0, sin^{2}2#theta_{13} = 0.088")
t1.AddText("sin^{2}#theta_{23} = 0.580")
t1.AddText("3.5 years (staged)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
l1.AddEntry(h,"Signal (#nu_{e} + #bar{#nu}_{e}) CC", "LE")
l1.AddEntry(h_beamnue, "Beam (#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_numu, "(#nu_{#mu} + #bar{#nu}_{#mu}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")
l1.SetFillColor(0)
l1.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,50.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
h.Draw("HIST,same")
h.Draw("E,same")
hs.Draw("same")
t1.Draw("same")
l1.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot/spec_app_anu_ih.eps")

#Disappearance FHC
h = specfile.Get("numu_fhc_ih_0pi").Rebin(2)
h_ws = specfile.Get("numu_fhc_wsbg_ih_0pi").Rebin(2)
h_nutau = specfile.Get("numu_fhc_nutaubg_ih_0pi").Rebin(2)
h_NC = specfile.Get("numu_fhc_ncbg_ih_0pi").Rebin(2)
h_sig = specfile.Get("numu_fhc_sig_ih_0pi").Rebin(2)
h_nue = specfile.Get("numu_fhc_nuebg_ih_0pi").Rebin(2)

geterrors(h)

h.SetLineWidth(3)
h_ws.SetLineWidth(3)
h_nutau.SetLineWidth(3)
h_NC.SetLineWidth(3)
h_nue.SetLineWidth(3)

h_ws.SetFillStyle(1001)
h_nutau.SetFillStyle(1001)
h_NC.SetFillStyle(1001)
h_nue.SetFillStyle(1001)

h_ws.SetLineColor(ROOT.kMagenta)
h_nutau.SetLineColor(ROOT.kCyan)
h_NC.SetLineColor(ROOT.kGreen)
h_nue.SetLineColor(ROOT.kBlue)

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
l1.AddEntry(h,"Signal #nu_{#mu} CC", "LE")
l1.AddEntry(h_ws,"#bar{#nu}_{#mu} CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_nue, "(#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")

l1.SetFillColor(0)
l1.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,750.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
hs.Draw("same")
h.Draw("HIST,same")
h.Draw("E,same")
t1.Draw("same")
l1.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot/spec_dis_nu_ih.eps")


#Disappearance RHC
h = specfile.Get("numu_rhc_ih_0pi").Rebin(2)
h_ws = specfile.Get("numu_rhc_wsbg_ih_0pi").Rebin(2)
h_nutau = specfile.Get("numu_rhc_nutaubg_ih_0pi").Rebin(2)
h_NC = specfile.Get("numu_rhc_ncbg_ih_0pi").Rebin(2)
h_sig = specfile.Get("numu_rhc_sig_ih_0pi").Rebin(2)
h_nue = specfile.Get("numu_rhc_nuebg_ih_0pi").Rebin(2)

geterrors(h)

h.SetLineWidth(3)
h_ws.SetLineWidth(3)
h_nutau.SetLineWidth(3)
h_NC.SetLineWidth(3)
h_nue.SetLineWidth(3)

h_ws.SetFillStyle(1001)
h_nutau.SetFillStyle(1001)
h_NC.SetFillStyle(1001)
h_nue.SetFillStyle(1001)

h_ws.SetLineColor(ROOT.kMagenta)
h_nutau.SetLineColor(ROOT.kCyan)
h_NC.SetLineColor(ROOT.kGreen)
h_nue.SetLineColor(ROOT.kBlue)

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
t1.AddText("DUNE #bar{#nu}_{#mu} Disappearance")
t1.AddText("sin^{2}#theta_{23} = 0.580")
t1.AddText("#Deltam^{2}_{32} = 2.451 #times 10^{-3} eV^{2}")
t1.AddText("3.5 years (staged)")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)

l1 = ROOT.TLegend(0.55,0.52,0.89,0.7)
l1.AddEntry(h,"Signal #bar{#nu}_{#mu} CC", "LE")
l1.AddEntry(h_ws,"#nu_{#mu} CC", "F")
l1.AddEntry(h_NC, "NC", "F")
l1.AddEntry(h_nue, "(#nu_{e} + #bar{#nu}_{e}) CC", "F")
l1.AddEntry(h_nutau, "(#nu_{#tau} + #bar{#nu}_{#tau}) CC", "F")

l1.SetFillColor(0)
l1.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,350.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
hs.Draw("same")
h.Draw("HIST,same")
h.Draw("E,same")
t1.Draw("same")
l1.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot/spec_dis_anu_ih.eps")


