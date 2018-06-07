{
// Plot the energy spectrum of the primary particles
gROOT -> Reset();

TFile f("brachytherapy.root");
  
// Draw histos filled by Geant4 simulation 
//   
  
TCanvas* c1 = new TCanvas("c1", " ");


h10 -> GetXaxis()->SetTitle("Energy (KeV)");
h10 -> GetYaxis()->SetTitle("Events");
h10 -> SetTitle("");

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

h10 -> GetXaxis()->SetTitleSize(tsize);
h10 -> GetXaxis()->SetTitleFont(font);
h10 -> GetXaxis()->SetTitleOffset(offset);
h10 -> GetXaxis()->SetLabelFont(font);
h10 -> GetXaxis()->SetLabelSize(tsize);
//h10 -> GetXaxis()->SetLabelOffset(offset);

h10 -> GetYaxis()->SetTitleSize(tsize);
h10 -> GetYaxis()->SetTitleFont(font);
h10 -> GetYaxis()->SetTitleOffset(offset);
h10 -> GetYaxis()->SetLabelFont(font);
h10 -> GetYaxis()->SetLabelSize(tsize);
//h10 -> GetXaxis()->SetLabelOffset(offset);

h10.Draw();
}
