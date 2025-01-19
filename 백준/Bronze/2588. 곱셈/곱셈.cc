#include <iostream>
using namespace std;

int main(){
  int num1, num2;
  int hundred, ten, one;

  cin >> num1 >> num2;
  hundred = num2 / 100; 
  ten = num2 % 100 / 10;
  one = num2 % 100 %10;
  cout << num1 * one << "\n";
  cout << num1 * ten << "\n";
  cout << num1 * hundred << "\n";
  cout << num1 * num2;

  return 0; 
}