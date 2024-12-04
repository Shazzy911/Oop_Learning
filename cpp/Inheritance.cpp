#include <iostream>
using namespace std;

class Account{
    public:
    int accountNumber;
    string accountHolderName;
    double balance;
    
    
    Account(int x, string y, double z):accountNumber(x),accountHolderName(y), balance(z){
        
    }
    int deposit(int amount){
        balance += amount;
        return balance;
    }
    int withdraw(int amount){
        balance -= amount;
        return balance;
    }
    void displayDetails(){
        cout<< "User Account Number " << accountNumber << " balance is " << balance << " User Name is " << accountHolderName << endl;
    }
};

class SavingAccount: public Account{
    public:
    double interestRate;
    SavingAccount(int x, string y, double z, double r): interestRate(r), Account(x,y,z){
        
    }
   double calculateInterest(){
        return balance * interestRate / 100;
    }
    void displaySavingDetails(){
        displayDetails();
        cout << "Interest Rate: " << interestRate << "%" << endl;
        cout << "Interest: " << calculateInterest() << endl;
    }
};


int main() {
   
   Account user1(223423523, "Shahzaib Saleem", 60050.23);
   SavingAccount user2(223423523, "Shahzaib Saleem", 60050.23, 21.3);
   
   user2.displaySavingDetails();

    return 0;
}