//Just a simple calculator idea I had after making my first C++ program.

#include <iostream>

int main()
{
    //declare vars
    int choice = 0;
    double number01 = 0, number02 = 0;

    //Gets user Input
    std::cout << "Chose Operation: 1. Add 2. Subtract 3. Multiply 4. Devide \n";
    std::cin >> choice;
    std::cout << "Input First Number: \n";
    std::cin >> number01;
    std::cout << "Input Second Number: \n";
    std::cin >> number02;

    //Stops the user from dividing by zero
    if (choice == 4 and number02 == 0) {
        std::cout << "Nice try, you cannot devide by zero!\n";
        std::exit;
    } 
    
    //The maths
    //I know this could be written better but I dont know the langauge well enough yet.
    if (choice == 1) {
        std::cout << number01 + number02;
    }
    else if (choice == 2) {
        std::cout << number01 - number02;
    }
    else if (choice == 3) {
        std::cout << number01 * number02;
    }
    else if (choice == 4) {
        std::cout << number01 / number02;
    }
    else {
        std::cout << "Error, invalid selection";
    }

}
