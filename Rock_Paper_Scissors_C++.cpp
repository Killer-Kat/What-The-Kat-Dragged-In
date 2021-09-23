#include <iostream>
#include <cstdlib> // for random number gen
#include <ctime> // gets time

class CPUData {
public:
    int CPUChoice;
    std::string CPUChoiceMessage;

    void RandomOpponent() {

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

    };
};
void PlayGame(CPUData Opponent) {

    //Win State 
    int PlayerChoice = 3; //3 is null 0 is Rock 1 is Paper and 2 is Scissors
    std::cout << "Make Your Move!\n";
    std::cin >> PlayerChoice;
    switch (PlayerChoice) {
    case 0:
        std::cout << "You Chose Rock and " << Opponent.CPUChoiceMessage << "\n";
        if (Opponent.CPUChoice == 0) {
            std::cout << "The game ends in a tie!\n";
        }
        else if (Opponent.CPUChoice == 2) {
            std::cout << "You win!\n";
        }
        else {
            std::cout << "CPU wins!\n";
        }
        break;
    case 1:
        std::cout << "You Chose Paper and " << Opponent.CPUChoiceMessage << "\n";
        if (Opponent.CPUChoice == 1) {
            std::cout << "The game ends in a tie!\n";
        }
        else if (Opponent.CPUChoice == 0) {
            std::cout << "You win!\n";
        }
        else {
            std::cout << "CPU wins!\n";
        }
        break;
    case 2:
        std::cout << "You Chose Scissors and " << Opponent.CPUChoiceMessage << "\n";
        if (Opponent.CPUChoice == 2) {
            std::cout << "The game ends in a tie!\n";
        }
        else if (Opponent.CPUChoice == 1) {
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
     void main()
    {
        //seeds the pseudo random number generator with the time, not the best choice but it works well enough for this use case.
        srand((unsigned)time(0));

        
        //int CPUChoice = 3; //The Computers Move. 

        CPUData CPUPlayer;
        
        std::cout << "Wellcome to Rock Paper Scissors C++ Edition!\n";
        std::cout << "This app made by Killerkat on 9/22/2021\n";
        std::cout << "0 for Rock 1 for Paper and 2 for Scissors\n";
        std::cout << "Current Mode Random\n";

        //random
        CPUPlayer.RandomOpponent();     
        //add notes later
        PlayGame(CPUPlayer);
        //std::cout << "Play again? 1 = Yes 0 = No\n";

    }
    