{
#include<iostream>
#include<stdlib.h>
#include<math.h>

Int_t numberOfBins=801;

gROOT -> Reset();
TFile f1("brachytherapy_HM_1.root");
TFile f2("brachytherapy_HM_2.root");
TFile f3("brachytherapy_HM_3.root");
TFile f4("brachytherapy_HM_4.root");
TFile f5("brachytherapy_HM_5.root");
TFile g("brachytherapy_new_vector.root");

Double_t EnergyMap[401][91]; //2D map of total energy in "radial distance (mm)" and "angle (degrees)"
Int_t Voxels[401][91]; //the number of voxels used to provide dose to each element of the energy map 

TH2F* hist_HM_1 = (TH2F*)f1.Get("hgeom");
TH2F* hist_HM_2 = (TH2F*)f2.Get("hgeom");
TH2F* hist_HM_3 = (TH2F*)f3.Get("hgeom");
TH2F* hist_HM_4 = (TH2F*)f4.Get("hgeom");
TH2F* hist_HM_5 = (TH2F*)f5.Get("hgeom");

for (int i=0; i <401; i++)
 {
 for (int j=0; j<91; j++)
  {
   EnergyMap[i][j]=0.;
   Voxels[i][j]=0.;
}}

for (int q=0; q< numberOfBins; q++)
 {
   for (int w=0; w<numberOfBins; w++)
 {
 

}
