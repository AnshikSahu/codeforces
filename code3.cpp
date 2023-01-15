#include <iostream>
#include <vector>
int main(){
    int t,a,b,x;
    std::cin>>t;
    while(t>0){
        t=t-1;
        std::cin>>a>>b;
        if(a==0){
            x=1;
        }
        else{
            x=a+b*2+1;
        }
        std::cout<<x<<std::endl;
    }
    return 0;
}
