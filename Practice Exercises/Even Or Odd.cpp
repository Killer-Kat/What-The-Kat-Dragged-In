#include <iostream>
#include <vector> // vector support
#include <cstdlib> // for random number gen
#include <ctime> // gets time

//This Program generates random numbers and then lists if they are even or odd.
int main() {
    //seeds the pseudo random number generator with the time, not the best choice but it works well enough for this use case.
    srand((unsigned)time(0));

    int odd = 0, even = 0, input = 0;

    std::cout << "How many numbers would you like to test? \n";
    std::cin >> input;
    
    //This for loop fills the vector with random numbers.
    std::vector<int> Numbers(0);
    for (int x = 0; x < input; x++) {
        Numbers.push_back((rand() % 1000) + 1);
    }

    //and this for loop prints them to console after checking if they are even or odd.
    for (int i = 0; i < Numbers.size(); i++) {
        if ((Numbers[i] % 2) != 0) {
        std::cout << Numbers[i] << " is odd \n";
        }
        else if ((Numbers[i] % 2) == 0) {
            std::cout << Numbers[i] << " is even \n";
        }
        else
        {
            std::cout << "ERROR INVALID INPUT \n";
        }
    }

}