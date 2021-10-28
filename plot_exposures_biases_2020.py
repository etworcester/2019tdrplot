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

def fix450(graph):
      print "Warning: hack in place to interpolate bad point in "+graph.GetName()
      expup = ROOT.Double(0.0)
      expdown = ROOT.Double(0.0)
      exptarget = ROOT.Double(0.0)
      valup = ROOT.Double(0.0)
      valdown = ROOT.Double(0.0)
      valtarget = ROOT.Double(0.0)
      up = graph.GetPoint(7,expup,valup)
      down = graph.GetPoint(9,expdown,valdown)
      target = graph.GetPoint(8,exptarget,valtarget)
      m = (valup-valdown)/(expup-expdown)
      b = valup - m*expup
      ynew = m*exptarget + b
      print valtarget, ynew
      graph.SetPoint(8,exptarget,ynew)
      return graph

# Determine how far you are from another point, accounding for the 2pi wraparound
def getDiff( d1, d2 ):
      diff = abs(d1 - d2)
      if diff > 1.: diff = 2. - diff
      return diff

#Apply the bias
def applybias(g_cpv, g_res, bias):
      g_cpv_bias = ROOT.TGraph(g_res.GetN())
      for i in range(g_res.GetN()):
           x = ROOT.Double(0.)
           res = ROOT.Double(0.)
           g_res.GetPoint(i, x, res)
           diff = min(getDiff(x,0), getDiff(x,1.), getDiff(x,-1.))
           gauss_cpv_sigma = 180*diff/res
           gauss_cpv_sigma_bias = 180*diff/(math.sqrt(res*res+bias*bias))
           xcpv = ROOT.Double(0.)
           ycpv = ROOT.Double(0.)
           g_cpv.GetPoint(i, xcpv, ycpv)
           if gauss_cpv_sigma > 0.: 
                 g_cpv_bias.SetPoint(i, xcpv, ycpv*gauss_cpv_sigma_bias/gauss_cpv_sigma)
           else:
                 g_cpv_bias.SetPoint(i, xcpv, 0.)
      return g_cpv_bias

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
cpvlist75 = [0]
cpvlist50 = [0]
cpvlistbest = [0]

cpvlist75_fullbias = [0]
cpvlist50_fullbias = [0]
cpvlistbest_fullbias = [0]
cpvlist75_medbias = [0]
cpvlist50_medbias = [0]
cpvlistbest_medbias = [0]
cpvlist75_lobias = [0]
cpvlist50_lobias = [0]
cpvlistbest_lobias = [0]

graph_dcpres = ROOT.TFile("root_v4/throws/graphs_final.root").Get("dcp_th23all_th13_10yr")

for myexp in explist:

      if (myexp==0):
            continue

      filename = "root_v4/sens_staging/cpv_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov0_v4.root"
      f1 = ROOT.TFile(filename)
      cpvgraph = f1.Get("sens_cpv_"+hier)
      cpvgraph_fullbias = applybias(cpvgraph, graph_dcpres, 25.)
      cpvgraph_medbias = applybias(cpvgraph, graph_dcpres, 10.)
      cpvgraph_lobias = applybias(cpvgraph, graph_dcpres, 5.)      

      nvals = cpvgraph.GetN()
      cut75 = int(0.25*nvals)
      cut50 = int(0.5*nvals)
      ibest = int(0.25*nvals)

      cpv_vals = [ROOT.Double(0.0)]*nvals
      cpv_vals = array('d',cpv_vals)
      cpv_vals = cpvgraph.GetY()

      cpv_vals_fullbias = [ROOT.Double(0.0)]*nvals
      cpv_vals_fullbias = array('d',cpv_vals_fullbias)
      cpv_vals_fullbias = cpvgraph_fullbias.GetY()

      cpv_vals_medbias = [ROOT.Double(0.0)]*nvals
      cpv_vals_medbias = array('d',cpv_vals_medbias)
      cpv_vals_medbias = cpvgraph_medbias.GetY()

      cpv_vals_lobias = [ROOT.Double(0.0)]*nvals
      cpv_vals_lobias = array('d',cpv_vals_lobias)
      cpv_vals_lobias = cpvgraph_lobias.GetY()
      
      
      i = 0
      cpv_vals_list = []
      cpv_vals_fullbias_list = []
      cpv_vals_medbias_list = []
      cpv_vals_lobias_list = []      
      while i < nvals:
            cpv_vals_list.append(cpv_vals[i])
            cpv_vals_fullbias_list.append(cpv_vals_fullbias[i])
            cpv_vals_medbias_list.append(cpv_vals_medbias[i])
            cpv_vals_lobias_list.append(cpv_vals_lobias[i])            
            i += 1

      cpvsig_75 = sorted(cpv_vals_list)[cut75]
      cpvsig_50 = sorted(cpv_vals_list)[cut50]
      cpvsig_best = cpv_vals_list[ibest]
      cpvsig_75_fullbias = sorted(cpv_vals_fullbias_list)[cut75]
      cpvsig_50_fullbias = sorted(cpv_vals_fullbias_list)[cut50]
      cpvsig_best_fullbias = cpv_vals_fullbias_list[ibest]
      cpvsig_75_medbias = sorted(cpv_vals_medbias_list)[cut75]
      cpvsig_50_medbias = sorted(cpv_vals_medbias_list)[cut50]
      cpvsig_best_medbias = cpv_vals_medbias_list[ibest]
      cpvsig_75_lobias = sorted(cpv_vals_lobias_list)[cut75]
      cpvsig_50_lobias = sorted(cpv_vals_lobias_list)[cut50]
      cpvsig_best_lobias = cpv_vals_lobias_list[ibest]


      cpvlist75.append(cpvsig_75)
      cpvlist50.append(cpvsig_50)
      cpvlistbest.append(cpvsig_best)
      cpvlist75_fullbias.append(cpvsig_75_fullbias)
      cpvlist50_fullbias.append(cpvsig_50_fullbias)
      cpvlistbest_fullbias.append(cpvsig_best_fullbias)
      cpvlist75_medbias.append(cpvsig_75_medbias)
      cpvlist50_medbias.append(cpvsig_50_medbias)
      cpvlistbest_medbias.append(cpvsig_best_medbias)
      cpvlist75_lobias.append(cpvsig_75_lobias)
      cpvlist50_lobias.append(cpvsig_50_lobias)
      cpvlistbest_lobias.append(cpvsig_best_lobias)

      
      f1.Close()


n = len(explist)
explist = array('d',explist)
cpvlist75 = array('d',cpvlist75)
cpvlist50 = array('d',cpvlist50)
cpvlistbest = array('d',cpvlistbest)

cpvlist75_fullbias = array('d',cpvlist75_fullbias)
cpvlist50_fullbias = array('d',cpvlist50_fullbias)
cpvlistbest_fullbias = array('d',cpvlistbest_fullbias)

cpvlist75_medbias = array('d',cpvlist75_medbias)
cpvlist50_medbias = array('d',cpvlist50_medbias)
cpvlistbest_medbias = array('d',cpvlistbest_medbias)

cpvlist75_lobias = array('d',cpvlist75_lobias)
cpvlist50_lobias = array('d',cpvlist50_lobias)
cpvlistbest_lobias = array('d',cpvlistbest_lobias)

g_cpvsig_75 = ROOT.TGraph(n,explist,cpvlist75)
g_cpvsig_50 = ROOT.TGraph(n,explist,cpvlist50)
g_cpvsig_best = ROOT.TGraph(n,explist,cpvlistbest)

g_cpvsig_75_fullbias = ROOT.TGraph(n,explist,cpvlist75_fullbias)
g_cpvsig_50_fullbias = ROOT.TGraph(n,explist,cpvlist50_fullbias)
g_cpvsig_best_fullbias = ROOT.TGraph(n,explist,cpvlistbest_fullbias)

g_cpvsig_75_medbias = ROOT.TGraph(n,explist,cpvlist75_medbias)
g_cpvsig_50_medbias = ROOT.TGraph(n,explist,cpvlist50_medbias)
g_cpvsig_best_medbias = ROOT.TGraph(n,explist,cpvlistbest_medbias)

g_cpvsig_75_lobias = ROOT.TGraph(n,explist,cpvlist75_lobias)
g_cpvsig_50_lobias = ROOT.TGraph(n,explist,cpvlist50_lobias)
g_cpvsig_best_lobias = ROOT.TGraph(n,explist,cpvlistbest_lobias)

graph_cpvrange75 = filldiff(g_cpvsig_75,g_cpvsig_75_fullbias)
graph_cpvrange50 = filldiff(g_cpvsig_50,g_cpvsig_50_fullbias)
graph_cpvbestrange = filldiff(g_cpvsig_best,g_cpvsig_best_fullbias)

g_cpvsig_75.SetLineWidth(3)
g_cpvsig_50.SetLineWidth(3)
g_cpvsig_best.SetLineWidth(3)
g_cpvsig_75_fullbias.SetLineWidth(3)
g_cpvsig_50_fullbias.SetLineWidth(3)
g_cpvsig_best_fullbias.SetLineWidth(3)
g_cpvsig_75_medbias.SetLineWidth(3)
g_cpvsig_50_medbias.SetLineWidth(3)
g_cpvsig_best_medbias.SetLineWidth(3)
g_cpvsig_75_lobias.SetLineWidth(3)
g_cpvsig_50_lobias.SetLineWidth(3)
g_cpvsig_best_lobias.SetLineWidth(3)

g_cpvsig_75_fullbias.SetLineStyle(2)
g_cpvsig_50_fullbias.SetLineStyle(2)
g_cpvsig_best_fullbias.SetLineStyle(2)

g_cpvsig_75_medbias.SetLineStyle(3)
g_cpvsig_50_medbias.SetLineStyle(3)
g_cpvsig_best_medbias.SetLineStyle(3)

g_cpvsig_75_lobias.SetLineStyle(4)
g_cpvsig_50_lobias.SetLineStyle(4)
g_cpvsig_best_lobias.SetLineStyle(4)


c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(0,0.0,1500.0,12.0)
h1.SetTitle("CP Violation Sensitivity")
h1.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
#graph_cpvrange75.SetFillColor(ROOT.kCyan+2)
#graph_cpvrange75.SetLineColor(0)
#graph_cpvrange75.Draw("F same")
#g_cpvsig_75.Draw("L same")
#g_cpvsig_75_fullbias.Draw("L same")
#g_cpvsig_75_medbias.Draw("L same")
#g_cpvsig_75_lobias.Draw("L same")

#graph_cpvrange50.SetFillColor(ROOT.kCyan-7)
#graph_cpvrange50.SetLineColor(0)
#graph_cpvrange50.Draw("F same")
#g_cpvsig_50.Draw("L same")
#g_cpvsig_50_fullbias.Draw("L same")
#g_cpvsig_50_medbias.Draw("L same")
#g_cpvsig_50_lobias.Draw("L same")

graph_cpvbestrange.SetFillColor(ROOT.kPink-3)
graph_cpvbestrange.SetLineColor(0)
graph_cpvbestrange.Draw("F same")
g_cpvsig_best.Draw("L same")
g_cpvsig_best_fullbias.Draw("L same")
g_cpvsig_best_medbias.Draw("L same")
g_cpvsig_best_lobias.Draw("L same")

t1 = ROOT.TPaveText(0.16,0.72,0.6,0.89,"NDC")
t1.AddText("DUNE Sensitivity")
t1.AddText("All Systematics")
t1.AddText(htext)
if (hier == 'nh'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")
elif (hier == 'ih'):
      t1.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t1.AddText("sin^{2}#theta_{23} = 0.583 unconstrained")
t1.SetFillStyle(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.7,0.89,0.89)
l1.AddEntry(graph_cpvbestrange, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(g_cpvsig_best, "Nominal Sensitivity","L")
l1.AddEntry(g_cpvsig_best_lobias, "Low Bias","L")
l1.AddEntry(g_cpvsig_best_medbias, "Medium Bias","L")
l1.AddEntry(g_cpvsig_best_fullbias, "Full Bias","L")
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

outname = "plot_v4/exposures/cpv_exp_bias_max_"+hier+"_2019_v4.eps"
outname2 = "plot_v4/exposures/cpv_exp_bias_max_"+hier+"_2019_v4.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)


      

