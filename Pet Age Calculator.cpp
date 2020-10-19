//After doing the dog years project on codecademy I knew I had to make this.
#include <iostream>

int main()
{
    int human_years, pet_age, pet_type;
    //std::cout << "Please enter the pets name: \n";
    std::cout << "Pet age calculator, please select pet type: \n 1. Dog 2. Cat 3. PLACEHOLDER :";
    std::cin >> pet_type;
    std::cout << "Please input pets age in whole years :\n";
    std::cin >> pet_age;

    //Gets pet type and does maths/output for that pet type
    switch (pet_type) {
    case 1:
        if (pet_age >= 2) {
            human_years = ((pet_age - 2) * 4) + 21;
            std::cout << "Your dog is " << human_years << " human years old! \n";
        }
        else if (pet_age == 1) {
            std::cout << "Your dog is 7 human years old! \n";
        }
        else {
            std::cout << "Error invalid age, please enter the age in whole years.";
        }
        
        break;
    case 2:
        if (pet_age >= 2) {
            human_years = ((pet_age - 2) * 4) + 24; //For calculating the cats age I went by the AAFP-AAHA Feline Life Stage Guidelines. https://www.aaha.org/globalassets/02-guidelines/feline-life-stage/felinelifestageguidelines.pdf
            std::cout << "Your cat is " << human_years << " human years old! \n";
        }
        else if (pet_age == 1) {
            std::cout << "Your cat is 15 human years old! \n";
        }
        else {
            std::cout << "Error invalid age, please enter the age in whole years.";
        }
        break;
    case 3:
        std::cout << "Placeholder";
        break;
    case 1337:
        std::cout << "Your Killer_Kat is " << pet_age << " years old in human years, wait hold on thats me! \n";
        break;
    default:
        std::cout << "Error, invalid selection.";
    }
}

