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

for myexp in explist:

      if (myexp==0):
            continue

      #No th13 penalty CPV
      filename = "root_v4/sens_staging/cpv_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_nopen_hie"+hnum+"_asimov0_v4.root"
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

      #Th13 Penalty CPV
      filename = "root_v4/sens_staging/cpv_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov0_v4.root"
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

      #No th13 penalty MH
      filename = "root_v4/sens_staging/mh_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_nopen_hie"+hnum+"_asimov0_v4.root"
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

      #Th13 Penalty MH
      filename = "root_v4/sens_staging/mh_sens_ndfd_"+str(myexp)+"kTMWyr_allsyst_th13_hie"+hnum+"_asimov0_v4.root"
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

n = len(explist)
explist = array('d',explist)
cpvlist75_lo = array('d',cpvlist75_lo)
cpvlist75_hi = array('d',cpvlist75_hi)

cpvlist50_lo = array('d',cpvlist50_lo)
cpvlist50_hi = array('d',cpvlist50_hi)

cpvlistbest_lo = array('d',cpvlistbest_lo)
cpvlistbest_hi = array('d',cpvlistbest_hi)

mhlist100_lo = array('d',mhlist100_lo)
mhlist100_hi = array('d',mhlist100_hi)

mhlistbest_lo = array('d',mhlistbest_lo)
mhlistbest_hi = array('d',mhlistbest_hi)

g_cpvsig_75_lo = ROOT.TGraph(n,explist,cpvlist75_lo)
g_cpvsig_75_hi = ROOT.TGraph(n,explist,cpvlist75_hi)

g_cpvsig_50_lo = ROOT.TGraph(n,explist,cpvlist50_lo)
g_cpvsig_50_hi = ROOT.TGraph(n,explist,cpvlist50_hi)

g_cpvsig_best_lo = ROOT.TGraph(n,explist,cpvlistbest_lo)
g_cpvsig_best_hi = ROOT.TGraph(n,explist,cpvlistbest_hi)

g_mhsig_100_lo = ROOT.TGraph(n,explist,mhlist100_lo)
g_mhsig_100_hi = ROOT.TGraph(n,explist,mhlist100_hi)

g_mhsig_best_lo = ROOT.TGraph(n,explist,mhlistbest_lo)
g_mhsig_best_hi = ROOT.TGraph(n,explist,mhlistbest_hi)

g_cpvsig_75_lo.SetLineWidth(3)
g_cpvsig_75_lo.SetLineStyle(3)
g_cpvsig_75_hi.SetLineWidth(3)

g_cpvsig_50_lo.SetLineWidth(3)
g_cpvsig_50_lo.SetLineStyle(3)
g_cpvsig_50_hi.SetLineWidth(3)

g_cpvsig_best_hi.SetLineWidth(3)
g_cpvsig_best_lo.SetLineWidth(3)
g_cpvsig_best_lo.SetLineStyle(3)

g_mhsig_100_lo.SetLineWidth(3)
g_mhsig_100_lo.SetLineStyle(3)
g_mhsig_100_hi.SetLineWidth(3)

g_mhsig_best_lo.SetLineWidth(3)
g_mhsig_best_lo.SetLineStyle(3)
g_mhsig_best_hi.SetLineWidth(3)

graph_cpvrange75 = filldiff(g_cpvsig_75_hi,g_cpvsig_75_lo)
graph_cpvrange50 = filldiff(g_cpvsig_50_hi,g_cpvsig_50_lo)
graph_cpvbestrange = filldiff(g_cpvsig_best_hi,g_cpvsig_best_lo)

graph_mhrange100 = filldiff(g_mhsig_100_hi, g_mhsig_100_lo)
graph_mhrangebest = filldiff(g_mhsig_best_hi, g_mhsig_best_lo)

f_res = ROOT.TFile("root_v4/throws/res_vs_exposure.root")
graph_dcpres0_noconstr = f_res.Get("asimov10_dcp_nopen")
graph_dcpres0_th13 = f_res.Get("asimov10_dcp_th13")
graph_dcpresneg_noconstr = f_res.Get("asimov11_dcp_nopen")
graph_dcpresneg_th13 = f_res.Get("asimov11_dcp_th13")

f_res = ROOT.TFile("root_v4/throws/res_vs_exposure.root")
graph_th13res_noconstr = f_res.Get("asimov0_th13_nopen")
graph_th23res_noconstr = f_res.Get("asimov0_th23_nopen")
graph_th23res_th13 = f_res.Get("asimov0_th23_th13")
graph_dmsqres_noconstr = f_res.Get("asimov0_dm2_nopen")
graph_dmsqres_th13 = f_res.Get("asimov0_dm2_th13")

#hack to fix the some plots
graph_th13res_noconstr = fix450(graph_th13res_noconstr)
graph_th23res_noconstr = fix450(graph_th23res_noconstr)
#graph_th23res_th13 = fix450(graph_th23res_th13)

graph_diff_dcpres0 = filldiff(graph_dcpres0_noconstr,graph_dcpres0_th13)
graph_diff_dcpresneg = filldiff(graph_dcpresneg_noconstr,graph_dcpresneg_th13)
graph_diff_th23res = filldiff(graph_th23res_noconstr,graph_th23res_th13)
graph_diff_dmsqres = filldiff(graph_dmsqres_noconstr,graph_dmsqres_th13)

graph_dcpres0_noconstr.SetLineWidth(3)
graph_dcpresneg_noconstr.SetLineWidth(3)
graph_dcpresneg_noconstr.SetLineColor(ROOT.kBlack)
graph_dcpres0_th13.SetLineWidth(3)
graph_dcpresneg_th13.SetLineWidth(3)
graph_dcpresneg_th13.SetLineColor(ROOT.kBlack)
graph_th13res_noconstr.SetLineWidth(4)
graph_th23res_noconstr.SetLineWidth(3)
graph_dmsqres_noconstr.SetLineWidth(3)
graph_th23res_th13.SetLineWidth(3)
graph_dmsqres_th13.SetLineWidth(3)

graph_dcpres0_noconstr.SetLineStyle(3)
graph_dcpresneg_noconstr.SetLineStyle(3)
graph_th13res_noconstr.SetLineStyle(3)
graph_th23res_noconstr.SetLineStyle(3)
graph_dmsqres_noconstr.SetLineStyle(3)

myout = ROOT.TFile("root_v4/exposure_graphs_"+hier+".root","recreate")
g_cpvsig_75_lo.SetName("cpvsig75_nopen")
g_cpvsig_50_lo.SetName("cpvsig50_nopen")
g_cpvsig_best_lo.SetName("cpvsigbest_nopen")
g_cpvsig_75_hi.SetName("cpvsig75_th13pen")
g_cpvsig_50_hi.SetName("cpvsig50_th13pen")
g_cpvsig_best_hi.SetName("cpvsigbest_th13pen")
g_mhsig_100_lo.SetName("mhsig100_nopen")
g_mhsig_best_lo.SetName("mhsigbest_nopen")
g_mhsig_100_hi.SetName("mhsig100_th13pen")
g_mhsig_best_hi.SetName("mhsigbest_th13pen")

graph_dcpres0_noconstr.SetName("dcpres0_nopen")
graph_dcpresneg_noconstr.SetName("dcpresneg_nopen")
graph_dcpres0_th13.SetName("dcpres0_th13pen")
graph_dcpresneg_th13.SetName("dcpresneg_th13pen")

graph_th13res_noconstr.SetName("th13res_nopen")
graph_th23res_noconstr.SetName("th23res_nopen")
graph_dmsqres_noconstr.SetName("dmsqres_nopen")

graph_th23res_th13.SetName("th23res_th13pen")
graph_dmsqres_th13.SetName("dmsqres_th13pen")

g_cpvsig_75_lo.Write()
g_cpvsig_50_lo.Write()
g_cpvsig_best_lo.Write()
g_cpvsig_75_hi.Write()
g_cpvsig_50_hi.Write()
g_cpvsig_best_hi.Write()
g_mhsig_100_lo.Write()
g_mhsig_best_lo.Write()
g_mhsig_100_hi.Write()
g_mhsig_best_hi.Write()
graph_dcpres0_noconstr.Write()
graph_dcpresneg_noconstr.Write()
graph_dcpres0_th13.Write()
graph_dcpresneg_th13.Write()
graph_th13res_noconstr.Write()
graph_th23res_noconstr.Write()
graph_dmsqres_noconstr.Write()
graph_th23res_th13.Write()
graph_dmsqres_th13.Write()
myout.Close()


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
g_cpvsig_75_lo.Draw("L same")
g_cpvsig_75_hi.Draw("L same")

graph_cpvrange50.SetFillColor(ROOT.kCyan-7)
graph_cpvrange50.SetLineColor(0)
graph_cpvrange50.Draw("F same")
g_cpvsig_50_lo.Draw("L same")
g_cpvsig_50_hi.Draw("L same")

graph_cpvbestrange.SetFillColor(ROOT.kPink-3)
graph_cpvbestrange.SetLineColor(0)
graph_cpvbestrange.Draw("F same")
g_cpvsig_best_lo.Draw("L same")
g_cpvsig_best_hi.Draw("L same")

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

l1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
l1.AddEntry(graph_cpvbestrange, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(graph_cpvrange50, "50% of #delta_{CP} values","F")
l1.AddEntry(graph_cpvrange75, "75% of #delta_{CP} values","F")
l1.AddEntry(g_cpvsig_75_hi,"Nominal Analysis","L")
l1.AddEntry(g_cpvsig_75_lo,"#theta_{13} unconstrained","L")
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

outname = "plot_v4/exposures/cpv_exp_varyconstr_"+hier+"_2019_v4.eps"
outname2 = "plot_v4/exposures/cpv_exp_varyconstr_"+hier+"_2019_v4.png"
c1.SaveAs(outname)
c1.SaveAs(outname2)

c1a = ROOT.TCanvas("c1a","c1a",800,800)
c1a.SetLeftMargin(0.15)
h1a = c1.DrawFrame(0,0.0,1000.0,12.0)
h1a.SetTitle("CP Violation Sensitivity")
h1a.GetXaxis().SetTitle("Exposure (kt-MW-years)")
h1a.GetYaxis().SetTitle("#sigma = #sqrt{#bar{#Delta#chi^{2}}}")
h1a.GetYaxis().SetTitleOffset(1.3)
h1a.GetYaxis().CenterTitle()
c1a.Modified()

graph_cpvbestrange.SetFillColor(ROOT.kPink-3)
graph_cpvbestrange.SetLineColor(0)
graph_cpvbestrange.Draw("F same")
g_cpvsig_best_lo.Draw("L same")
g_cpvsig_best_hi.Draw("L same")

t1.Draw("same")

l1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
l1.AddEntry(graph_cpvbestrange, "#delta_{CP} = -#pi/2","F")
l1.AddEntry(g_cpvsig_75_hi,"Nominal Analysis","L")
l1.AddEntry(g_cpvsig_75_lo,"#theta_{13} unconstrained","L")
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

outname = "plot_v4/exposures/cpv_exp_varyconstr_"+hier+"_2019_v4_maxcpv.eps"
outname2 = "plot_v4/exposures/cpv_exp_varyconstr_"+hier+"_2019_v4_maxcpv.png"
c1a.SaveAs(outname)
c1a.SaveAs(outname2)

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
      g_mhsig_best_lo.Draw("L same")
      g_mhsig_best_hi.Draw("L same")
graph_mhrange100.Draw("F same")
g_mhsig_100_lo.Draw("L same")
g_mhsig_100_hi.Draw("L same")

t1.Draw("same")

lm1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
if (hier == "nh"):
      lm1.AddEntry(graph_mhrangebest, "#delta_{CP} = -#pi/2","F")
lm1.AddEntry(graph_mhrange100, "100% of #delta_{CP} values","F")
lm1.AddEntry(g_mhsig_100_hi,"Nominal Analysis","L")
lm1.AddEntry(g_mhsig_100_lo,"#theta_{13} unconstrained","L")      
lm1.SetBorderSize(0)
lm1.SetFillStyle(0)
lm1.Draw("same")

line3 = ROOT.TLine(0.0,5.,500.,5.)
line3.SetLineStyle(2)
line3.SetLineWidth(3)
line3.Draw("same")

outname = "plot_v4/exposures/mh_exp_varyconstr_"+hier+"_2019_v4.eps"
outname2 = "plot_v4/exposures/mh_exp_varyconstr_"+hier+"_2019_v4.png"
c2.SaveAs(outname)
c2.SaveAs(outname2)

if (hier == "nh"):

      c3 = ROOT.TCanvas("c3","c3",800,800)
      c3.SetLeftMargin(0.15)
      h3 = c3.DrawFrame(0,0.0,1500.,60.)
      h3.SetTitle("")
      h3.GetXaxis().SetTitle("Exposure (kt-MW-years)")
      h3.GetYaxis().SetTitle("#delta_{cp} resolution (degrees)")
      h3.GetYaxis().SetTitleOffset(1.3)
      h3.GetYaxis().CenterTitle()
      c3.Modified()
      graph_diff_dcpres0.SetFillColor(ROOT.kCyan+3)
      graph_diff_dcpres0.SetLineColor(0)
      graph_diff_dcpresneg.SetFillColor(ROOT.kPink-3)
      graph_diff_dcpresneg.SetLineColor(0)
      graph_diff_dcpres0.Draw("F same")
      graph_dcpres0_noconstr.Draw("L same")
      graph_dcpres0_th13.Draw("L same")
      graph_diff_dcpresneg.Draw("F same")
      graph_dcpresneg_noconstr.Draw("L same")
      graph_dcpresneg_th13.Draw("L same")

      t2 = ROOT.TPaveText(0.16,0.7,0.6,0.89,"NDC")
      t2.AddText("DUNE Sensitivity")
      t2.AddText("All Systematics")
      t2.AddText(htext)
      t2.AddText("sin^{2}2#theta_{13} = 0.088 #pm 0.003")
      t2.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")      
      #t2.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
      t2.SetFillStyle(0)
      t2.SetBorderSize(0)
      t2.SetTextAlign(12)

      t2.Draw("same")

      lm1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
      lm1.AddEntry(graph_diff_dcpresneg, "#delta_{CP} = -#pi/2","F")
      lm1.AddEntry(graph_diff_dcpres0, "#delta_{CP} = 0","F")
      lm1.AddEntry(graph_dcpres0_th13,"Nominal Analysis","L")
      lm1.AddEntry(graph_dcpres0_noconstr,"#theta_{13} unconstrained","L")      
      lm1.SetBorderSize(0)
      lm1.SetFillStyle(0)
      lm1.Draw("same")

      outname = "plot_v4/res/dcpres_exp_varyconstr_"+hier+"_2019_v4.eps"
      outname2 = "plot_v4/res/dcpres_exp_varyconstr_"+hier+"_2019_v4.png"
      c3.SaveAs(outname)
      c3.SaveAs(outname2)

      c4 = ROOT.TCanvas("c4","c4",800,800)
      c4.SetLeftMargin(0.15)
      h4 = c4.DrawFrame(0,0.0,1500.,0.02)
      h4.SetTitle("")
      h4.GetXaxis().SetTitle("Exposure (kt-MW-years)")
      h4.GetYaxis().SetTitle("sin^{2}(2#theta_{23}) Resolution")
      h4.GetYaxis().SetTitleOffset(1.7)
      h4.GetYaxis().CenterTitle()
      c4.Modified()
      graph_diff_th23res.SetFillColor(ROOT.kCyan+3)
      graph_diff_th23res.SetLineColor(0)
      graph_diff_th23res.Draw("F same")
      graph_th23res_noconstr.Draw("l same")
      graph_th23res_th13.Draw("l same")

      t2.Draw("same")

      lm1 = ROOT.TLegend(0.55,0.78,0.89,0.89)
      lm1.AddEntry(graph_th23res_th13,"Nominal Analysis","L")
      lm1.AddEntry(graph_th23res_noconstr,"#theta_{13} unconstrained","L")      
      lm1.SetBorderSize(0)
      lm1.SetFillStyle(0)
      lm1.Draw("same")

      outname = "plot_v4/res/th23res_exp_varyconstr_"+hier+"_2019_v4.eps"
      outname2 = "plot_v4/res/th23res_exp_varyconstr_"+hier+"_2019_v4.png"
      c4.SaveAs(outname)
      c4.SaveAs(outname2)

      c5 = ROOT.TCanvas("c5","c5",800,800)
      c5.SetLeftMargin(0.15)
      h5 = c5.DrawFrame(0,0.0,1500.,0.05)
      h5.SetTitle("")
      h5.GetXaxis().SetTitle("Exposure (kt-MW-years)")
      h5.GetYaxis().SetTitle("#Deltam^{2}_{32} Resolution (eV^{2} x 10^{-3})")
      h5.GetYaxis().SetTitleOffset(1.8)
      h5.GetYaxis().CenterTitle()
      c5.Modified()
      graph_diff_dmsqres.SetFillColor(ROOT.kCyan+3)
      graph_diff_dmsqres.SetLineColor(0)
      #graph_diff_dmsqres.Draw("F same")
      #graph_dmsqres_noconstr.Draw("L same")
      graph_dmsqres_noconstr.SetLineWidth(4)
      graph_dmsqres_noconstr.SetLineColor(ROOT.kCyan+3)
      graph_dmsqres_noconstr.Draw("L same")

      t3 = ROOT.TPaveText(0.16,0.7,0.6,0.89,"NDC")
      t3.AddText("DUNE Sensitivity")
      t3.AddText("All Systematics")
      t3.AddText(htext)
      t3.AddText("sin^{2}2#theta_{13} = 0.088 unconstrained")
      t3.AddText("sin^{2}#theta_{23} = 0.580 unconstrained")      
      #t3.AddText("0.4 < sin^{2}#theta_{23} < 0.6")
      t3.SetFillStyle(0)
      t3.SetBorderSize(0)
      t3.SetTextAlign(12)
      

      t3.Draw("same")
      
      null = ROOT.TObject()
      lm1 = ROOT.TLegend(0.55,0.85,0.89,0.89)
      lm1.AddEntry(graph_dmsqres_noconstr,"#theta_{13} unconstrained","L")
      lm1.SetBorderSize(0)
      lm1.SetFillStyle(0)
      lm1.Draw("same")

      outname = "plot_v4/res/dmsqres_exp_varyconstr_"+hier+"_2019_v4.eps"
      outname2 = "plot_v4/res/dmsqres_exp_varyconstr_"+hier+"_2019_v4.png"
      c5.SaveAs(outname)
      c5.SaveAs(outname2)

      c6 = ROOT.TCanvas("c6","c6",800,800)
      c6.SetLeftMargin(0.15)
      h6 = c6.DrawFrame(0,0.0,1500.,0.03)
      h6.SetTitle("")
      h6.GetXaxis().SetTitle("Exposure (kt-MW-years)")
      h6.GetYaxis().SetTitle("sin^{2}(2#theta_{13}) Resolution")
      h6.GetYaxis().SetTitleOffset(1.8)
      h6.GetYaxis().CenterTitle()
      c6.Modified()
      graph_th13res_noconstr.SetLineWidth(4)
      graph_th13res_noconstr.SetLineColor(ROOT.kCyan+3)
      graph_th13res_noconstr.Draw("l same")

      t3.Draw("same")

      lm1 = ROOT.TLegend(0.55,0.85,0.89,0.89)
      lm1.AddEntry(graph_th13res_noconstr,"#theta_{13} unconstrained","L")
      lm1.SetBorderSize(0)
      lm1.SetFillStyle(0)
      lm1.Draw("same")

      outname = "plot_v4/res/th13res_exp_varyconstr_"+hier+"_2019_v4.eps"
      outname2 = "plot_v4/res/th13res_exp_varyconstr_"+hier+"_2019_v4.png"
      c6.SaveAs(outname)
      c6.SaveAs(outname2)
      

