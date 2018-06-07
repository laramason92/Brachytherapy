{
// Plot the energy spectrum of the primary particles
gROOT -> Reset();

TFile f("brachytherapy.root");
  
// Draw histos filled by Geant4 simulation 
//   
  
TCanvas* c1 = new TCanvas("c1", " ");
h20 -> GetXaxis()->SetTitle("x (mm)");
//h20 ->GetXaxis()->SetRangeUser(-1,1);
h20 -> GetYaxis()->SetTitle("y (mm)");
//h20 ->GetYaxis()->SetRangeUser(-1,1);
h20 -> SetTitle("");

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

h20 -> GetXaxis()->SetTitleSize(tsize);
h20 -> GetXaxis()->SetTitleFont(font);
h20 -> GetXaxis()->SetTitleOffset(offset);
h20 -> GetXaxis()->SetLabelFont(font);
h20 -> GetXaxis()->SetLabelSize(tsize);
//h20 -> GetXaxis()->SetLabelOffset(offset);

h20 -> GetYaxis()->SetTitleSize(tsize);
h20 -> GetYaxis()->SetTitleFont(font);
h20 -> GetYaxis()->SetTitleOffset(offset);
h20 -> GetYaxis()->SetLabelFont(font);
h20 -> GetYaxis()->SetLabelSize(tsize);
//h20 -> GetXaxis()->SetLabelOffset(offset);

h20.Draw("COLZ");
}
