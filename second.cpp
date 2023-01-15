#include <iostream>
int main(){
int n,m,s,x;
    bool c=false;
std::cin>>n;
if(n<1){
std::cout<<"Invalid";}
else{
if(n==1){
std::cin>>s;
c=false;}
else{
std::cin>>m>>s;
if(s>m){
x=m;
m=s;
s=x;}
while(n>2){
n=n-1;
std::cin>>x;
if(x>m){
s=m;
m=x;}
else{
if(x>s){
s=x;
}}}
if((m-s)<2){
c=true;}}
std::cout<<c<<std::endl;}
return 0;
}
