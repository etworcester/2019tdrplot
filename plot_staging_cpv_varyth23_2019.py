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

def filldiff(up,down,mid):
      n = up.GetN()
      diffgraph = ROOT.TGraph(2*n)
      i = 0
      xup = ROOT.Double(-9.9)
      yup = ROOT.Double(-9.9)
      xlo = ROOT.Double(-9.9)
      ylo = ROOT.Double(-9.9)
      xmid = ROOT.Double(-9.9)
      ymid = ROOT.Double(-9.9)

      while i<n:
            up.GetPoint(i,xup,yup)
            mid.GetPoint(i,xmid,ymid)
            down.GetPoint(i,xlo,ylo)
            yval = max(yup,ymid)
            yval = max(yval,ylo)

            diffgraph.SetPoint(i,xup,yval)

            up.GetPoint(n-i-1,xup,yup)
            down.GetPoint(n-i-1,xlo,ylo)
            mid.GetPoint(n-i-1,xmid,ymid)
            yval = min(yup,ymid)
            yval = min(yval,ylo)
            diffgraph.SetPoint(n+i,xlo,yval)

            i += 1
      return diffgraph

hier = sys.argv[1]
if (hier == 'nh'):
      htext = "Normal Ordering"
      hnum = "1"
elif (hier == 'ih'):
      htext = "Inverted Ordering"
      hnum = "-1"
else:
      print "Must supply nh or ih!"
      exit()

g_cpvsig_75_lo_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig75_q23lo")
g_cpvsig_50_lo_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig50_q23lo")
g_cpvsig_best_lo_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsigbest_q23lo")

g_cpvsig_75_hi_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig75_q23hi")
g_cpvsig_50_hi_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig50_q23hi")
g_cpvsig_best_hi_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsigbest_q23hi")

g_cpvsig_75_nom_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig75_q23nom")
g_cpvsig_50_nom_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig50_q23nom")
g_cpvsig_best_nom_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsigbest_q23nom")

g_cpvsig_75_lo_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig75_q23lo")
g_cpvsig_50_lo_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig50_q23lo")
g_cpvsig_best_lo_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsigbest_q23lo")

g_cpvsig_75_hi_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig75_q23hi")
g_cpvsig_50_hi_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig50_q23hi")
g_cpvsig_best_hi_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsigbest_q23hi")

g_cpvsig_75_nom_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig75_q23nom")
g_cpvsig_50_nom_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsig50_q23nom")
g_cpvsig_best_nom_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("cpvsigbest_q23nom")

g_mhsig_100_lo_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsig100_q23lo")
g_mhsig_best_lo_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsigbest_q23lo")

g_mhsig_100_hi_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsig100_q23hi")
g_mhsig_best_hi_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsigbest_q23hi")

g_mhsig_100_nom_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsig100_q23nom")
g_mhsig_best_nom_prelim = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsigbest_q23nom")

g_mhsig_100_lo_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsig100_q23lo")
g_mhsig_best_lo_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsigbest_q23lo")

g_mhsig_100_hi_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsig100_q23hi")
g_mhsig_best_hi_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsigbest_q23hi")

g_mhsig_100_nom_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsig100_q23nom")
g_mhsig_best_nom_full = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root").Get("mhsigbest_q23nom")


explist = [0,1,5,10,30,50,100,200,336,450,624,800,1104,1300,1500]
cpv75_lo = [0]
cpv50_lo = [0]
cpvbest_lo = [0]
cpv75_hi = [0]
cpv50_hi = [0]
cpvbest_hi = [0]
cpv75_nom = [0]
cpv50_nom = [0]
cpvbest_nom = [0]

mh100_lo = [0]
mhbest_lo = [0]
mh100_hi = [0]
mhbest_hi = [0]
mh100_nom = [0]
mhbest_nom = [0]


def fillstaged(thisexp,syst=""):
      thing = globals()["g_cpvsig_75_lo_"+syst]
      cpv75_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_50_lo_"+syst]
      cpv50_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_best_lo_"+syst]
      cpvbest_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_75_hi_"+syst]
      cpv75_hi.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_50_hi_"+syst]
      cpv50_hi.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_best_hi_"+syst]
      cpvbest_hi.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_75_nom_"+syst]
      cpv75_nom.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_50_nom_"+syst]
      cpv50_nom.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_cpvsig_best_nom_"+syst]
      cpvbest_nom.append(thing.Eval(thisexp,0,"S"))

      thing = globals()["g_mhsig_100_lo_"+syst]
      mh100_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_best_lo_"+syst]
      mhbest_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_100_hi_"+syst]
      mh100_hi.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_best_hi_"+syst]
      mhbest_hi.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_100_nom_"+syst]
      mh100_nom.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_best_nom_"+syst]
      mhbest_nom.append(thing.Eval(thisexp,0,"S"))

      return 0


g_staging = ROOT.TGraph()
g_staging.SetPoint(0, 0.0, 0.0)

years = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
         6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
thisexp = 0
count = 0
for year in years:
      thissyst = "full"
      if year < 3.5:
            thissyst = "prelim"

      power = 2.4
      if year < 7:
            power = 1.2

      mass = 40
      if year < 3.5:
            mass = 30
      if year < 1.25:
            mass = 20

      if count > 0:
            thisexp += mass*power*(year - years[count-1])
            print "Year ", year, ": ", thisexp
            fillstaged(thisexp,thissyst)
            g_staging.SetPoint(g_staging.GetN(), thisexp, years[g_staging.GetN()])
      count +=1

f_out = ROOT.TFile("root/staging_convert.root","RECREATE")
g_staging.SetName("g_exp")
g_staging.Write()
f_out.Close()

nyears = len(years)
years = array('d',years)
cpv75_lo = array('d',cpv75_lo)
cpv50_lo = array('d',cpv50_lo)
cpvbest_lo = array('d',cpvbest_lo)
cpv75_hi = array('d',cpv75_hi)
cpv50_hi = array('d',cpv50_hi)
cpvbest_hi = array('d',cpvbest_hi)
cpv75_nom = array('d',cpv75_nom)
cpv50_nom = array('d',cpv50_nom)
cpvbest_nom = array('d',cpvbest_nom)

mh100_lo = array('d',mh100_lo)
mhbest_lo = array('d',mhbest_lo)
mh100_hi = array('d',mh100_hi)
mhbest_hi = array('d',mhbest_hi)
mh100_nom = array('d',mh100_nom)
mhbest_nom = array('d',mhbest_nom)

g_staged_cpv75_lo = ROOT.TGraph(nyears,years,cpv75_lo)
g_staged_cpv50_lo = ROOT.TGraph(nyears,years,cpv50_lo)
g_staged_cpvbest_lo = ROOT.TGraph(nyears,years,cpvbest_lo)
g_staged_cpv75_hi = ROOT.TGraph(nyears,years,cpv75_hi)
g_staged_cpv50_hi = ROOT.TGraph(nyears,years,cpv50_hi)
g_staged_cpvbest_hi = ROOT.TGraph(nyears,years,cpvbest_hi)
g_staged_cpv75_nom = ROOT.TGraph(nyears,years,cpv75_nom)
g_staged_cpv50_nom = ROOT.TGraph(nyears,years,cpv50_nom)
g_staged_cpvbest_nom = ROOT.TGraph(nyears,years,cpvbest_nom)

g_staged_mh100_lo = ROOT.TGraph(nyears,years,mh100_lo)
g_staged_mhbest_lo = ROOT.TGraph(nyears,years,mhbest_lo)
g_staged_mh100_hi = ROOT.TGraph(nyears,years,mh100_hi)
g_staged_mhbest_hi = ROOT.TGraph(nyears,years,mhbest_hi)
g_staged_mh100_nom = ROOT.TGraph(nyears,years,mh100_nom)
g_staged_mhbest_nom = ROOT.TGraph(nyears,years,mhbest_nom)

gdiff_staged_cpv75 = filldiff(g_staged_cpv75_hi,g_staged_cpv75_lo,g_staged_cpv75_nom)
gdiff_staged_cpv50 = filldiff(g_staged_cpv50_hi,g_staged_cpv50_lo,g_staged_cpv50_nom)
gdiff_staged_cpvbest = filldiff(g_staged_cpvbest_hi,g_staged_cpvbest_lo,g_staged_cpvbest_nom)
gdiff_staged_mh100 = filldiff(g_staged_mh100_hi,g_staged_mh100_lo,g_staged_mh100_nom)
gdiff_staged_mhbest = filldiff(g_staged_mhbest_hi,g_staged_mhbest_lo,g_staged_mhbest_nom)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,15.0,12.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Years")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.5)
h1.GetYaxis().CenterTitle()
c1.Modified()

gdiff_staged_cpv75.SetFillColor(ROOT.kCyan+2)
gdiff_staged_cpv75.SetLineColor(0)
gdiff_staged_cpv75.SetLineColor(0)
gdiff_staged_cpv75.Draw("F same")

gdiff_staged_cpv50.SetFillColor(ROOT.kCyan-7)
gdiff_staged_cpv50.SetLineColor(0)
gdiff_staged_cpv50.Draw("F same")

gdiff_staged_cpvbest.SetFillColor(ROOT.kPink-3)
gdiff_staged_cpvbest.SetLineColor(0)
gdiff_staged_cpvbest.Draw("F same")

t1 = ROOT.TPaveText(0.16,0.7,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23}: NuFIT 4.0 90% C.L.")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.6,0.75,0.88,0.89)
l1.AddEntry(gdiff_staged_cpvbest, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(gdiff_staged_cpv50, "50% of #delta_{CP} values","F")
l1.AddEntry(gdiff_staged_cpv75, "75% of #delta_{CP} values","F")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,15.0,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,15.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(50.,3.1,100.,3.3)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetBorderSize(0)
t3sig.Draw("same")

t5sig = ROOT.TPaveText(50.,5.1,100.,5.3)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
t5sig.Draw("same")

outname = "plot/exposures/cpv_exp_staging_varyth23_"+hier+"_2019.eps"
outname2 = "plot/exposures/cpv_exp_staging_varyth23_"+hier+"_2019.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)                               

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,7.0,35.0)
h2.SetTitle("Mass Ordering Sensitivity")
h2.GetXaxis().SetTitle("Years")
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.5)
h2.GetYaxis().CenterTitle()
c2.Modified()

gdiff_staged_mh100.SetFillColor(ROOT.kCyan+2)
gdiff_staged_mh100.SetLineColor(0)
gdiff_staged_mh100.Draw("F same")

if (hier == "nh"):
      gdiff_staged_mhbest.SetFillColor(ROOT.kPink-3)
      gdiff_staged_mhbest.SetLineColor(0)
      gdiff_staged_mhbest.Draw("F same")

t1 = ROOT.TPaveText(0.16,0.7,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23}: NuFIT 4.0 90% C.L.")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.6,0.75,0.88,0.89)
if (hier == "nh"):
      l1.AddEntry(gdiff_staged_mhbest, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(gdiff_staged_mh100, "100% of #delta_{CP} values","F")
l1.SetBorderSize(0)
l1.Draw("same")

line3 = ROOT.TLine(0.0,5.,7.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot/exposures/mh_exp_staging_varyth23_"+hier+"_2019.eps"
outname2 = "plot/exposures/mh_exp_staging_varyth23_"+hier+"_2019.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)                               


