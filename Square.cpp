#include <iostream>
#include "Ansh.h"
int main(){
    Ansh an;
    int n;
    std::cout<<"Enter a number:";
    std::cin>>n;
    an.length(n);
    an.square();
    std::cout<<"The square of "<< n << " is ";
    std::cout<<an.a<<std::endl;
    return 0;
}