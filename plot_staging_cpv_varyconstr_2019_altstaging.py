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
      hnum = "1"
elif (hier == 'ih'):
      htext = "Inverted Ordering"
      hnum = "-1"
else:
      print "Must supply nh or ih!"
      exit()

g_cpvsig_75_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig75_nopen")
g_cpvsig_50_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig50_nopen")
g_cpvsig_best_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsigbest_nopen")

g_cpvsig_75_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig75_th13pen")
g_cpvsig_50_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig50_th13pen")
g_cpvsig_best_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsigbest_th13pen")

g_cpvsig_75_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig75_nopen")
g_cpvsig_50_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig50_nopen")
g_cpvsig_best_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsigbest_nopen")

g_cpvsig_75_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig75_th13pen")
g_cpvsig_50_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsig50_th13pen")
g_cpvsig_best_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("cpvsigbest_th13pen")

g_mhsig_100_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsig100_nopen")
g_mhsig_best_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsigbest_nopen")

g_mhsig_100_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsig100_th13pen")
g_mhsig_best_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsigbest_th13pen")

g_mhsig_100_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsig100_nopen")
g_mhsig_best_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsigbest_nopen")

g_mhsig_100_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsig100_th13pen")
g_mhsig_best_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("mhsigbest_th13pen")

g_dcpres0_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpres0_th13pen")
g_dcpresneg_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpresneg_th13pen")
g_th23res_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("th23res_th13pen")
g_dmsqres_hi_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dmsqres_th13pen")

g_dcpres0_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpres0_nopen")
g_dcpresneg_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpresneg_nopen")
g_th23res_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("th23res_nopen")
g_dmsqres_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dmsqres_nopen")
g_th13res_lo_full = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("th13res_nopen")

g_dcpres0_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpres0_th13pen")
g_dcpresneg_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpresneg_th13pen")
g_th23res_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("th23res_th13pen")
g_dmsqres_hi_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dmsqres_th13pen")

g_dcpres0_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpres0_nopen")
g_dcpresneg_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dcpresneg_nopen")
g_th23res_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("th23res_nopen")
g_dmsqres_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("dmsqres_nopen")
g_th13res_lo_prelim = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root").Get("th13res_nopen")


explist = [0,1,5,10,30,50,100,200,336,450,624,800,1104,1300,1500]
cpv75_lo = []
cpv50_lo = []
cpvbest_lo = []
cpv75_hi = []
cpv50_hi = []
cpvbest_hi = []

mh100_lo = []
mhbest_lo = []
mh100_hi = []
mhbest_hi = []

dcpres0_lo = [1000]
dcpresneg_lo = [1000]
th23res_lo = [0.05]
dmsqres_lo = [0.3]
th13res_lo = [0.1]

dcpres0_hi = [1000]
dcpresneg_hi = [1000]
th23res_hi = [0.05]
dmsqres_hi = [0.3]


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

      thing = globals()["g_mhsig_100_lo_"+syst]
      mh100_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_best_lo_"+syst]
      mhbest_lo.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_100_hi_"+syst]
      mh100_hi.append(thing.Eval(thisexp,0,"S"))
      thing = globals()["g_mhsig_best_hi_"+syst]
      mhbest_hi.append(thing.Eval(thisexp,0,"S"))

      thing = globals()["g_dcpres0_lo_"+syst]
      dcpres0_lo.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_dcpresneg_lo_"+syst]
      dcpresneg_lo.append(thing.Eval(thisexp,0,""))

      thing = globals()["g_th23res_lo_"+syst]
      th23res_lo.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_th13res_lo_"+syst]
      th13res_lo.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_dmsqres_lo_"+syst]
      dmsqres_lo.append(thing.Eval(thisexp,0,""))

      thing = globals()["g_dcpres0_hi_"+syst]
      dcpres0_hi.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_dcpresneg_hi_"+syst]
      dcpresneg_hi.append(thing.Eval(thisexp,0,""))

      thing = globals()["g_th23res_hi_"+syst]
      th23res_hi.append(thing.Eval(thisexp,0,""))
      thing = globals()["g_dmsqres_hi_"+syst]
      dmsqres_hi.append(thing.Eval(thisexp,0,""))
      

      return 0


g_staging = ROOT.TGraph()

years = []

#Change staging scenario here
thisexp = 0
count = 0
year = 0
#for year in years:
while year < 15.01:
      years.append(year)
      thissyst = "full"
      if year < 3.5:
            thissyst = "prelim"
      
      #Power Ramp for PIP-II (linear interpolation between year milestones, put in offset between proton beam and neutrino beam, no 2.4 upgrade yet)
      #year_beam corresponds to PIP-II timeline)
      year_beam = year + 1.25 #assume 15 months - this is scenario C +9 months, and commissioning +15 months
      year_beam = year_beam*(4.0/2.5) #For accelerated scenario - same shape except finish by 2.5 years
      power = 2.4
      if year_beam < 99.01:
            power = 1.2
      if year_beam < 4.0:
            power = 1.175
      if year_beam < 3.75:
            power = 1.15
      if year_beam < 3.5:
            power = 1.125
      if year_beam < 3.25:
            power = 1.1
      if year_beam < 3:
            power = 1.0125
      if year_beam < 2.75:
            power = 0.925
      if year_beam < 2.5:
            power = 0.8735
      if year_beam < 2.25:
            power = 0.75
      if year_beam < 2.0:
            power = 0.625
      if year_beam < 1.75:
            power = 0.5
      if year_beam < 1.5:
            power = 0.375
      if year_beam < 1.25:
            power = 0.25
      if year_beam < 1.0:
            power = 0.1875
      if year_beam < 0.75:
            power = 0.125
      if year_beam < 0.5:
            power = 0.0625
      if year_beam < 0.25:
            power = 0.03125

            
#      #No power ramp
#      power = 2.4
#      if year < 6.01:
#            power = 1.2
            
# Physics staging scenario
#      mass = 40
#      if year < 3.0:
#            mass = 30
#      if year < 1.0:
#            mass = 20

# Scenario A:
#      mass = 20
#      if year < 2.5:
#            mass = 10
 
# Scenario B:
#      if year < 0.25:
#            power = 0
#      mass = 20
#      if year < 1.51:
#            mass = 10


# Scenario C:
      mass = 20
            
      if count > 0:
            thisexp += mass*power*(year - years[count-1])

      print "Year ", year, ": ", power, thisexp
      fillstaged(thisexp,thissyst)
      g_staging.SetPoint(g_staging.GetN(), thisexp, years[g_staging.GetN()])

      count +=1
      year += 0.05

f_out = ROOT.TFile("root_v4/staging_convert_fastrampcomm.root","RECREATE")
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

mh100_lo = array('d',mh100_lo)
mhbest_lo = array('d',mhbest_lo)
mh100_hi = array('d',mh100_hi)
mhbest_hi = array('d',mhbest_hi)

dcpres0_lo = array('d',dcpres0_lo)
dcpresneg_lo = array('d',dcpresneg_lo)
th23res_lo = array('d',th23res_lo)
th13res_lo = array('d',th13res_lo)
dmsqres_lo = array('d',dmsqres_lo)

dcpres0_hi = array('d',dcpres0_hi)
dcpresneg_hi = array('d',dcpresneg_hi)
th23res_hi = array('d',th23res_hi)
dmsqres_hi = array('d',dmsqres_hi)

g_staged_cpv75_lo = ROOT.TGraph(nyears,years,cpv75_lo)
g_staged_cpv50_lo = ROOT.TGraph(nyears,years,cpv50_lo)
g_staged_cpvbest_lo = ROOT.TGraph(nyears,years,cpvbest_lo)
g_staged_cpv75_hi = ROOT.TGraph(nyears,years,cpv75_hi)
g_staged_cpv50_hi = ROOT.TGraph(nyears,years,cpv50_hi)
g_staged_cpvbest_hi = ROOT.TGraph(nyears,years,cpvbest_hi)

g_staged_mh100_lo = ROOT.TGraph(nyears,years,mh100_lo)
g_staged_mhbest_lo = ROOT.TGraph(nyears,years,mhbest_lo)
g_staged_mh100_hi = ROOT.TGraph(nyears,years,mh100_hi)
g_staged_mhbest_hi = ROOT.TGraph(nyears,years,mhbest_hi)

g_staged_dcpres0_lo = ROOT.TGraph(nyears,years,dcpres0_lo)
g_staged_dcpresneg_lo = ROOT.TGraph(nyears,years,dcpresneg_lo)
g_staged_th23res_lo = ROOT.TGraph(nyears,years,th23res_lo)
g_staged_th13res_lo = ROOT.TGraph(nyears,years,th13res_lo)
g_staged_dmsqres_lo = ROOT.TGraph(nyears,years,dmsqres_lo)

g_staged_dcpres0_hi = ROOT.TGraph(nyears,years,dcpres0_hi)
g_staged_dcpresneg_hi = ROOT.TGraph(nyears,years,dcpresneg_hi)
g_staged_th23res_hi = ROOT.TGraph(nyears,years,th23res_hi)
g_staged_dmsqres_hi = ROOT.TGraph(nyears,years,dmsqres_hi)

gdiff_staged_cpv75 = filldiff(g_staged_cpv75_hi,g_staged_cpv75_lo)
gdiff_staged_cpv50 = filldiff(g_staged_cpv50_hi,g_staged_cpv50_lo)
gdiff_staged_cpvbest = filldiff(g_staged_cpvbest_hi,g_staged_cpvbest_lo)
gdiff_staged_mh100 = filldiff(g_staged_mh100_hi,g_staged_mh100_lo)
gdiff_staged_mhbest = filldiff(g_staged_mhbest_hi,g_staged_mhbest_lo)

gdiff_staged_dcpres0 = filldiff(g_staged_dcpres0_hi,g_staged_dcpres0_lo)
gdiff_staged_dcpresneg = filldiff(g_staged_dcpresneg_hi,g_staged_dcpresneg_lo)
gdiff_staged_th23res = filldiff(g_staged_th23res_hi,g_staged_th23res_lo)
gdiff_staged_dmsqres = filldiff(g_staged_dmsqres_hi,g_staged_dmsqres_lo)

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
g_staged_cpv75_lo.SetLineWidth(3)
g_staged_cpv75_hi.SetLineWidth(3)
g_staged_cpv75_lo.SetLineStyle(3)

gdiff_staged_cpv75.Draw("F same")
g_staged_cpv75_lo.Draw("same")
g_staged_cpv75_hi.Draw("same")

gdiff_staged_cpv50.SetFillColor(ROOT.kCyan-7)
gdiff_staged_cpv50.SetLineColor(0)
g_staged_cpv50_lo.SetLineWidth(3)
g_staged_cpv50_hi.SetLineWidth(3)
g_staged_cpv50_lo.SetLineStyle(3)

gdiff_staged_cpv50.Draw("F same")
g_staged_cpv50_lo.Draw("same")
g_staged_cpv50_hi.Draw("same")

gdiff_staged_cpvbest.SetFillColor(ROOT.kPink-3)
gdiff_staged_cpvbest.SetLineColor(0)
g_staged_cpvbest_lo.SetLineWidth(3)
g_staged_cpvbest_hi.SetLineWidth(3)
g_staged_cpvbest_lo.SetLineStyle(3)

gdiff_staged_cpvbest.Draw("F same")
g_staged_cpvbest_lo.Draw("same")
g_staged_cpvbest_hi.Draw("same")

t1 = ROOT.TPaveText(0.16,0.72,0.55,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
#t1.SetFillColor(ROOT.kWhite)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.88,0.89)
l1.AddEntry(gdiff_staged_cpvbest, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(gdiff_staged_cpv50, "50% of #delta_{CP} values","F")
l1.AddEntry(gdiff_staged_cpv75, "75% of #delta_{CP} values","F")
l1.AddEntry(g_staged_cpv75_hi,"Nominal Analysis","L")
l1.AddEntry(g_staged_cpv75_lo,"#theta_{13} unconstrained","L")
l1.SetBorderSize(0)
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

outname = "plot_v4/exposures/cpv_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.eps"
outname2 = "plot_v4/exposures/cpv_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.png"
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
g_staged_mh100_lo.SetLineWidth(3)
g_staged_mh100_hi.SetLineWidth(3)
g_staged_mh100_lo.SetLineStyle(3)

gdiff_staged_mh100.Draw("F same")
g_staged_mh100_lo.Draw("same")
g_staged_mh100_hi.Draw("same")

if (hier == "nh"):
      gdiff_staged_mhbest.SetFillColor(ROOT.kPink-3)
      gdiff_staged_mhbest.SetLineColor(0)
      g_staged_mhbest_lo.SetLineWidth(3)
      g_staged_mhbest_hi.SetLineWidth(3)
      g_staged_mhbest_lo.SetLineStyle(3)

      gdiff_staged_mhbest.Draw("F same")
      g_staged_mhbest_lo.Draw("same")
      g_staged_mhbest_hi.Draw("same")

t1 = ROOT.TPaveText(0.16,0.72,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity (Staged)")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.SetBorderSize(0)
t1.SetFillStyle(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.88,0.89)
if (hier == "nh"):
      l1.AddEntry(gdiff_staged_mhbest, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(gdiff_staged_mh100, "100% of #delta_{CP} values","F")
l1.AddEntry(g_staged_mh100_hi,"Nominal Analysis","L")
l1.AddEntry(g_staged_mh100_lo,"#theta_{13} unconstrained","L")
l1.SetBorderSize(0)
l1.Draw("same")

line3 = ROOT.TLine(0.0,5.,7.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot_v4/exposures/mh_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.eps"
outname2 = "plot_v4/exposures/mh_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)                               

if (hier == "nh"):
      c3 = ROOT.TCanvas("c3","c3",800,800)
      c3.SetLeftMargin(0.15)
      h3 = c3.DrawFrame(0,0.0,15.0,60.0)
      h3.SetTitle("")
      h3.GetXaxis().SetTitle("Years")
      h3.GetYaxis().SetTitle("#delta_{CP} Resolution (degrees)")      
      h3.GetYaxis().SetTitleOffset(1.5)
      h3.GetYaxis().CenterTitle()
      c3.Modified()

      gdiff_staged_dcpres0.SetFillColor(ROOT.kCyan+3)
      gdiff_staged_dcpres0.SetLineColor(0)
      g_staged_dcpres0_lo.SetLineWidth(3)
      g_staged_dcpres0_hi.SetLineWidth(3)
      g_staged_dcpres0_lo.SetLineStyle(3)

      gdiff_staged_dcpres0.Draw("F same")
      g_staged_dcpres0_lo.Draw("same")
      g_staged_dcpres0_hi.Draw("same")

      gdiff_staged_dcpresneg.SetFillColor(ROOT.kPink-3)
      gdiff_staged_dcpresneg.SetLineColor(0)
      g_staged_dcpresneg_lo.SetLineWidth(3)
      g_staged_dcpresneg_hi.SetLineWidth(3)
      g_staged_dcpresneg_lo.SetLineStyle(3)

      gdiff_staged_dcpresneg.Draw("F same")
      g_staged_dcpresneg_lo.Draw("same")
      g_staged_dcpresneg_hi.Draw("same")

      t1 = ROOT.TPaveText(0.5,0.72,0.89,0.89,"NDC")
      t1.AddText("DUNE Sensitivity (Staged)")
      t1.AddText("All Systematics")
      t1.AddText(htext)
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
      t1.SetBorderSize(0)
      t1.SetFillStyle(0)
      t1.SetTextAlign(12)
      t1.Draw("same")

      l1 = ROOT.TLegend(0.5,0.58,0.89,0.7)
      l1.AddEntry(gdiff_staged_dcpresneg, "#delta_{CP} = -#pi/2","F")
      l1.AddEntry(gdiff_staged_dcpres0, "#delta_{CP} = 0","F")
      l1.AddEntry(g_staged_dcpres0_hi,"Nominal Analysis","L")
      l1.AddEntry(g_staged_dcpresneg_lo,"#theta_{13} unconstrained","L")
      l1.SetBorderSize(0)
      l1.Draw("same")
      
      outname = "plot_v4/res/dcp_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.eps"
      outname2 = "plot_v4/res/dcp_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.png"
      c3.SaveAs(outname)
      c3.SaveAs(outname2)                               

      c4 = ROOT.TCanvas("c4","c4",800,800)
      c4.SetLeftMargin(0.15)
      h4 = c4.DrawFrame(0,0.0,15.0,0.02)
      h4.SetTitle("")
      h4.GetXaxis().SetTitle("Years")
      h4.GetYaxis().SetTitle("sin^{2}(2#theta_{23}) Resolution")      
      h4.GetYaxis().SetTitleOffset(1.7)
      h4.GetYaxis().CenterTitle()
      c4.Modified()

      gdiff_staged_th23res.SetFillColor(ROOT.kCyan+3)
      gdiff_staged_th23res.SetLineColor(0)
      g_staged_th23res_lo.SetLineWidth(3)
      g_staged_th23res_hi.SetLineWidth(3)
      g_staged_th23res_lo.SetLineStyle(3)

      gdiff_staged_th23res.Draw("F same")
      g_staged_th23res_lo.Draw("same")
      g_staged_th23res_hi.Draw("same")

      t1 = ROOT.TPaveText(0.5,0.72,0.89,0.89,"NDC")
      t1.AddText("DUNE Sensitivity (Staged)")
      t1.AddText("All Systematics")
      t1.AddText(htext)
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
      t1.SetBorderSize(0)
      t1.SetFillStyle(0)
      t1.SetTextAlign(12)
      t1.Draw("same")

      l1 = ROOT.TLegend(0.5,0.6,0.89,0.7)
      l1.AddEntry(g_staged_th23res_hi,"Nominal Analysis","L")
      l1.AddEntry(g_staged_th23res_lo,"#theta_{13} unconstrained","L")
      l1.SetBorderSize(0)
      l1.Draw("same")
      
      outname = "plot_v4/res/th23_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.eps"
      outname2 = "plot_v4/res/th23_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.png"
      c4.SaveAs(outname)
      c4.SaveAs(outname2)                               

      c5 = ROOT.TCanvas("c5","c5",800,800)
      c5.SetLeftMargin(0.15)
      h5 = c5.DrawFrame(0,0.0,15.0,0.05)
      h5.SetTitle("")
      h5.GetXaxis().SetTitle("Years")
      h5.GetYaxis().SetTitle("#Deltam^{2}_{32} Resolution (eV^{2} x 10^{-3})")
      h5.GetYaxis().SetTitleOffset(1.7)
      h5.GetYaxis().CenterTitle()
      c5.Modified()

      gdiff_staged_dmsqres.SetFillColor(ROOT.kCyan+3)
      gdiff_staged_dmsqres.SetLineColor(0)
      g_staged_dmsqres_lo.SetLineWidth(3)
      g_staged_dmsqres_hi.SetLineWidth(3)
      g_staged_dmsqres_lo.SetLineStyle(3)

      g_staged_dmsqres_lo.Draw("same")

      t1 = ROOT.TPaveText(0.5,0.72,0.89,0.89,"NDC")
      t1.AddText("DUNE Sensitivity (Staged)")
      t1.AddText("All Systematics")
      t1.AddText(htext)
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
      t1.SetBorderSize(0)
      t1.SetFillStyle(0)
      t1.SetTextAlign(12)
      t1.Draw("same")

      l1 = ROOT.TLegend(0.5,0.6,0.89,0.7)
      l1.AddEntry(g_staged_dmsqres_lo,"#theta_{13} unconstrained","L")
      l1.SetBorderSize(0)
      l1.Draw("same")
      
      outname = "plot_v4/res/dmsq_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.eps"
      outname2 = "plot_v4/res/dmsq_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.png"
      c5.SaveAs(outname)
      c5.SaveAs(outname2)                               

      c6 = ROOT.TCanvas("c6","c6",800,800)
      c6.SetLeftMargin(0.15)
      h6 = c6.DrawFrame(0,0.0,15.0,0.03)
      h6.SetTitle("")
      h6.GetXaxis().SetTitle("Years")
      h6.GetYaxis().SetTitle("sin^{2}(2#theta_{13}) Resolution")
      h6.GetYaxis().SetTitleOffset(1.7)
      h6.GetYaxis().CenterTitle()
      c6.Modified()

      g_staged_th13res_lo.SetLineWidth(4)
      g_staged_th13res_lo.SetLineStyle(3)
      g_staged_th13res_lo.Draw("same")

      t1 = ROOT.TPaveText(0.5,0.72,0.89,0.89,"NDC")
      t1.AddText("DUNE Sensitivity (Staged)")
      t1.AddText("All Systematics")
      t1.AddText(htext)
      t1.AddText("sin^{2}2#theta_{13} = 0.088 unconstrained")
      t1.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
      t1.SetBorderSize(0)
      t1.SetFillStyle(0)
      t1.SetTextAlign(12)
      t1.Draw("same")
      l1.Draw("same")

      outname = "plot_v4/res/th13_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.eps"
      outname2 = "plot_v4/res/th13_exp_staging_varyconstr_"+hier+"_2019_v4_fastrampcomm.png"
      c6.SaveAs(outname)
      c6.SaveAs(outname2)                               


f_out = ROOT.TFile("root_v4/staging_graphs_fastrampcomm.root","RECREATE")
gdiff_staged_cpv75.SetName("cpv75")
gdiff_staged_cpv50.SetName("cpv50")
gdiff_staged_cpvbest.SetName("cpvbest")
gdiff_staged_mh100.SetName("mh100")
gdiff_staged_mhbest.SetName("mhbest")
gdiff_staged_dcpres0.SetName("dcpres0")
gdiff_staged_dcpresneg.SetName("dcpresneg")

gdiff_staged_cpv75.Write()
gdiff_staged_cpv50.Write()
gdiff_staged_cpvbest.Write()
gdiff_staged_mh100.Write()
gdiff_staged_mhbest.Write()
gdiff_staged_dcpres0.Write()
gdiff_staged_dcpresneg.Write()
f_out.Close()

