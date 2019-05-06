#!/usr/bin/env python

import sys
import math
import ROOT
import random

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

#Groupings indicate colors I've used together

#Used in the CPV/MH and bubble plots
greenColor = ROOT.kGreen-7
orangeColor = ROOT.kOrange-3
blueColor = ROOT.kBlue-7

#Used to highlight allowed regions
yellowHighlightColor = ROOT.kYellow-7

#Used in exposure plots
darkcyanColor = ROOT.kCyan+2
cyanColor = ROOT.kCyan-7
redColor = ROOT.kPink-3

#Make some histograms just to use in the example
ghist1 = ROOT.TH1F("ghist1","Example histogram",50,-3.,3.0)
for i in range(1000): ghist1.Fill(random.gauss(0,0.2))
ghist2 = ROOT.TH1F("ghist2","Example histogram",50,-3.,3.0)
for i in range(1000): ghist2.Fill(random.gauss(1,0.2))
ghist3 = ROOT.TH1F("ghist3","Example histogram",50,-3.,3.0)
for i in range(1000): ghist3.Fill(random.gauss(-1,0.2))
box1 = ROOT.TBox(-2,0,-0.5,300.)

ghist1.SetLineWidth(3)
ghist2.SetLineWidth(3)
ghist3.SetLineWidth(3)

ghist1.SetLineColor(greenColor)
ghist1.SetFillColor(greenColor)
ghist1.SetFillStyle(1001)
ghist2.SetLineColor(orangeColor)
ghist3.SetLineColor(blueColor)
box1.SetLineColor(yellowHighlightColor)
box1.SetFillColor(yellowHighlightColor)

#Set up canvas and plot
c1 = ROOT.TCanvas("c1","c1",800,800)
c1.SetLeftMargin(0.15)
h1 = c1.DrawFrame(-3.0,0.0,3.0,325.0)
h1.SetTitle("Title Goes Here")
h1.GetXaxis().SetTitle("x axis label")
h1.GetXaxis().CenterTitle()
h1.GetYaxis().SetTitle("yaxis label")
h1.GetYaxis().SetTitleOffset(1.3)
h1.GetYaxis().CenterTitle()
c1.Modified()
box1.Draw("same")
ghist1.Draw("same")
ghist2.Draw("same")
ghist3.Draw("same")
ROOT.gPad.RedrawAxis()

#Text box
t1 = ROOT.TPaveText(0.16,0.75,0.53,0.89,"NDC")
t1.AddText("DUNE Plot")
t1.AddText("GP Burdell Model")
t1.AddText("Text line 3")
t1.AddText("Text line 4")
t1.SetFillColor(0)
t1.SetBorderSize(0)
t1.SetTextAlign(12)
t1.Draw("same")

#Legend
l1 = ROOT.TLegend(0.55,0.75,0.89,0.89)
l1.AddEntry(ghist1,"Hist1","F")
l1.AddEntry(ghist2,"Hist2","L")
l1.AddEntry(ghist3,"Hist3","L")
l1.AddEntry(box1,"Highlighted Area","F")
l1.SetBorderSize(0)
l1.SetFillStyle(0)
l1.Draw()

#Write out
outname = "myplot.png"
c1.SaveAs(outname)


