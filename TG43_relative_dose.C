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
//   //cout << "k  " << k << "xx_histo  "<< xx_histo << endl;
//   Double_t yy_histo = h20.GetYaxis()->GetBinCenter(m);
//   Double_t edep_histo=h20.GetBinContent(k, m);
//   radius = sqrt(xx_histo*xx_histo+yy_histo*yy_histo); //in mm from hist 
//
//   if (radius != 0){
//		      radInt = TMath::Nint(4*radius); //number of voxels to radius
//		      if ((radInt>0)&&(radInt<=400))
//			{
//			 EnergyMap[radInt]+= edep_histo;
//			 Voxels[radInt]+= 1; //store the number of voxels 
//				}
//			}
//}}

//std::cout << "Energy Map Complete" << std::endl;

////Create Normalised Dose Map
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

//myfile.open ("geant4_dose.txt");

//for (int i=0; i<=400; i++)
//{
// R = double(i)/40; //distance in CM!!!
// if (Voxels[i]>0) normDose[i] = EnergyMap[i]/Voxels[i]/tempNormValue;
//    else normDose[i] = 0;


            
// if (R>  0.05)
//    {
//    //cout << R << "     " << normDose[i] << endl;  
//    myfile << R <<  "     " << normDose[i] << "\n";                     
//    }
//}
//
//myfile.close();
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


//******************** DOSE RATE AND GEOMETRY FUNCTION GL ******************************// 

Double_t EnergyMap[401][91]; //2D map of total energy in "radial distance (mm)" and "angle (degrees)"
Int_t Voxels[401][91]; //the number of voxels used to provide dose to each element of the energy map 
Double_t GL[401][91];
Double_t Mass_water_voxel = 0.00025; //grams
Double_t conv = 1e3 * 1.6022e-19 * 1e3 * 10 * 3.7e10 * 1 * 2.363 * 100 * 3600;//1.6022e-16 (J/kev) *1e3 (g/kg) * 10 Ci * 3.7e10 (Bq/Ci) * 1 (decay/s)/Bq * 2.363 photons/decay *3600 (s/h) = [Gy/h] * 100 = [cGy/h]

//************ UNCERTAINTIES***********//

Double_t Unc_D_dot[401][91];
Double_t Unc_GL[401][91];
Double_t Unc_gL[401];
Double_t Unc_F[401][91];
Double_t Unc_GL_norm[401][91];

Double_t RMS_h_geom = 0.01;
Double_t U_xsec = 0.02;
Double_t U_I = 0.005;
Double_t U_geom = 0.02;

Double_t U_D_dot_factor = sqrt( RMS_h_geom*RMS_h_geom + U_xsec*U_xsec + U_I*U_I + U_geom*U_geom );
Double_t U_Lambda_factor = sqrt(U_D_dot_factor*U_D_dot_factor + U_D_dot_factor*U_D_dot_factor);
Double_t U_GL_factor = sqrt(RMS_h_geom*RMS_h_geom); //just uncertainty on the point itself
Double_t U_gL_factor = sqrt( U_D_dot_factor*U_D_dot_factor + U_D_dot_factor*U_D_dot_factor + U_GL_factor*U_GL_factor + U_GL_factor*U_GL_factor);
Double_t U_F_factor = sqrt( U_D_dot_factor*U_D_dot_factor + U_D_dot_factor*U_D_dot_factor + U_GL_factor*U_GL_factor + U_GL_factor*U_GL_factor);
Double_t U_GL_norm_factor = sqrt(2*U_D_dot_factor*U_D_dot_factor + 2*U_GL_factor*U_GL_factor);

std::cout << "Sk = " << Sk << " +/- " << U_D_dot_factor << " %" << std::endl;
std::cout << "Lambda = " << Lambda << " +/- " <<  U_Lambda_factor << " %" << std::endl;
//**************************************//


for (int i=0; i <401; i++)
 {
 for (int j=0; j<91; j++)
  {
   EnergyMap[i][j]=0.;
   Voxels[i][j]=0.;
   GL[i][j]=0.;
}}

std::cout << Voxels[200][450] <<std::endl;

for (int q=0; q< numberOfBins; q++)
 {
   for (int w=0; w<numberOfBins; w++)
 {
   
   Double_t zz_geom_histo = hgeom.GetXaxis()->GetBinCenter(q);
   Double_t yy_geom_histo = hgeom.GetYaxis()->GetBinCenter(w);
   Double_t edep_histo    = hgeom.GetBinContent(q,w);
   radius = sqrt(zz_geom_histo*zz_geom_histo + yy_geom_histo*yy_geom_histo);

   if (radius != 0){
     radZ = TMath::Nint(4*zz_geom_histo); //get into number of voxels
     radY = TMath::Nint(4*yy_geom_histo);

     radInt = TMath::Nint(4*radius);

     if ((yy_geom_histo>=0) && zz_geom_histo >= 0) //we are in the top right quadrant
        {
       if ( (radInt < 400) )
        { 
          theta = atan( yy_geom_histo/zz_geom_histo ) * 180. / Pi ;
          //theta_1 = atan( yy_geom_histo/(zz_geom_histo-L/2.) ) * 180. / Pi ;
          //theta_2 = atan( yy_geom_histo/(zz_geom_histo+L/2.) ) * 180. / Pi ;
          theta_1 = atan( (zz_geom_histo-L/2.)/yy_geom_histo ) * 180. / Pi ; //why is it this way according to the paper?
          theta_2 = atan( (zz_geom_histo+L/2.)/yy_geom_histo ) * 180. / Pi ;
          beta = theta_2 - theta_1; // 90-theta1-(90-theta2)

          thetaInt = TMath::Nint(theta);
          EnergyMap[radInt][thetaInt] += edep_histo; 
          Voxels[radInt][thetaInt] +=1;

          if (thetaInt == 0){
              GL_val = 1./ ( (radInt/40.)**2-L**2/4.);
              //std::cout << "theta is zero and GL*r^2 is   " << GL_val*radInt*radInt << "when r is   " << radInt/40. << std::endl;
              }
          else{
              GL_val = beta/ ( L*(radInt/40.)*sin(thetaInt)); 

              if ((thetaInt == 90)&&(radInt==40)){
               //std::cout <<radInt << std::endl;
               GL_0 = GL_val;
               std::cout << "New value of GL_0 is  " << GL_val << std::endl; 
                   }
               }
          GL[radInt][thetaInt] = GL_val; // this is = not += because it's not dose - it's just one value
          Unc_GL[radInt][thetaInt] = GL_val*U_GL_factor; 
        }
     }
  } } 
        
}
//std::cout << "GL filled" << std::endl;
Double_t D_r0_theta0 = (EnergyMap[40][90]/(Voxels[40][90] * Mass_water_voxel) )* conv;
std::cout << "Dose rate at norm pt   " << D_r0_theta0 << std::endl; 

Lambda = D_r0_theta0/Sk;
std::cout << "Lambda is " << Lambda << " cGy/(hU)" << std::endl;

Double_t GL_r0_theta0 = GL[40][90];
std::cout << "GL at norm pt   " << GL_r0_theta0 << std::endl; //keV / g

Double_t D_dot[401][91];
Double_t GL_norm[401][91];

Double_t F_r_theta[401][91];
Double_t gL_r[401];


for (int i=0; i<400; i++)
{
 for (int j=0; j<91; j++)
{
 if (Voxels[i][j] > 0){
  D_dot[i][j] = (EnergyMap[i][j]/(Voxels[i][j] * Mass_water_voxel) )* conv;
  Unc_D_dot[i][j] = (EnergyMap[i][j]/(Voxels[i][j] * Mass_water_voxel) )* conv *U_D_dot_factor;
  }
 else {
  D_dot[i][j] = 0;
  Unc_D_dot[i][j] = 0;
  }
 GL_norm[i][j] = i/40.*i/40.*GL[i][j] / GL_r0_theta0 ; //for plotting comparisons (Determination of the geometry function.pdf) 
 Unc_GL_norm[i][j] = (i/40.*i/40.*GL[i][j] / GL_r0_theta0)*U_GL_norm_factor;
 } 
}


for (int i=0; i<401; i++)
{
 gL_r[i] = ( D_dot[i][90]/D_dot[40][90])*( GL[40][90] / GL[i][90]);
 std::cout << i << "  " << gL_r[i] << std::endl; 
 Unc_gL[i] = ( D_dot[i][90]/D_dot[40][90])*( GL[40][90] / GL[i][90])*U_gL_factor;
 for (int j=0; j<91; j++)
 {
 F_r_theta[i][j] = ( D_dot[i][j] / D_dot[i][90] ) * ( GL[i][90] / GL[i][j] );
 Unc_F[i][j] = (( D_dot[i][j] / D_dot[i][90] ) * ( GL[i][90] / GL[i][j] )) * U_F_factor;
 }
}

ofstream myfile_dose;
ofstream myfile_GL;
ofstream myfile_gL;
ofstream myfile_F;

myfile_dose.open ("geant4_dose_with_theta.txt");
myfile_GL.open ("GL_r_theta.txt");
myfile_gL.open ("gL_r.txt");
myfile_F.open ("F_r_theta.txt");

for (int i=0; i<=400; i++)
{
 R = double(i)/40; //distance in CM!!!
 myfile_gL << R <<  "     " <<  gL_r[i] <<  "     " <<  Unc_gL[i] << "\n";                     
 for (int j=0; j<91; j++)
 { 
 if (R>  0.05)

    {
    //cout << R << "     " << normDose[i] << endl;  
    myfile_dose << R <<  "     " << j << "     " << D_dot[i][j] <<  "     " << Unc_D_dot[i][j] <<  "\n";                     
    myfile_GL << R <<  "     " << j << "     " << GL_norm[i][j] << "     " << Unc_GL_norm[i][j] <<    "\n";                     
    myfile_F << R <<  "     " << j << "     " << F_r_theta[i][j] << "     " << Unc_F[i][j] <<     "\n";                     
    }
   }
}

myfile_dose.close();
myfile_GL.close();
myfile_F.close();
myfile_gL.close();

} 
