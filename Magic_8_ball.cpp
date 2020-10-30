#include<iostream> // Magic
#include<vector> // Vector support
#include<cstdlib> //for rand function
#include<ctime> //gets time

//Made by KillerKat 10/20/2020
//I like this, I may do more with this later.
int main(){
  srand((unsigned)time(0)); // seeds our pseudo random number gen with the time
  //Store responses here
  std::vector<std::string> Wisdom = {"It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Signs point to yes.", "Reply hazy, try again.", "Concentrate and ask again.", "Cannot predict now.",  "Ask again later.", "Outlook not so good.", "Very doubtful.", "My sources say no.", "Don't count on it.", "Better not tell you now.", "Only if it compiles.", "My reply is no.", "ERROR 404 WISDOM NOT FOUND"};

int shake = std::rand() % Wisdom.size(); //This way we can add more wisdom without breaking the code.
  std::cout << "MAGIC 8-BALL: " << Wisdom[shake] << "\n";

}