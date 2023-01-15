#include <iostream>
using namespace std;
int main(){
    int t,i,n,x,m,j;
    std::cin>>t;
    for(i=0;i<t;i++){
        n=0;
        m=0;
        x=0;
        std::cin>>n;
        int [n]s;
        for(j=0;j<n;j++){
            std::cin>>s[j];
            
        }
        sort(s.begin(),s.end());
        for(j=0;j<n;j++){
            if((n-j)*s[j]>m){
                m=(n-j)*s[j];
            }
        }
        std::cout<<m<<"\n";
    }
    return 0;
}
