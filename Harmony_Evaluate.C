{
#include<iostream>
#include<stdlib.h>
#include<math.h>

gROOT -> Reset();
TFile f("brachytherapy_newHMvector.root");

Double_t EnergyMap[401][91]; //2D map of total energy in "radial distance (mm)" and "angle (degrees)"
Int_t Voxels[401][91]; //the number of voxels used to provide dose to each element of the energy map 

}
