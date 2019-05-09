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

explist = [0,1,5,10,30,50,100,200,336,450,624,800,1104,1300,1500]
cpvlist75_lo = [0]
cpvlist50_lo = [0]
cpvlistbest_lo = [0]

mhlist100_lo = [0]
mhlistbest_lo = [0]

cpvlist50_hi = [0]
cpvlist75_hi = [0]
cpvlistbest_hi = [0]

mhlist100_hi = [0]
mhlistbest_hi = [0]

cpvlist50_nom = [0]
cpvlist75_nom = [0]
cpvlistbest_nom = [0]

mhlist100_nom = [0]
mhlistbest_nom = [0]

for myexp in explist:

      if (myexp==0):
            continue

      #Th23 lo
      filename = "root_callum/cpv_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov1_v3.root"
      f1 = ROOT.TFile(filename)
      cpvgraph_lo = f1.Get("sens_cpv_"+hier)
      nvals = cpvgraph_lo.GetN()
      cut75 = int(0.25*nvals)
      cut50 = int(0.5*nvals)
      cutbest = int(0.25*nvals)
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_lo.GetY()

      i = 0
      cpv_vals_lo = []
      while i < nvals:
            cpv_vals_lo.append(cpv_vals[i])
            i += 1

      cpvsig_75_lo = sorted(cpv_vals_lo)[cut75]
      cpvsig_50_lo = sorted(cpv_vals_lo)[cut50]
      cpvlist75_lo.append(cpvsig_75_lo)
      cpvlist50_lo.append(cpvsig_50_lo)
      cpvlistbest_lo.append(cpv_vals[cutbest])
      f1.Close()

      #Th23 Hi
      filename = "root_callum/cpv_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov2_v3.root"
      f1 = ROOT.TFile(filename)
      cpvgraph_hi = f1.Get("sens_cpv_"+hier)
      nvals = cpvgraph_hi.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_hi.GetY()

      i = 0
      cpv_vals_hi = []
      while i < nvals:
            cpv_vals_hi.append(cpv_vals[i])
            i += 1

      cpvsig_75_hi = sorted(cpv_vals_hi)[cut75]
      cpvsig_50_hi = sorted(cpv_vals_hi)[cut50]
      cpvlist75_hi.append(cpvsig_75_hi)
      cpvlist50_hi.append(cpvsig_50_hi)
      cpvlistbest_hi.append(cpv_vals[cutbest])
      f1.Close()

      #Th23 Nom
      filename = "root_callum/cpv_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov0_v3.root"
      f1 = ROOT.TFile(filename)
      cpvgraph_nom = f1.Get("sens_cpv_"+hier)
      nvals = cpvgraph_nom.GetN()
      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph_nom.GetY()

      i = 0
      cpv_vals_nom = []
      while i < nvals:
            cpv_vals_nom.append(cpv_vals[i])
            i += 1

      cpvsig_75_nom = sorted(cpv_vals_hi)[cut75]
      cpvsig_50_nom = sorted(cpv_vals_hi)[cut50]
      cpvlist75_nom.append(cpvsig_75_nom)
      cpvlist50_nom.append(cpvsig_50_nom)
      cpvlistbest_nom.append(cpv_vals[cutbest])
      f1.Close()
      
      #MH Th23 lo
      filename = "root_callum/mh_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov1_v3.root"
      f1 = ROOT.TFile(filename)
      mhgraph_lo = f1.Get("sens_mh_"+hier)
      nvals = mhgraph_lo.GetN()
      cutbest = int(0.25*nvals)
      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_lo.GetY()

      i = 0
      mh_vals_lo = []
      while i < nvals:
            mh_vals_lo.append(mh_vals[i])
            i += 1

      mhlist100_lo.append(min(mh_vals_lo))
      mhlistbest_lo.append(mh_vals[cutbest])
      f1.Close()

      #MH Th23 hi
      filename = "root_callum/mh_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov2_v3.root"
      f1 = ROOT.TFile(filename)
      mhgraph_hi = f1.Get("sens_mh_"+hier)
      nvals = mhgraph_hi.GetN()
      cutbest = int(0.25*nvals)
      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_hi.GetY()

      i = 0
      mh_vals_hi = []
      while i < nvals:
            mh_vals_hi.append(mh_vals[i])
            i += 1

      mhlist100_hi.append(min(mh_vals_hi))
      mhlistbest_hi.append(mh_vals[cutbest])
      f1.Close()

      #MH Th23 nom
      filename = "root_callum/mh_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov0_v3.root"
      f1 = ROOT.TFile(filename)
      mhgraph_nom = f1.Get("sens_mh_"+hier)
      nvals = mhgraph_nom.GetN()
      cutbest = int(0.25*nvals)
      mh_vals = [ROOT.Double(0.0)]*nvals
      mh_vals = array('d',mh_vals)
      mh_vals = mhgraph_hi.GetY()

      i = 0
      mh_vals_nom = []
      while i < nvals:
            mh_vals_nom.append(mh_vals[i])
            i += 1

      mhlist100_nom.append(min(mh_vals_nom))
      mhlistbest_nom.append(mh_vals[cutbest])
      f1.Close()
      

n = len(explist)
explist = array('d',explist)
cpvlist75_lo = array('d',cpvlist75_lo)
cpvlist75_hi = array('d',cpvlist75_hi)
cpvlist75_nom = array('d',cpvlist75_nom)

cpvlist50_lo = array('d',cpvlist50_lo)
cpvlist50_hi = array('d',cpvlist50_hi)
cpvlist50_nom = array('d',cpvlist50_nom)

cpvlistbest_lo = array('d',cpvlistbest_lo)
cpvlistbest_hi = array('d',cpvlistbest_hi)
cpvlistbest_nom = array('d',cpvlistbest_nom)

mhlist100_lo = array('d',mhlist100_lo)
mhlist100_hi = array('d',mhlist100_hi)
mhlist100_nom = array('d',mhlist100_nom)

mhlistbest_lo = array('d',mhlistbest_lo)
mhlistbest_hi = array('d',mhlistbest_hi)
mhlistbest_nom = array('d',mhlistbest_nom)

g_cpvsig_75_lo = ROOT.TGraph(n,explist,cpvlist75_lo)
g_cpvsig_75_hi = ROOT.TGraph(n,explist,cpvlist75_hi)
g_cpvsig_75_nom = ROOT.TGraph(n,explist,cpvlist75_nom)

g_cpvsig_50_lo = ROOT.TGraph(n,explist,cpvlist50_lo)
g_cpvsig_50_hi = ROOT.TGraph(n,explist,cpvlist50_hi)
g_cpvsig_50_nom = ROOT.TGraph(n,explist,cpvlist50_nom)

g_cpvsig_best_lo = ROOT.TGraph(n,explist,cpvlistbest_lo)
g_cpvsig_best_hi = ROOT.TGraph(n,explist,cpvlistbest_hi)
g_cpvsig_best_nom = ROOT.TGraph(n,explist,cpvlistbest_nom)

g_mhsig_100_lo = ROOT.TGraph(n,explist,mhlist100_lo)
g_mhsig_100_hi = ROOT.TGraph(n,explist,mhlist100_hi)
g_mhsig_100_nom = ROOT.TGraph(n,explist,mhlist100_nom)

g_mhsig_best_lo = ROOT.TGraph(n,explist,mhlistbest_lo)
g_mhsig_best_hi = ROOT.TGraph(n,explist,mhlistbest_hi)
g_mhsig_best_nom = ROOT.TGraph(n,explist,mhlistbest_nom)

g_cpvsig_75_lo.SetLineWidth(3)
g_cpvsig_75_hi.SetLineWidth(3)
g_cpvsig_75_nom.SetLineWidth(3)

g_cpvsig_50_lo.SetLineWidth(3)
g_cpvsig_50_hi.SetLineWidth(3)
g_cpvsig_50_nom.SetLineWidth(3)

g_cpvsig_best_hi.SetLineWidth(3)
g_cpvsig_best_lo.SetLineStyle(3)
g_cpvsig_best_nom.SetLineStyle(3)

g_mhsig_100_lo.SetLineWidth(3)
g_mhsig_100_hi.SetLineWidth(3)
g_mhsig_100_nom.SetLineWidth(3)

g_mhsig_best_lo.SetLineWidth(3)
g_mhsig_best_hi.SetLineWidth(3)
g_mhsig_best_nom.SetLineWidth(3)

myout = ROOT.TFile("root/exposure_graphs_varyth23_"+hier+".root","recreate")
g_cpvsig_75_lo.SetName("cpvsig75_q23lo")
g_cpvsig_50_lo.SetName("cpvsig50_q23lo")
g_cpvsig_best_lo.SetName("cpvsigbest_q23lo")
g_cpvsig_75_hi.SetName("cpvsig75_q23hi")
g_cpvsig_50_hi.SetName("cpvsig50_q23hi")
g_cpvsig_best_hi.SetName("cpvsigbest_q23hi")
g_cpvsig_75_nom.SetName("cpvsig75_q23nom")
g_cpvsig_50_nom.SetName("cpvsig50_q23nom")
g_cpvsig_best_nom.SetName("cpvsigbest_q23nom")

g_mhsig_100_lo.SetName("mhsig100_q23lo")
g_mhsig_best_lo.SetName("mhsigbest_q23lo")
g_mhsig_100_hi.SetName("mhsig100_q23hi")
g_mhsig_best_hi.SetName("mhsigbest_q23hi")
g_mhsig_100_nom.SetName("mhsig100_q23nom")
g_mhsig_best_nom.SetName("mhsigbest_q23nom")

g_cpvsig_75_lo.Write()
g_cpvsig_50_lo.Write()
g_cpvsig_best_lo.Write()
g_cpvsig_75_hi.Write()
g_cpvsig_50_hi.Write()
g_cpvsig_best_hi.Write()
g_cpvsig_75_nom.Write()
g_cpvsig_50_nom.Write()
g_cpvsig_best_nom.Write()

g_mhsig_100_lo.Write()
g_mhsig_best_lo.Write()
g_mhsig_100_hi.Write()
g_mhsig_best_hi.Write()
g_mhsig_100_nom.Write()
g_mhsig_best_nom.Write()

myout.Close()

graph_cpvrange75 = filldiff(g_cpvsig_75_hi,g_cpvsig_75_lo,g_cpvsig_75_nom)
graph_cpvrange50 = filldiff(g_cpvsig_50_hi,g_cpvsig_50_lo,g_cpvsig_50_nom)
graph_cpvbestrange = filldiff(g_cpvsig_best_hi,g_cpvsig_best_lo,g_cpvsig_best_nom)

graph_mhrange100 = filldiff(g_mhsig_100_hi, g_mhsig_100_lo, g_mhsig_100_nom)
graph_mhrangebest = filldiff(g_mhsig_best_hi, g_mhsig_best_lo, g_mhsig_best_nom)

c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1500.0,12.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
graph_cpvrange75.SetFillColor(ROOT.kCyan+2)
graph_cpvrange75.SetLineColor(0)
graph_cpvrange75.Draw("F same")

graph_cpvrange50.SetFillColor(ROOT.kCyan-7)
graph_cpvrange50.SetLineColor(0)
graph_cpvrange50.Draw("F same")

graph_cpvbestrange.SetFillColor(ROOT.kPink-3)
graph_cpvbestrange.SetLineColor(0)
graph_cpvbestrange.Draw("F same")

t1 = ROOT.TPaveText(0.16,0.7,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
t1.AddText("sin^{2}#theta_{23}: NuFit4 90% C.L.")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.6,0.75,0.89,0.89)
l1.AddEntry(graph_cpvbestrange, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(graph_cpvrange50, "50% of #delta_{CP} values","F")
l1.AddEntry(graph_cpvrange75, "75% of #delta_{CP} values","F")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw("same")

line1 = ROOT.TLine(0.,3.,1500.,3.)
line1.SetLineStyle(2)
line1.SetLineWidth(3)
line1.Draw("same")

line2 = ROOT.TLine(0.0,5.,1500.,5.)
line2.SetLineStyle(2)
line2.SetLineWidth(3)
line2.Draw("same")

t3sig = ROOT.TPaveText(10.,3.1,115.,3.7)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetFillStyle(0)
t3sig.SetBorderSize(0)
#t3sig.Draw("same")

t5sig = ROOT.TPaveText(10.,5.1,115.,5.7)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetFillStyle(0)
t5sig.SetBorderSize(0)
#t5sig.Draw("same")

outname = "plot/exposures/cpv_exp_varyth23_"+hier+"_2019.eps"
outname2 = "plot/exposures/cpv_exp_varyth23_"+hier+"_2019.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

c2 = ROOT.TCanvas("c2","c2",800,800)
c2.SetLeftMargin(0.15)
h2 = c2.DrawFrame(0,0.0,500.,35.)
h2.SetTitle("Mass Ordering Sensitivity")
h2.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h2.GetYaxis().SetTitle("#sqrt{#bar{#Delta#chi^{2}}}")
h2.GetYaxis().SetTitleOffset(1.3)
h2.GetYaxis().CenterTitle()
c2.Modified()
graph_mhrange100.SetFillColor(ROOT.kCyan+3)
graph_mhrange100.SetLineColor(0)
if (hier == "nh"):
      graph_mhrangebest.SetFillColor(ROOT.kPink-3)
      graph_mhrangebest.SetLineColor(0)
      graph_mhrangebest.Draw("F same")
graph_mhrange100.Draw("F same")

t1.Draw("same")

lm1 = ROOT.TLegend(0.6,0.75,0.89,0.89)
if (hier == "nh"):
      lm1.AddEntry(graph_mhrangebest, "#delta_{CP} = -#pi/2","F")
lm1.AddEntry(graph_mhrange100, "100% of #delta_{CP} values","F")
lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

line3 = ROOT.TLine(0.0,5.,500.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot/exposures/mh_exp_varyth23_"+hier+"_2019.eps"
outname2 = "plot/exposures/mh_exp_varyth23_"+hier+"_2019.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)


