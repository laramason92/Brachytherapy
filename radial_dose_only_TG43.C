{
// Create output file geant4_dose.txt with the dose rate distribution, calculated
// with the simulation results containted in brachytherapy.root

//#include <math.h>

gROOT -> Reset();
//TFile f("brachytherapy.root");
TFile f("brachytherapy210601.root");

//******************** DEFINITIONS ******************************// 					     
Double_t L = 0.35; //seed length in cm
Double_t normDose[401]; //Energy map divided by voxels used to make cell, normalised to energy deposition at 1cm, 90 degrees
Double_t normDoseKERMA[1001]; //Energy map divided by voxels used to make cell, normalised to energy deposition at 1cm, 90 degrees

Double_t R;     //radial distance in cm
Double_t RKERMA;     //radial distance in cm

Double_t radius; //radius (mm)
Double_t radiusKERMA; //radius (cm)

Double_t theta;
Double_t theta_1;
Double_t theta_2;
Double_t beta;  //beta angle for Geometry Function calculation

Double_t Pi = 3.14159265;

Double_t GL_val;
Double_t GL_0=1;


Int_t thetaInt;
Int_t radInt; //nearest integer of radius (mm)
Int_t radZ;
Int_t radY;

Int_t radIntKERMA; //nearest integer of radius (mm)

Int_t numberOfBins=801;
Int_t numberOfBinsKERMA=8001;

Double_t Sk = 36519.0; // [U] from Lopez Donaire and Alcalde
Double_t Lambda;

std::cout << "Have you edited the uncertainty params correctly?" << std::endl;
//******************** GET RADIAL DOSE RATE ALONE ******************************// 

Double_t EnergyMap[401]; //2D map of total energy in "radial distance (mm)" and "angle (5 degrees)"
Int_t Voxels[401]; //the number of voxels used to provide dose to each element of the energy map

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
   radius = sqrt(xx_histo*xx_histo+yy_histo*yy_histo); //in mm from hist 

   if (radius != 0){
		      radInt = TMath::Nint(4*radius); //number of voxels to radius
		      if ((radInt>0)&&(radInt<=400))
			{
			 EnergyMap[radInt]+= edep_histo;
			 Voxels[radInt]+= 1; //store the number of voxels 
				}
			}
}}

std::cout << "Energy Map Complete" << std::endl;

//Create Normalised Dose Map
std::cout << "The energy deposition at the reference point is " << EnergyMap[40] << std::endl;
Double_t tempNormValue = EnergyMap[40]/Voxels[40]; //this must be the dose in water keV/g
std::cout << "dose rate at normalisation pt" << tempNormValue << std::endl; 
Double_t EnergyDepNorm = EnergyMap[40] * 1e3 * 1.6022e-19 * 1e3 * 10 * 3.7e10 * 1 * 2.363 * 100 * 3600;
Double_t MassNorm = Voxels[40] * 0.00025 ;
Double_t DoseRateNorm = EnergyDepNorm/MassNorm;
std::cout << "dose rate at normalisation pt in correct units" << DoseRateNorm << std::endl; 
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
//


//******************** GET KERMA ALONE ******************************// 

//Double_t EnergyMap[401]; //2D map of total energy in "radial distance (mm)" and "angle (5 degrees)"
//Int_t Voxels[401]; //the number of voxels used to provide dose to each element of the energy map

//for (int i=0; i <401; i++)
// {
// EnergyMap[i]=0.;
// Voxels[i]=0.;
//}

////Build Energy Deposition Map
//for (int k=0; k< numberOfBins; k++)
// {
//   for (int m=0; m< numberOfBins; m++) 
// {
//   Double_t xx_histo = h20.GetXaxis()->GetBinCenter(k);
//   cout << "k  " << k << "xx_histo  "<< xx_histo << endl;
//   Double_t yy_histo = h20.GetYaxis()->GetBinCenter(m);
//   Double_t edep_histo=h20.GetBinContent(k, m);
//   radius = sqrt(xx_histo*xx_histo+yy_histo*yy_histo); 

//   if (radius != 0){
//		      radInt = TMath::Nint(4*radius);
//		      if ((radInt>0)&&(radInt<=400))
//			{
//			 EnergyMap[radInt]+= edep_histo;
//			 Voxels[radInt]+= 1; //store the number of voxels 
//				}
//			}
//}}
//
//std::cout << "Energy Map Complete" << std::endl;

//Create Normalised Dose Map
//std::cout << "The energy deposition at the reference point is " << EnergyMap[40] << std::endl;
//Double_t tempNormValue = EnergyMap[40]/Voxels[40]; //this must be the dose in water keV/g
//std::cout << "dose rate at normalisation pt" << tempNormValue << std::endl; 
//Double_t EnergyDepNorm = EnergyMap[40] * 1.60218e-16 * 10 * 3.7e10 * 2.363 * 100 * 3600;
//Double_t MassNorm = Voxels[40] * 0.001 *1000 ;
//Double_t DoseRateNorm = EnergyDepNorm/MassNorm;
//std::cout << "dose rate at normalisation pt in correct units" << DoseRateNorm << std::endl; 
////value at 1cm, 90 degrees, the normalisation point
//std::cout << "Dose rate ditribution (distances in cm)" << std::endl;

//ofstream myfile;

//myfile.open ("Kerma.txt");
//
//for (int i=0; i<=400; i++)
//{
// R = double(i)/40; //distance in CM!!!
// if (Voxels[i]>0) normDose[i] = EnergyMap[i]/Voxels[i];///tempNormValue;
 //   else normDose[i] = 0;
//

            
// if (R>  0.05)
// if (R>  2)
//    {
//    //cout << R << "     " << normDose[i] << endl;  
//    myfile << R <<  "     " << normDose[i] << "\n";                     
//    }
//}

//myfile.close();


} 
