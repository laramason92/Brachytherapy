{
// Plot the energy spectrum of the primary particles
gROOT -> Reset();

TFile f("brachytherapy.root");
  
// Draw histos filled by Geant4 simulation 
//   
  
TCanvas* c1 = new TCanvas("c1", " ");
h30 -> GetXaxis()->SetTitle("x (mm)");
h30 ->GetXaxis()->SetRangeUser(-100,100);
h30 -> GetYaxis()->SetTitle("y (mm)");
h30 ->GetYaxis()->SetRangeUser(-100,100);
h30 -> SetTitle("");

//STYLE TINGS
gStyle->SetOptStat(0);
c1->SetTopMargin(0.05);
c1->SetRightMargin(0.05);
c1->SetBottomMargin(0.1);
c1->SetLeftMargin(0.1);
c1->SetTicks(0,0);
Int_t font=42;
Double_t tsize=0.04;
Int_t offset=1;

h30 -> GetXaxis()->SetTitleSize(tsize);
h30 -> GetXaxis()->SetTitleFont(font);
h30 -> GetXaxis()->SetTitleOffset(offset);
h30 -> GetXaxis()->SetLabelFont(font);
h30 -> GetXaxis()->SetLabelSize(tsize);
//h30 -> GetXaxis()->SetLabelOffset(offset);

h30 -> GetYaxis()->SetTitleSize(tsize);
h30 -> GetYaxis()->SetTitleFont(font);
h30 -> GetYaxis()->SetTitleOffset(offset);
h30 -> GetYaxis()->SetLabelFont(font);
h30 -> GetYaxis()->SetLabelSize(tsize);
//h30 -> GetXaxis()->SetLabelOffset(offset);


h30.Draw("COLZ");
}
