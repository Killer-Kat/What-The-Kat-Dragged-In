#include <iostream>

//Written by KillerKat 10/30/2020
int main() {

  double pesos, reais, soles, dollars;
  /* 
1 Colombian Peso equals
0.00026 United States Dollar
1 Brazilian Real equals
0.17 United States Dollar
1 Sol equals
0.28 United States Dollar */
double peso_rate = 0.00026, reais_rate = 0.17, soles_rate = 0.28;

std::cout << "Enter number of Colombian Pesos: ";
std::cin >> pesos;
dollars = pesos * peso_rate;
std::cout << "Thats $" << dollars << " USD \n";
std::cout << "Enter number of Brazilian Reais: ";
std::cin >> reais;
dollars = (reais * reais_rate) + dollars;
std::cout << "Thats $" << (reais * reais_rate) << " USD \n";
std::cout << "Enter number of Peruvian Soles: ";
std::cin >> soles;
dollars = (soles_rate * soles) + dollars;
std::cout << "Thats $" << (soles_rate * soles) << " USD \n";
std::cout << "You have a total of $" << dollars << " USD \n";
}