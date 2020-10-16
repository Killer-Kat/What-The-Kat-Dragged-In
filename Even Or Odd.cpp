#include <iostream>
#include <vector>

//This Program checks if the numbers in a vector are even or odd and prints it to console.
int main() {

    std::vector<int> Numbers = { 2, 4, 3, 6, 1, 9, 15, 8, -12, 125, -7, 4};
    int odd = 0, even = 0;

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