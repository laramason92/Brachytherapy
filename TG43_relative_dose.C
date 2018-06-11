{
// Create output file geant4_dose.txt with the dose rate distribution, calculated
// with the simulation results containted in brachytherapy.root

gROOT -> Reset();
TFile f("brachytherapy.root");
 					     
Double_t L = 0.35; //seed length in cm

Double_t EnergyMap[401]; //2D map of total energy in "radial distance (mm)" and "angle (5 degrees)"
Int_t Voxels[401]; //the number of voxels used to provide dose to each element of the energy map
Double_t normDose[401]; //Energy map divided by voxels used to make cell, normalised to energy deposition at 1cm, 90 degrees
Double_t GeomFunction[401]; //Geometry Function, normalised to the geometry function at the reference point
Double_t GeometryFunctionZero;  //Geometry function at reference point, 1cm and 90 degrees
Double_t beta;  //beta angle for Geometry Function calculation
Double_t R;     //radial distance in cm
Double_t K;     //polar angle in radians
Double_t Radial[401]; //radial dose function
Double_t radius; //radius (mm)
Double_t radius_k; //radius (mm)
Double_t radius_geom;
Double_t theta;
Double_t theta_1;
Double_t theta_2;
Double_t GL;
Double_t GL_0;

Int_t radInt; //nearest integer of radius (mm)
Int_t numberOfBins=801;
Int_t numberOfBinsKerma=201;
Double_t Sk; // = ?? todo!
Double_t D_dot_0; // = ?? todo!
// ******** calculate the TG43 params!
// Double_t Lambda = D_dot_0/Sk; //cm-2

for (int i=0; i <401; i++)
 {
 EnergyMap[i]=0.;
 Voxels[i]=0.;
}

//Build Energy Deposition Map
for (int k=0; k< numberOfBins; k++)
 {
   for (int m=0; m< numberOfBins; m++) 
 {
   Double_t xx_histo = h20.GetXaxis()->GetBinCenter(k);
   //cout << "k  " << k << "xx_histo  "<< xx_histo << endl;
   Double_t yy_histo = h20.GetYaxis()->GetBinCenter(m);
   Double_t edep_histo=h20.GetBinContent(k, m);
   radius = sqrt(xx_histo*xx_histo+yy_histo*yy_histo); //This is the way to do the radial dose

 //  if ((edep_histo!=0) && radius < 12. && radius > 9) std::cout << "histo: " << xx_histo << ", " << yy_histo 
   //                                                             << ", radius: " << radius <<", edep: "<< edep_histo << std::endl;

    if (radius != 0){
		      radInt = TMath::Nint(4*radius);
		      if ((radInt>0)&&(radInt<=400))
			{
			 EnergyMap[radInt]+= edep_histo;
			 Voxels[radInt]+= 1; //store the number of voxels
                      //   if (radius < 12. && radius > 9 && edep_histo!=0)std::cout<< "Radius: " << radius << ", radInt:"<<radInt << ", EnergyMap: "<< EnergyMap[radInt]<< ", voxels: " << Voxels[radInt]<< std::endl;
                         
				}
			}

}}

// *******************    Get geometry function *************************** //
//for (int q=0; q< numberOfBins; q++)
// {
//   for (int w=0; w<numberOfBins; w++)
// {
   
//   Double_t zz_geom_histo = hgeom.GetZaxis()->GetBinCenter(q);
//   Double_t yy_geom_histo = hgeom.GetYaxis()->GetBinCenter(w);
//   Double_t edep_histo    = hgeom.GetBinContent(q,w);

//   if ((zz_geom_histo>0)&&(yy_geom_histo>0)){ //stick in the top right quadrant for now

//     radius_geom = sqrt(zz_geom_histo*zz_geom_histo+yy_geom_histo*yy_geom_histo); 

//     theta = atan(y,z)/deg;
//     theta_1 = atan(y,(z-L/2))/deg;
//     theta_2 = atan(y,(z+L/2))/deg;
//     beta = theta_2 - theta_1;

//     if (radius_geom != 0){
//              radInt_geom = TMath::Nint(4*radius_geom);
//             }
//       if (theta == 0){
//              GL = 1./(radInt_geom**2-L**2/4.);
//              }
//       else{
//              GL = beta/(L*radInt_geom*sin(theta)); 

//              if ((theta == 90)&&(radInt_geom==1.)){
//               GL_0 = GL 
//        }
//       }
//     }
    
        
//}}

ofstream myfile;
myfile.open ("Kerma.txt");
for (int j=0; j<numberOfBinsKerma; j++)
 {
  for (int l=0; l<numberOfBinsKerma; l++)
 { 
   Double_t xx_histo3 = h30.GetYaxis()->GetBinCenter(l)/10.; //put it in cm for the sk conversion
   Double_t yy_histo3 = h30.GetYaxis()->GetBinCenter(j)/10.;
   radius_k = sqrt(xx_histo3*xx_histo3+yy_histo3*yy_histo3); 
   Double_t kerma_histo3=h30.GetBinContent(l,j);
  
   if (radius_k > 2 && radius_k <= 100 && kerma_histo3!=0){ //want to measure between 2 and 100 
       //cout << radius_k << "kerma     " << kerma_histo3 << endl;
       myfile << radius_k <<  "     " << kerma_histo3 << "\n";
  }                        
 } 
}
myfile.close();

std::cout << "Energy Map Complete" << std::endl;

//Create Normalised Dose Map
std::cout << "The energy deposition at the reference point is " << EnergyMap[40] << std::endl;
Double_t tempNormValue = EnergyMap[40]/Voxels[40]; //this must be the dose in water keV/g
std::cout << "dose rate at normalisation pt" << tempNormValue << std::endl; 
//value at 1cm, 90 degrees, the normalisation point
std::cout << "Dose rate ditribution (distances in cm)" << std::endl;

ofstream myfile;

myfile.open ("geant4_dose.txt");

for (int i=0; i<=400; i++)
{
 R = double(i)/40; //distance in CM!!!
 if (Voxels[i]>0) normDose[i] = EnergyMap[i]/Voxels[i]/tempNormValue;
    else normDose[i] = 0;

 
            
 if (R>  0.05)
    {
    //cout << R << "     " << normDose[i] << endl;  
    myfile << R <<  "     " << normDose[i] << "\n";                     
    }
}

myfile.close();
}


 
