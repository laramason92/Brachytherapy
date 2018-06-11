{
// Plot the energy spectrum of the primary particles
gROOT -> Reset();

TFile f("brachytherapy.root");
  
// Draw histos filled by Geant4 simulation 
//   
  
TCanvas* c1 = new TCanvas("c1", " ");
h50 -> GetXaxis()->SetTitle("x (mm)");
h50 ->GetXaxis()->SetRangeUser(-100,100);
h50 -> GetYaxis()->SetTitle("y (mm)");
h50 ->GetYaxis()->SetRangeUser(-100,100);
h50 -> SetTitle("");

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

h50 -> GetXaxis()->SetTitleSize(tsize);
h50 -> GetXaxis()->SetTitleFont(font);
h50 -> GetXaxis()->SetTitleOffset(offset);
h50 -> GetXaxis()->SetLabelFont(font);
h50 -> GetXaxis()->SetLabelSize(tsize);
//h50 -> GetXaxis()->SetLabelOffset(offset);

h50 -> GetYaxis()->SetTitleSize(tsize);
h50 -> GetYaxis()->SetTitleFont(font);
h50 -> GetYaxis()->SetTitleOffset(offset);
h50 -> GetYaxis()->SetLabelFont(font);
h50 -> GetYaxis()->SetLabelSize(tsize);
//h50 -> GetXaxis()->SetLabelOffset(offset);


h50.Draw("COLZ");
}
