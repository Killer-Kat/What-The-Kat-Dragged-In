#include <iostream>
#include <cstdlib> // for random number gen
#include <ctime> // gets time
#include <windows.h> //Needed for clearing console window\

void clear() {
    COORD topLeft = { 0, 0 };
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO screen;
    DWORD written;

    GetConsoleScreenBufferInfo(console, &screen);
    FillConsoleOutputCharacterA(
        console, ' ', screen.dwSize.X * screen.dwSize.Y, topLeft, &written
    );
    FillConsoleOutputAttribute(
        console, FOREGROUND_GREEN | FOREGROUND_RED | FOREGROUND_BLUE,
        screen.dwSize.X * screen.dwSize.Y, topLeft, &written
    );
    SetConsoleCursorPosition(console, topLeft);
}
class CPUData { //Creates a class so we can store the varibles we need in an object that can be passed when needed.
public:
    int CPUChoice;
    std::string CPUChoiceMessage;
    bool debugMessageToggle;

    void RandomOpponent() {

        //Random mode
        CPUChoice = (rand() % 3);
        if (debugMessageToggle) {
            std::cout << "DEBUG: CPU CHOICE (Random) IS " << CPUChoice << "\n";
        }
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
    void RockLoverOpponent() {
        //Rock mode
        CPUChoice = (rand() % 3);
        if (debugMessageToggle) {
            std::cout << "DEBUG: CPU (Rocky) CHOICE IS " << CPUChoice << "\n";
        }
        switch (CPUChoice) {
        case 0:
            CPUChoiceMessage = "CPU Chose Rock";
            break;
        case 1:
            CPUChoice = (rand() % 3);
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
            break;
        case 2:
            CPUChoiceMessage = "CPU Chose Scissors";
            break;
        default:
            CPUChoiceMessage = "CPU Had an Invalid Choice\n";
        }
    };
};
bool PlayGame(CPUData Opponent) {

    //Win State 
    int PlayerChoice = 3; //3 is null 0 is Rock 1 is Paper and 2 is Scissors
    std::cout << "Make Your Move!\n";
    std::cin >> PlayerChoice;
    switch (PlayerChoice) {
    case 0:
        std::cout << "You Chose Rock and " << Opponent.CPUChoiceMessage << "\n";
        if (Opponent.CPUChoice == 0) {
            std::cout << "The game ends in a tie!\n";
            return false;
        }
        else if (Opponent.CPUChoice == 2) {
            std::cout << "You win!\n";
            return true;
        }
        else {
            std::cout << "CPU wins!\n";
            return false;
        }
        break;
    case 1:
        std::cout << "You Chose Paper and " << Opponent.CPUChoiceMessage << "\n";
        if (Opponent.CPUChoice == 1) {
            std::cout << "The game ends in a tie!\n";
            return false;
        }
        else if (Opponent.CPUChoice == 0) {
            std::cout << "You win!\n";
            return true;
        }
        else {
            std::cout << "CPU wins!\n";
            return false;
        }
        break;
    case 2:
        std::cout << "You Chose Scissors and " << Opponent.CPUChoiceMessage << "\n";
        if (Opponent.CPUChoice == 2) {
            std::cout << "The game ends in a tie!\n";
            return false;
        }
        else if (Opponent.CPUChoice == 1) {
            std::cout << "You win!\n";
            return true;
        }
        else {
            std::cout << "CPU wins!\n";
            return false;
        }
        break;
    default:
        std::cout << "Invalid Choice\n";
        return false;
    }
}
     void main()
    {
        //seeds the pseudo random number generator with the time, not the best choice but it works well enough for this use case.
        srand((unsigned)time(0));

        static int gameScore;
        static int gameMode;
        static bool debugMessage;
        int optionsMenu; // used for the options menu switch
        CPUData CPUPlayer; //Obj we use to hold the data for the CPU player for easy use between functions
        CPUPlayer.debugMessageToggle = debugMessage;

        std::cout << "Wellcome to Rock Paper Scissors C++ Edition!\n";
        std::cout << "This app made by Killerkat on 9/22/2021 find me on Github or Checkout my blog!\n";
        std::cout << "0 for Rock 1 for Paper and 2 for Scissors\n";
        
        
        switch (gameMode) { //Game mode selector
        case 0:
            CPUPlayer.RandomOpponent();
            std::cout << "Current Mode Random\n";
            break;
        case 1:
            CPUPlayer.RockLoverOpponent();
            std::cout << "Current Mode Rock Lover\n";
            break;
        default:
            break;
        }

        if (gameScore > 0) { //Simple way to track game wins
            std::cout << "You have won " << gameScore << " times!\n";
        }
        //add notes later
        if (PlayGame(CPUPlayer)) {
            gameScore++;
        }
        int pasta; //because its spaghetti code.
        std::cout << "Play again? 1 = Yes 0 = No (Close Game) 2 = Open options menu\n";
        std::cin >> pasta;
        switch (pasta){
        case 0 :
            break;
        case 1 :
            clear();
            main();
            break;
        case 2:
            clear();
            std::cout << "OPTIONS MENU: Select an option\n 0 : Set opponent to Random mode.\n 1 : Set opponent to Rock Lover mode.\n 2 : Toggle Debug Mode.\n";
            std::cin >> optionsMenu;
            switch (optionsMenu) {
            case 0:
                gameMode = 0;
                break;
            case 1:
                gameMode = 1;
                break;
            case 2 :
                debugMessage = !debugMessage;
                if (debugMessage) {
                    std::cout << "Debug mode is on.\n";
                }
                else {
                    std::cout << "Debug mode is off.\n";
                }

                break;
            default :
                break;
            }
            clear();
            main();
            break;
        default:
            clear();
            main();
            break;
        }
        
    }
    