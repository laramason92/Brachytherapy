{
#include<iostream>
#include<stdlib.h>
#include<math.h>
#include <ctime>

srand ( time(NULL) );

//this code will probably need to be split. 

//First code randomly initialises HMS vectors of length n and outputs the macros. it should also output a text file detailing the harmony memory vectors

//Then run geant4 on each macro and rename the output accordingly
// mv brachytherapy.root brach

//Second code  makes a new vector called "new" and adds it as "new and pending" to the memory text file, and outputs the macro

// run geant on new vector

// mv HarmonyMemory_New.txt HarmonyMemory.txt
// mv brachytherapy.root brachytherapy_new_vector.root

//Third code evaluates the root file for the new and pending vectorm, and reads in the text file of the other HM vector doses and ranks them If the new one is better than the worst one, it kicks the worst one off and replaces it. If not, discard.

//Continue for x iterations

// **************************

// THIS IS THE CODE TO INITIATE THE HARMONY MEMORY

Int_t HMS = 5;
Int_t vec_length = 5;
Double_t DT_max = 10.0; // max dwell time - how long to set this to make sure code doesnt take forever?
Double_t secs_to_events = 1000; //to be filled in after calibration

Double_t HM[HMS][vec_length];

for (int s=0; s<HMS; s++)
 {
  for (int m=0; m<vec_length; m++)
  {
    Double_t r = (double) rand()/((double)RAND_MAX+1);//random numbers 0 to 1
    Double_t dwell_time = DT_max*r;

    HM[s][m] = dwell_time;
  }
 }

ofstream HarmonyMemory;
ofstream Macro_HM_1;
ofstream Macro_HM_2;
ofstream Macro_HM_3;
ofstream Macro_HM_4;
ofstream Macro_HM_5;

HarmonyMemory.open("HarmonyMemory.txt");
Macro_HM_1.open("Macro_HM_1.mac");
Macro_HM_2.open("Macro_HM_2.mac");
Macro_HM_3.open("Macro_HM_3.mac");
Macro_HM_4.open("Macro_HM_4.mac");
Macro_HM_5.open("Macro_HM_5.mac");

Macro_HM_1 << "/control/verbose 1" << "\n";
Macro_HM_1 << "/tracking/verbose 0" << "\n";
Macro_HM_1 << "/run/verbose 0" << "\n";
Macro_HM_1 << "/event/verbose 0" << "\n";
Macro_HM_1 << "/source/switch GammaMed" << "\n";
Macro_HM_1 << "/control/execute iridium_source_primary.mac:" << "\n";
Macro_HM_1 << "/score/create/boxMesh boxMesh_4:" << "\n";
Macro_HM_1 << "/score/mesh/boxSize 5 5 5 cm" << "\n";
Macro_HM_1 << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_1 << "/score/quantity/energyDeposit eDep" << "\n";
Macro_HM_1 << "/score/mesh/translate/xyz 0 100 0 cm" << "\n";
Macro_HM_1 << "/score/close" << "\n";
Macro_HM_1 << "/score/list" << "\n";

Macro_HM_2 << "/control/verbose 1" << "\n";
Macro_HM_2 << "/tracking/verbose 0" << "\n";
Macro_HM_2 << "/run/verbose 0" << "\n";
Macro_HM_2 << "/event/verbose 0" << "\n";
Macro_HM_2 << "/source/switch GammaMed" << "\n";
Macro_HM_2 << "/control/execute iridium_source_primary.mac:" << "\n";
Macro_HM_2 << "/score/create/boxMesh boxMesh_4:" << "\n";
Macro_HM_2 << "/score/mesh/boxSize 5 5 5 cm" << "\n";
Macro_HM_2 << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_2 << "/score/quantity/energyDeposit eDep" << "\n";
Macro_HM_2 << "/score/mesh/translate/xyz 0 100 0 cm" << "\n";
Macro_HM_2 << "/score/close" << "\n";
Macro_HM_2 << "/score/list" << "\n";

Macro_HM_3 << "/control/verbose 1" << "\n";
Macro_HM_3 << "/tracking/verbose 0" << "\n";
Macro_HM_3 << "/run/verbose 0" << "\n";
Macro_HM_3 << "/event/verbose 0" << "\n";
Macro_HM_3 << "/source/switch GammaMed" << "\n";
Macro_HM_3 << "/control/execute iridium_source_primary.mac:" << "\n";
Macro_HM_3 << "/score/create/boxMesh boxMesh_4:" << "\n";
Macro_HM_3 << "/score/mesh/boxSize 5 5 5 cm" << "\n";
Macro_HM_3 << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_3 << "/score/quantity/energyDeposit eDep" << "\n";
Macro_HM_3 << "/score/mesh/translate/xyz 0 100 0 cm" << "\n";
Macro_HM_3 << "/score/close" << "\n";
Macro_HM_3 << "/score/list" << "\n";

Macro_HM_4 << "/control/verbose 1" << "\n";
Macro_HM_4 << "/tracking/verbose 0" << "\n";
Macro_HM_4 << "/run/verbose 0" << "\n";
Macro_HM_4 << "/event/verbose 0" << "\n";
Macro_HM_4 << "/source/switch GammaMed" << "\n";
Macro_HM_4 << "/control/execute iridium_source_primary.mac:" << "\n";
Macro_HM_4 << "/score/create/boxMesh boxMesh_4:" << "\n";
Macro_HM_4 << "/score/mesh/boxSize 5 5 5 cm" << "\n";
Macro_HM_4 << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_4 << "/score/quantity/energyDeposit eDep" << "\n";
Macro_HM_4 << "/score/mesh/translate/xyz 0 100 0 cm" << "\n";
Macro_HM_4 << "/score/close" << "\n";
Macro_HM_4 << "/score/list" << "\n";

Macro_HM_5 << "/control/verbose 1" << "\n";
Macro_HM_5 << "/tracking/verbose 0" << "\n";
Macro_HM_5 << "/run/verbose 0" << "\n";
Macro_HM_5 << "/event/verbose 0" << "\n";
Macro_HM_5 << "/source/switch GammaMed" << "\n";
Macro_HM_5 << "/control/execute iridium_source_primary.mac:" << "\n";
Macro_HM_5 << "/score/create/boxMesh boxMesh_4:" << "\n";
Macro_HM_5 << "/score/mesh/boxSize 5 5 5 cm" << "\n";
Macro_HM_5 << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_5 << "/score/quantity/energyDeposit eDep" << "\n";
Macro_HM_5 << "/score/mesh/translate/xyz 0 100 0 cm" << "\n";
Macro_HM_5 << "/score/close" << "\n";
Macro_HM_5 << "/score/list" << "\n";

for (int s=0; s<HMS; s++)
 {
  for (int m=0; m<vec_length; m++)
  {
  HarmonyMemory << TMath::Nint(HM[s][m]*secs_to_events) << "  " ;
  if (s==0){
   Macro_HM_1 << "/run/beamOn " << TMath::Nint(HM[s][m]*secs_to_events) << "\n"; 
   }
  if (s==1){
   Macro_HM_2 << "/run/beamOn " << TMath::Nint(HM[s][m]*secs_to_events) << "\n"; 
   }
  if (s==2){
   Macro_HM_3 << "/run/beamOn " << TMath::Nint(HM[s][m]*secs_to_events) << "\n"; 
   }
  if (s==3){
   Macro_HM_4 << "/run/beamOn " << TMath::Nint(HM[s][m]*secs_to_events) << "\n"; 
   }
  if (s==4){
   Macro_HM_5 << "/run/beamOn " << TMath::Nint(HM[s][m]*secs_to_events) << "\n"; 
   }
  }
 HarmonyMemory << "\n";
}

Macro_HM_1 << "/score/dumpQuantityToFile boxMesh_4 eDep EnergyDeposition_GammaMed.out" << "\n";
Macro_HM_2 << "/score/dumpQuantityToFile boxMesh_4 eDep EnergyDeposition_GammaMed.out" << "\n";
Macro_HM_3 << "/score/dumpQuantityToFile boxMesh_4 eDep EnergyDeposition_GammaMed.out" << "\n";
Macro_HM_4 << "/score/dumpQuantityToFile boxMesh_4 eDep EnergyDeposition_GammaMed.out" << "\n";
Macro_HM_5 << "/score/dumpQuantityToFile boxMesh_4 eDep EnergyDeposition_GammaMed.out" << "\n";

HarmonyMemory.close();
Macro_HM_1.close();
Macro_HM_2.close();
Macro_HM_3.close();
Macro_HM_4.close();
Macro_HM_5.close();

}
