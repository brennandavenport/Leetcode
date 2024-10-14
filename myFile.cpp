#include <iostream>

class Dog {
private:
    int age;
    std::string name;
    

public:
    Dog(std::string dogName, int dogAge) {
        name = dogName;
        age = dogAge;
    }

    void bark() {
        std::cout << name << " says Woof" << std::endl;
    }

    void info() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Age: " << age << std::endl;
    }
};

int main() {
    int a = 3;
    int * p = &a;

    std::cout << "Hello World" << std::endl;

    std::cout << a << std::endl;
    std::cout << p << std::endl;

    Dog* myDog = new Dog("Jeff", 5);
    
    myDog->bark();

    myDog->info();

    delete myDog;
    

    return 0;


}

