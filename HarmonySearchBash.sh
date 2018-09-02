#!/bin/bash

echo "hello world"

root Harmony_Memory_Construction.C
echo "**********************************"
echo "memory constructed"
echo "**********************************"
root Harmony_New_Vector.C
echo "**********************************"
echo "new vector constructed"
echo "Now run Geant"
echo "**********************************"

source /Users/laramason/Downloads/Geant4/geant4.10.03.p03-install/bin/geant4.sh
source /Users/laramason//Downloads/ROOT/root-build/bin/thisroot.sh
export G4ENSDFSTATEDATA=/Users/laramason/Downloads/Geant4/geant4.10.03.p03-install/share/Geant4-10.3.3/data/G4ENSDFSTATE2.1;export G4LEDATA=/Users/laramason/Downloads/Geant4/geant4.10.03.p03-install/share/Geant4-10.3.3/data/G4EMLOW6.50/;export G4LEVELGAMMADATA=/Users/laramason/Downloads/Geant4/geant4.10.03.p03-install/share/Geant4-10.3.3/data/PhotonEvaporation4.3.2/;export G4SAIDXSDATA=/Users/laramason/Downloads/Geant4/geant4.10.03.p03-install/share/Geant4-10.3.3/data/G4SAIDDATA1.1;export G4NEUTRONXSDATA=/Users/laramason/Downloads/Geant4/geant4.10.03.p03-install/share/Geant4-10.3.3/data/G4NEUTRONXS1.4
/Users/laramason/Downloads/Geant4/build-brachy-proj/Brachy Macro_HM_1.mac

#mv EnergyDeposition_GammaMed.out EnergyDeposition_HM_1.out
 
/Users/laramason/Downloads/Geant4/build-brachy-proj/Brachy Macro_HM_2.mac 
/Users/laramason/Downloads/Geant4/build-brachy-proj/Brachy Macro_HM_3.mac 
/Users/laramason/Downloads/Geant4/build-brachy-proj/Brachy Macro_HM_4.mac 
/Users/laramason/Downloads/Geant4/build-brachy-proj/Brachy Macro_HM_5.mac 
/Users/laramason/Downloads/Geant4/build-brachy-proj/Brachy Macro_HM_new.mac 

#mv EnergyDeposition_GammaMed.out EnergyDeposition_HM_2.out
