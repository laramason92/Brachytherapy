{
#include<iostream>
#include<stdlib.h>
#include<math.h>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <ctime>

srand ( time(NULL) );

Double_t HMCR = 0.9;
Double_t PAR = 0.3;
Double_t BW = 100; //what should this be
Int_t vec_length = 11;
Double_t DT_max = 100; // max dwell time - how long to set this to make sure code doesnt take forever?
Double_t secs_to_events = 10000; //to be filled in after calibration
Int_t HMS = 5;

Double_t r1 = (double) rand()/((double)RAND_MAX+1);
Int_t r2 = TMath::Nint( (double) rand()/((double)RAND_MAX+1) * 4); // chooses 0, 1, 2, 3, or 4 to correspond to a HM candidate

ifstream HarmonyMemory;
HarmonyMemory.open("HarmonyMemory.txt");
//HarmonyMemory.open("HarmonyMemory.txt", ios::app);

std::vector<std::vector<int>>     data;

std::string line;

while (std::getline(HarmonyMemory,line)) //reads the harmony memory into a new vector
 {
  std::vector<int>   lineData;
  std::stringstream  lineStream(line);

  int value;  

  while(lineStream >> value)
 {
  lineData.push_back(value);
 }
 data.push_back(lineData);
}

Int_t plusminus = TMath::Nint( (double) rand()/((double)RAND_MAX+1)); 

std::vector<int>  new_candidate;

for (int m=0; m<vec_length; m++){ //construct a new vector
  if (r1 < HMCR){
   int new_val = data[r2][m];       
   if (r1 < PAR){

   if (plusminus ==0){
    int cand_val = TMath::Nint(new_val - (double) rand()/((double)RAND_MAX+1)*BW);
    }
   if (plusminus ==1){
    int cand_val = TMath::Nint(new_val + (double) rand()/((double)RAND_MAX+1)*BW);
    }

    } 
   else{
   int cand_val = new_val;
   }
   }
  else {
   int cand_val = (double) rand()/((double)RAND_MAX+1)*DT_max*secs_to_events;
   }
  //std::cout << cand_val << std::endl;
  new_candidate.push_back(cand_val);
}

data.push_back(new_candidate);

for (int s=0; s!=data.size(); s++){
 for (int l=0; l!=data[0].size(); l++){
 //std::cout << data[s][l] << std::endl; //reads out the randomly selected vector in the HM.
 }
}

//HarmonyMemory.close()

ofstream HarmonyMemory_New;
HarmonyMemory_New.open("HarmonyMemory_New.txt");

ofstream Macro_HM_new;
Macro_HM_new.open("Macro_HM_new.mac");

Macro_HM_new << "/control/verbose 1" << "\n";
Macro_HM_new << "/tracking/verbose 0" << "\n";
Macro_HM_new << "/run/verbose 0" << "\n";
Macro_HM_new << "/event/verbose 0" << "\n";
Macro_HM_new << "/source/switch GammaMed" << "\n";
Macro_HM_new << "/control/execute iridium_source_primary.mac" << "\n";

Macro_HM_new << "/score/create/boxMesh boxMesh_4" << "\n";
Macro_HM_new << "/score/mesh/boxSize 0.5 0.0125 0.5 cm" << "\n";
Macro_HM_new << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_new << "/score/quantity/doseDeposit doseDep" << "\n";
Macro_HM_new << "/score/mesh/translate/xyz 0 -3. 0. cm" << "\n";
Macro_HM_new << "/score/close" << "\n";

Macro_HM_new << "/score/create/boxMesh boxMesh_5" << "\n";
Macro_HM_new << "/score/mesh/boxSize 0.5 0.0125 0.5 cm" << "\n";
Macro_HM_new << "/score/mesh/nBin 1 1 1" << "\n";
Macro_HM_new << "/score/quantity/doseDeposit doseDep" << "\n";
Macro_HM_new << "/score/mesh/translate/xyz 0 2. 2. cm" << "\n";
Macro_HM_new << "/score/close" << "\n";

Macro_HM_new << "/score/list" << "\n";

for (int j=0; j<HMS+1;j++){
for (int m=1; m<vec_length+1; m++){
  HarmonyMemory_New << data[j][m] << "  " ;
  if (j==5){
   if (m==1){ //if 0 no need to move source
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 1." <<"\n";
   Macro_HM_new << "/control/execute source_HM_1.mac"  <<"\n";
   }
   if (m==2){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 2." <<"\n";
   Macro_HM_new << "/control/execute source_HM_2.mac"  <<"\n";
   }
   if (m==3){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 3." <<"\n";
   Macro_HM_new << "/control/execute source_HM_3.mac"  <<"\n";
   }
   if (m==4){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 4." <<"\n";
   Macro_HM_new << "/control/execute source_HM_4.mac"  <<"\n";
   }
   if (m==5){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 5." <<"\n";
   Macro_HM_new << "/control/execute source_HM_5.mac"  <<"\n";
   }
   if (m==6){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 6." <<"\n";
   Macro_HM_new << "/control/execute source_HM_6.mac"  <<"\n";
   }
   if (m==7){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 7." <<"\n";
   Macro_HM_new << "/control/execute source_HM_7.mac"  <<"\n";
   }
   if (m==8){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 8." <<"\n";
   Macro_HM_new << "/control/execute source_HM_8.mac"  <<"\n";
   }
   if (m==9){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 9." <<"\n";
   Macro_HM_new << "/control/execute source_HM_9.mac"  <<"\n";
   }
   if (m==10){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 10." <<"\n";
   Macro_HM_new << "/control/execute source_HM_10.mac"  <<"\n";
   }
   if (m==11){
   Macro_HM_new << "/gammamed/detector/SourceTranslationZ 11." <<"\n";
   Macro_HM_new << "/control/execute source_HM_11.mac"  <<"\n";
   }
  Macro_HM_new << "/run/beamOn " << data[5][m] << "\n";
  }
 }
 HarmonyMemory_New << "\n";
}

Macro_HM_new << "/score/dumpQuantityToFile boxMesh_5 doseDep EnergyDeposition_HM_new_ptA.out" << "\n";
Macro_HM_new << "/score/dumpQuantityToFile boxMesh_4 doseDep EnergyDeposition_HM_new_OAR.out" << "\n";
HarmonyMemory.close();
HarmonyMemory_New.close();
Macro_HM_new.close();

}
