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
    switch (choice) {
    case 1:
        std::cout << number01 + number02;
        break;
    case 2:
        std::cout << number01 - number02;
        break;
    case 3:
        std::cout << number01 * number02;
        break;
    case 4:
        std::cout << number01 / number02;
        break;
    default:
        std::cout << "Error, invalid selection";
        break;
    }
}
