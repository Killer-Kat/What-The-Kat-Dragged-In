#include <iostream>
#include <cstdlib> // for random number gen
#include <ctime> // gets time

int main()
{
    //seeds the pseudo random number generator with the time, not the best choice but it works well enough for this use case.
    srand((unsigned)time(0));

    int PlayerChoice = 3; //3 is null 0 is Rock 1 is Paper and 2 is Scissors
    int CPUChoice = 3; //The Computers Move.
    std::string CPUChoiceMessage;
    std::cout << "Wellcome to Rock Paper Scissors C++ Edition!\n";
    std::cout << "This app made by Killerkat on 9/22/2021\n";
    std::cout << "0 for Rock 1 for Paper and 2 for Scissors\n";
    std::cout << "Current Mode Random\n";

    //Random mode
    CPUChoice = (rand() % 3);
    std::cout << "DEBUG: CPU CHOICE IS " << CPUChoice << "\n";
    switch (CPUChoice) {
    case 0:
        CPUChoiceMessage = "CPU Chose Rock";
        break;
    case 1:
        CPUChoiceMessage = "CPU Chose Paper";
        break;
    case 2:
        CPUChoiceMessage = "CPU Chose Scissors";
        break;
    default:
        CPUChoiceMessage = "CPU Had an Invalid Choice\n";
    }
    
    //Name this part later
    std::cout << "Make Your Move!\n";
    std::cin >> PlayerChoice;
    switch (PlayerChoice) {
    case 0:
        std::cout << "You Chose Rock and " << CPUChoiceMessage << "\n";
        if (CPUChoice == 0) {
            std::cout << "The game ends in a tie!\n";
        }
        else if (CPUChoice == 2) {
            std::cout << "You win!\n";
        }
        else {
            std::cout << "CPU wins!\n";
        }
        break;
    case 1:
        std::cout << "You Chose Paper and " << CPUChoiceMessage << "\n";
        if (CPUChoice == 1) {
            std::cout << "The game ends in a tie!\n";
        }
        else if (CPUChoice == 0) {
            std::cout << "You win!\n";
        }
        else {
            std::cout << "CPU wins!\n";
        }
        break;
    case 2:
        std::cout << "You Chose Scissors and " << CPUChoiceMessage << "\n";
        if (CPUChoice == 2) {
            std::cout << "The game ends in a tie!\n";
        }
        else if (CPUChoice == 1) {
            std::cout << "You win!\n";
        }
        else {
            std::cout << "CPU wins!\n";
        }
        break;
    default:
        std::cout << "Invalid Choice\n";
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
