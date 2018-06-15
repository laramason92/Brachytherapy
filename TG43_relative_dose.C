{
// Create output file geant4_dose.txt with the dose rate distribution, calculated
// with the simulation results containted in brachytherapy.root

//#include <math.h>

gROOT -> Reset();
//TFile f("brachytherapy.root");
TFile f("brachytherapy_280mil_xymesh.root");

//******************** DEFINITIONS ******************************// 					     
Double_t L = 0.35; //seed length in cm
Int_t len_KermaMap=4001;
Double_t KermaMap[len_KermaMap];
Double_t Y_cm[len_KermaMap];
Double_t normDose[401]; //Energy map divided by voxels used to make cell, normalised to energy deposition at 1cm, 90 degrees
Double_t GeomFunction[401]; //Geometry Function, normalised to the geometry function at the reference point
Double_t GeometryFunctionZero;  //Geometry function at reference point, 1cm and 90 degrees
Double_t beta;  //beta angle for Geometry Function calculation
Double_t R;     //radial distance in cm
Double_t K;     //polar angle in radians
Double_t Radial[401]; //radial dose function
Double_t radius; //radius (mm)
Double_t radius_k; //radius (cm)
Int_t radius_k_rounded; //radius (cm)
Double_t radius_geom;
Double_t theta;
Double_t theta_1;
Double_t theta_2;
Double_t GL_val;
Double_t GL_0=1;
Int_t count_i;
Double_t Ci=10.0;

Int_t radInt; //nearest integer of radius (mm)
Int_t numberOfBins=801;
Int_t numberOfBinsKerma=2001;
Double_t Sk; // = ?? todo!
Double_t D_dot_0; // = ?? todo!

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
   radius = sqrt(xx_histo*xx_histo+yy_histo*yy_histo); 

   if (radius != 0){
		      radInt = TMath::Nint(4*radius);
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
Double_t EnergyDepNorm = EnergyMap[40] * 1.60218e-16 * 10 * 3.7e10 * 2.363 * 100 * 3600;
Double_t MassNorm = Voxels[40] * 0.001 *1000 ;
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
}




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
   Double_t xx_histo = h30.GetXaxis()->GetBinCenter(k);
   //cout << "k  " << k << "xx_histo  "<< xx_histo << endl;
   Double_t yy_histo = h30.GetYaxis()->GetBinCenter(m);
   Double_t edep_histo=h30.GetBinContent(k, m);
   radius = sqrt(xx_histo*xx_histo+yy_histo*yy_histo); 

   if (radius != 0){
		      radInt = TMath::Nint(4*radius);
		      if ((radInt>0)&&(radInt<=400))
			{
			 EnergyMap[radInt]+= edep_histo;
			 Voxels[radInt]+= 1; //Number of times around the cylindrical symmetry that the same r was used? 
				}
			}
}}

std::cout << "Energy Map Complete" << std::endl;

//Create Normalised Dose Map
std::cout << "The energy deposition at the reference point is " << EnergyMap[40] << std::endl;

Double_t tempNormValue = EnergyMap[40]/Voxels[40]; //this must be the dose in water keV/g
std::cout << "dose rate at normalisation pt" << tempNormValue << std::endl; 

Double_t EnergyDepNorm = EnergyMap[40] * 1.60218e-16 * 10 * 3.7e10 * 2.363 * 3600; //J/kg/h = Gy/h
Double_t MassNorm = Voxels[40] ; // density dry air is 0.0012928 g/cm^3
Double_t DoseRateNorm = EnergyDepNorm/MassNorm;
std::cout << "dose rate at normalisation pt in correct units" << DoseRateNorm << std::endl; 
//value at 1cm, 90 degrees, the normalisation point
std::cout << "Dose rate ditribution (distances in cm)" << std::endl;

ofstream myfile;

myfile.open ("geant4_dose.txt");

for (int i=0; i<=400; i++)
{
 R = double(i)/40; //distance in CM!!!
 if (Voxels[i]>0) normDose[i] = (EnergyMap[i]*1.60218e-16 * 10 * 3.7e10 * 2.363 * 3600 * 100) /  (Voxels[i]);// 100* J/Kg/h == 100* Gy/h = cGy/h
    else normDose[i] = 0;

 
            
 if (R>  0.05)
    {
    //cout << R << "     " << normDose[i] << endl;  
    myfile << R <<  "     " << normDose[i] << "\n";                     
    }
}

myfile.close();
}












//********************!!!!!!!! WRONG !!!!!!!!!!!!! AIR KERMA RATE ******************************// 

//for (int i=0; i<4001; i++)
// {
// KermaMap[i]=0.;
// Y_cm[i]=0.;
//}

//for (int j=0; j<numberOfBinsKerma; j++)
// {
//  for (int l=0; l<numberOfBinsKerma; l++)
// { 
//   Double_t xx_histo3 = h20.GetXaxis()->GetBinCenter(l); //put it in cm for the sk conversion
//   Double_t yy_histo3 = h20.GetYaxis()->GetBinCenter(j);
//   Double_t kerma_histo3 = h20.GetBinContent(l,j);
//   radius_k = sqrt(xx_histo3*xx_histo3+yy_histo3*yy_histo3);//mm 

//   if (radius_k !=0){ //want to measure between 2 and 100 
//     radius_k_rounded = TMath::Nint(4*radius_k); //mm
//     if ((radius_k_rounded>0)&&(radius_k_rounded<=4000))
//       { 
//       Double_t kerma_histo_rate = kerma_histo3 ;//* 1.60218e-13 * 1000 * Ci * 3.7e10 * 1 *2.363 * 60*60 * 100; //cGy/h
//
//       //std::cout << "   radius   " << radius_k_rounded << "   y   " << y_kerma_cm << "  kerma     " << kerma_histo3 << std::endl;
//       KermaMap[radius_k_rounded] += kerma_histo_rate; //mm
//       //myfile << radius_k <<  "     " << kerma_histo3 << "\n";
//  }
//  }                        
// } 
//}
//



//ofstream myfile;
//myfile.open ("Kerma.txt");
//for (int t=0; t<4001; t+=10)
// {
// if (KermaMap[t]>0){
//    myfile << t <<   "     " << KermaMap[t] << "\n";
//  }
// }
//myfile.close();

//std::cout << "Kerma Map Complete" << std::endl;














//******************** DOSE RATE AND GEOMETRY FUNCTION GL ******************************// 

//Double_t EnergyMap[401][401]; //2D map of total energy in "radial distance (mm)" and "angle (5 degrees)"
//Int_t Voxels[401][401]; //the number of voxels used to provide dose to each element of the energy map
//Double_t GL[401][401];

//for (int i=0; i <401; i++)
// {
// for (int j=0; j<401; j++)
//  {
//   EnergyMap[i][j]=0.;
//   Voxels[i][j]=0.;
//}}


//for (int q=0; q< numberOfBins; q++)
// {
//   for (int w=0; w<numberOfBins; w++)
// {
   
//   Double_t zz_geom_histo = hgeom.GetXaxis()->GetBinCenter(q);
//   Double_t yy_geom_histo = hgeom.GetYaxis()->GetBinCenter(w);
//   Double_t edep_histo    = hgeom.GetBinContent(q,w);
//   radius = sqrt(zz_geom_histo*zz_geom_histo + yy_geom_histo*yy_geom_histo);

//   if (radius != 0){
//     radZ = TMath::Nint(4*zz_geom_histo);
//     radY = TMath::Nint(4*yy_geom_histo);

//     radInt = TMath::Nint(4*radius);
//     if ( (radZ>0)&&(radZ<=400) && (radY>0)&&(radY<=400) )
//          {
//          EnergyMap[radZ][radY] += edep_histo; //this will be to calculate the dose
//          Voxels[radZ][radY] +=1
//          }
      
//          theta = atan(yy_geom_histo,zz_geom_histo)/deg;
//          theta_1 = atan(y,(z-L/2))/deg;
//          theta_2 = atan(y,(z+L/2))/deg;
//          beta = theta_2 - theta_1;

//          if (theta == 0){
//              GL_val = 1./(radInt_geom**2-L**2/4.);
//              }
//          else{
//              GL_val = beta/(L*radInt_geom*sin(theta)); 

//              if ((theta == 90)&&(radInt_geom==40)){
//               GL_0 = GL_val //I dont think this is going to work - will have to get from the lookup table
//               std::cout << "New value of GL_0 << std::endl; 
//          GL[radZ][radY] = GL_val
//        }
//       }
//     }
    
        
//}}

 
