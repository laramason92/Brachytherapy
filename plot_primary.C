{
// Plot the energy spectrum of the primary particles
gROOT -> Reset();

TFile f("brachytherapy.root");
  
// Draw histos filled by Geant4 simulation 
//   
  
TCanvas* c1 = new TCanvas("c1", " ");
h10->GetXaxis()->SetTitle("Energy (keV)");
h10->GetYaxis()->SetTitle("Events");
h10->SetTitle("");
h10->SetStats(kFALSE);
h10->GetXaxis()->SetTitleSize(0.04);
h10->GetYaxis()->SetTitleSize(0.04);

c1.Update();
h10.Draw();
c1.SaveAs(“plot_primary_spec.eps”);
}
