#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int t,n,m;
    cin>>t;
    for(int i = 0; i<t;i++){
        cin>>n;
        int arr[n];
        for(int j = 0;j<n;j++){
            cin>>arr[j];
        }
        arr.sort(arr.begin,arr.end);
        cin>>m;
        int tot = 0;
        int c=0;
        while(tot<=m && c<n){
            tot+=arr[c];
            c+=1;
        }
        cout>>c;
        m=0;

    }
}
