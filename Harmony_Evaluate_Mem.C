{
#include<iostream>
#include<stdlib.h>
#include<math.h>

ifstream HM1_ptA;
HM1_ptA.open("EnergyDeposition_HM_1_ptA.out");
ifstream HM2_ptA;
HM2_ptA.open("EnergyDeposition_HM_2_ptA.out");
ifstream HM3_ptA;
HM3_ptA.open("EnergyDeposition_HM_3_ptA.out");
ifstream HM4_ptA;
HM4_ptA.open("EnergyDeposition_HM_4_ptA.out");
ifstream HM5_ptA;
HM5_ptA.open("EnergyDeposition_HM_5_ptA.out");
ifstream HMnew_ptA;
HMnew_ptA.open("EnergyDeposition_HM_new_ptA.out");

ifstream HM1_OAR;
HM1_OAR.open("EnergyDeposition_HM_1_OAR.out");
ifstream HM2_OAR;
HM2_OAR.open("EnergyDeposition_HM_2_OAR.out");
ifstream HM3_OAR;
HM3_OAR.open("EnergyDeposition_HM_3_OAR.out");
ifstream HM4_OAR;
HM4_OAR.open("EnergyDeposition_HM_4_OAR.out");
ifstream HM5_OAR;
HM5_OAR.open("EnergyDeposition_HM_5_OAR.out");
ifstream HMnew_OAR;
HMnew_OAR.open("EnergyDeposition_HM_new_OAR.out");

std::string line1_ptA;
while (std::getline(HM1_ptA,line1_ptA)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM1_ptA;
  std::stringstream  lineStream(line1_ptA);

  if ((line1_ptA.length() != 22)&&(line1_ptA.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM1_ptA.push_back(value);
//std::cout << line1_ptA.length() << std::endl;
 }
 }
}
double HM1_ptA_dose = lineData_double_HM1_ptA[3]*1e18;
std::cout << HM1_ptA_dose << std::endl;
//
//
std::string line1_OAR;
while (std::getline(HM1_OAR,line1_OAR)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM1_OAR;
  std::stringstream  lineStream(line1_OAR);

  if ((line1_OAR.length() != 22)&&(line1_OAR.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM1_OAR.push_back(value);
 }
 }
}
double HM1_OAR_dose = lineData_double_HM1_OAR[3]*1e18;
std::cout << HM1_OAR_dose << std::endl;
//
//
std::string line2_ptA;
while (std::getline(HM2_ptA,line2_ptA)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM2_ptA;
  std::stringstream  lineStream(line2_ptA);

  if ((line2_ptA.length() != 22)&&(line2_ptA.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM2_ptA.push_back(value);
 }
 }
}
double HM2_ptA_dose =  lineData_double_HM2_ptA[3]*1e18;
std::cout << HM2_ptA_dose << std::endl;

std::string line2_OAR;
while (std::getline(HM2_OAR,line2_OAR)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM2_OAR;
  std::stringstream  lineStream(line2_OAR);

  if ((line2_OAR.length() != 22)&&(line2_OAR.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM2_OAR.push_back(value);
 }
 }
}
double HM2_OAR_dose = lineData_double_HM2_OAR[3]*1e18;
std::cout << HM2_OAR_dose << std::endl;


std::string line3_ptA;
while (std::getline(HM3_ptA,line3_ptA)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM3_ptA;
  std::stringstream  lineStream(line3_ptA);

  if ((line3_ptA.length() != 22)&&(line3_ptA.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM3_ptA.push_back(value);
 }
 }
}
double HM3_ptA_dose =  lineData_double_HM3_ptA[3]*1e18;
std::cout << HM3_ptA_dose << std::endl;

std::string line3_OAR;
while (std::getline(HM3_OAR,line3_OAR)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM3_OAR;
  std::stringstream  lineStream(line3_OAR);

  if ((line3_OAR.length() != 22)&&(line3_OAR.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM3_OAR.push_back(value);
 }
 }
}
double HM3_OAR_dose =  lineData_double_HM3_OAR[3]*1e18;
std::cout << HM3_OAR_dose << std::endl;

std::string line4_ptA;
while (std::getline(HM4_ptA,line4_ptA)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM4_ptA;
  std::stringstream  lineStream(line4_ptA);

  if ((line4_ptA.length() != 22)&&(line4_ptA.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM4_ptA.push_back(value);
 }
 }
}
double HM4_ptA_dose =  lineData_double_HM4_ptA[3]*1e18;
std::cout << HM4_ptA_dose << std::endl;

std::string line4_OAR;
while (std::getline(HM4_OAR,line4_OAR)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM4_OAR;
  std::stringstream  lineStream(line4_OAR);

  if ((line4_OAR.length() != 22)&&(line4_OAR.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM4_OAR.push_back(value);
 }
 }
}
double HM4_OAR_dose =  lineData_double_HM4_OAR[3]*1e18;
std::cout << HM4_OAR_dose << std::endl;


std::string line5_ptA;
while (std::getline(HM5_ptA,line5_ptA)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM5_ptA;
  std::stringstream  lineStream(line5_ptA);
  if ((line5_ptA.length() != 22)&&(line5_ptA.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM5_ptA.push_back(value);
 }
 }
}
double HM5_ptA_dose =  lineData_double_HM5_ptA[3]*1e18;
std::cout << HM5_ptA_dose << std::endl;

std::string line5_OAR;
while (std::getline(HM5_OAR,line5_OAR)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HM5_OAR;
  std::stringstream  lineStream(line5_OAR);

  if ((line5_OAR.length() != 22)&&(line5_OAR.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HM5_OAR.push_back(value);
 }
 }
}
double HM5_OAR_dose = lineData_double_HM5_OAR[3]*1e18;
std::cout << HM5_OAR_dose << std::endl;

std::string linenew_ptA;
while (std::getline(HMnew_ptA,linenew_ptA)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HMnew_ptA;
  std::stringstream  lineStream(linenew_ptA);

  if ((linenew_ptA.length() != 22)&&(linenew_ptA.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HMnew_ptA.push_back(value);
 }
 }
}
double HMnew_ptA_dose =  lineData_double_HMnew_ptA[3]*1e18;
std::cout << HMnew_ptA_dose << std::endl;

std::string linenew_OAR;
while (std::getline(HMnew_OAR,linenew_OAR)) //reads the harmony memory into a new vector
 {
  std::vector<double>   lineData_double_HMnew_OAR;
  std::stringstream  lineStream(linenew_OAR);

 if ((linenew_OAR.length() != 22)&&(linenew_OAR.length() != 32))
  {
  double value;
  while(lineStream >> value)
 {
  lineData_double_HMnew_OAR.push_back(value);
 }
 }
}
double HMnew_OAR_dose =  lineData_double_HMnew_OAR[3]*1e18;
std::cout << HMnew_OAR_dose << std::endl;
//// NEXT: INPUT THESE DOSES INTO THE OBJECTIVE FUNCTION

double w_min_cx = 2.;
double w_max_cx = 2.;
double w_max_oar = 2.;

double D_min_Cx = 50.;
double D_max_Cx = 150.;
double D_max_OAR = 70.;

double OF_1 = w_min_cx*(D_min_Cx - HM1_ptA_dose) + w_max_cx*(HM1_ptA_dose - D_max_Cx) + w_max_oar*(HM1_OAR_dose - D_max_OAR);
double OF_2 = w_min_cx*(D_min_Cx - HM2_ptA_dose) + w_max_cx*(HM2_ptA_dose - D_max_Cx) + w_max_oar*(HM2_OAR_dose - D_max_OAR);
double OF_3 = w_min_cx*(D_min_Cx - HM3_ptA_dose) + w_max_cx*(HM3_ptA_dose - D_max_Cx) + w_max_oar*(HM3_OAR_dose - D_max_OAR);
double OF_4 = w_min_cx*(D_min_Cx - HM4_ptA_dose) + w_max_cx*(HM4_ptA_dose - D_max_Cx) + w_max_oar*(HM4_OAR_dose - D_max_OAR);
double OF_5 = w_min_cx*(D_min_Cx - HM5_ptA_dose) + w_max_cx*(HM5_ptA_dose - D_max_Cx) + w_max_oar*(HM5_OAR_dose - D_max_OAR);
double OF_new = w_min_cx*(D_min_Cx - HMnew_ptA_dose) + w_max_cx*(HMnew_ptA_dose - D_max_Cx) + w_max_oar*(HMnew_OAR_dose - D_max_OAR);


//std::cout<< "*********** THE OBJECTIVE FUNCTIONS ARE ******************"
std::cout << "HM_1 = " << OF_1 << std::endl;
std::cout << "HM_2 = " << OF_2 << std::endl;
std::cout << "HM_3 = " << OF_3 << std::endl;
std::cout << "HM_4 = " << OF_4 << std::endl;
std::cout << "HM_5 = " << OF_5 << std::endl;
std::cout << "HM_new = " << OF_new << std::endl;

}
