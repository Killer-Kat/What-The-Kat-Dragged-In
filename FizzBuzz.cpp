#include<iostream>
//I'll be honest I remember watching tom scott's video on this so I feel a little like thats cheating since I am not going in blind but reguardless here is my take on the question.
int main(){

for (int i = 1; i <= 100; i++){
  if(i % 3 == 0 && i % 5 == 0){
    std::cout << "FizzBuzz! \n";
  } else if (i % 5 == 0){
    std::cout << "Buzz \n";
  } else if (i % 3 == 0){
    std::cout << "Fizz \n";
  } else {
    std::cout << i << "\n";
  }

}
}