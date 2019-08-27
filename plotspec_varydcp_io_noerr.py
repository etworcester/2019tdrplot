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

h = specfile.Get("nue_fhc_ih_0pi").Rebin(2)
h_dcppos = specfile.Get("nue_fhc_ih_piover2").Rebin(2)
h_dcpneg = specfile.Get("nue_fhc_ih_3piover2").Rebin(2)
h_sig = specfile.Get("nue_fhc_sig_ih_0pi").Rebin(2)
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

h_dcppos.SetLineColor(ROOT.kGray+2)
h_dcpneg.SetLineColor(ROOT.kGray+2)
h_dcppos.SetLineStyle(2)
h_dcpneg.SetLineStyle(3)
h_dcppos.SetLineWidth(3)
h_dcpneg.SetLineWidth(3)

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

print "Signal: ", nsig, nsig2
print "NC: ", nNC
print "numu: ", nnumu
print "nutau: ", nnutau
print "beam nue: ", nbeamnue

t1 = ROOT.TPaveText(0.55,0.7,0.89,0.89,"NDC")
t1.AddText("DUNE #nu_{e} Appearance")
t1.AddText("Inverted Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088")
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

l2 = ROOT.TLegend(0.61,0.35,0.8,0.45)
l2.AddEntry(h_dcpneg,"#delta_{CP} = -#pi/2","L")
l2.AddEntry(h,"#delta_{CP} = 0","L")
l2.AddEntry(h_dcppos,"#delta_{CP} = +#pi/2","L")
l2.SetFillStyle(0)
l2.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,175.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
hs.Draw("HIST, same")
h.Draw("HIST,same")
h.Draw("HIST,same")
h_dcppos.Draw("HIST,same")
h_dcpneg.Draw("HIST,same")
t1.Draw("same")
l1.Draw("same")
l2.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot_v3/spec_app_nu_varydcp_io_noerr.eps")
c1.SaveAs("plot_v3/spec_app_nu_varydcp_io_noerr.png")

#Anti-nu
h = specfile.Get("nue_rhc_ih_0pi").Rebin(2)
h_dcppos = specfile.Get("nue_rhc_ih_piover2").Rebin(2)
h_dcpneg = specfile.Get("nue_rhc_ih_3piover2").Rebin(2)
h_sig = specfile.Get("nue_rhc_sig_ih_0pi").Rebin(2)
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

h_dcppos.SetLineColor(ROOT.kGray+2)
h_dcpneg.SetLineColor(ROOT.kGray+2)
h_dcppos.SetLineStyle(2)
h_dcpneg.SetLineStyle(3)
h_dcppos.SetLineWidth(3)
h_dcpneg.SetLineWidth(3)

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

print "Signal: ", nsig, nsig2
print "NC: ", nNC
print "numu: ", nnumu
print "nutau: ", nnutau
print "beam nue: ", nbeamnue

t1 = ROOT.TPaveText(0.55,0.7,0.89,0.89,"NDC")
t1.AddText("DUNE #bar{#nu}_{e} Appearance")
t1.AddText("Inverted Ordering")
t1.AddText("sin^{2}2#theta_{13} = 0.088")
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

l2 = ROOT.TLegend(0.61,0.35,0.8,0.45)
l2.AddEntry(h_dcpneg,"#delta_{CP} = -#pi/2","L")
l2.AddEntry(h,"#delta_{CP} = 0","L")
l2.AddEntry(h_dcppos,"#delta_{CP} = +#pi/2","L")
l2.SetFillStyle(0)
l2.SetBorderSize(0)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0.5,0.,8.,75.)
h1.GetXaxis().SetTitle("Reconstructed Energy (GeV)")
h1.GetYaxis().SetTitle("Events per 0.25 GeV")
h1.GetYaxis().SetTitleOffset(1.5)
hs.SetTitle("")
hs.Draw("HIST,same")
h.Draw("HIST,same")
h.Draw("HIST,same")
h_dcppos.Draw("HIST,same")
h_dcpneg.Draw("HIST,same")
t1.Draw("same")
l1.Draw("same")
l2.Draw("same")
ROOT.gPad.RedrawAxis()
c1.SaveAs("plot_v3/spec_app_anu_varydcp_io_noerr.eps")
c1.SaveAs("plot_v3/spec_app_anu_varydcp_io_noerr.png")

