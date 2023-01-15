#include <iostream>
#include <vector>
int main(){
    int t,i,n,x,m,j;
    std::cin>>t;
    for(i=0;i<t;i++){
        std::vector<int> s;
        n=0;
        m=0;
        x=0;
        std::cin>>n;
        for(j=0;j<n;j++){
            std::cin>>x;
            s.push_back(x);
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
#include <iostream>
#include <vector>
int main(){
int n;
std::cin>>n>>std::endl;
std::vextor<int> a;
int i;
for(i=0;i<n;i++){
int x;
std::cin>>x;
a.push_back(x);
