TFile *f = new TFile("brachytherapy.root");
TH1F* h1 = (TH1F*)f.Get("h10");
h1->Draw();
