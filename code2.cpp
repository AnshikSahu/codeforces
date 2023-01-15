#include <iostream>
#include <vector>
int main(){
    int i,n,m=0,s=0,d=0;
    std::cin>>n;
    for(i=0;i<n;i++){
        int x;
        std::cin>>x;
        if(x>m){
            s=m;
            m=x;
            d=i+1;
        }
    }
    std::cout<<d<<" "<<s<<std::endl;
}
