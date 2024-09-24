#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int initialPower,n,t,result,greenSerums,blueSerums;
    cin>>t;
    for(int i=0;i<t;i++){
        vector<int> welderPowers;
        greenSerums = 2;
        blueSerums = 1;
        cin>>n>>initialPower;
        for(int j=0;j<n;j++){
            int temp;
            cin>>temp;
            welderPowers.push_back(temp);
        }
        result = n;
        sort(welderPowers.begin(), welderPowers.end());
        for (int j = 0; j < n; j++) {
            if (initialPower > welderPowers[j]) {
                initialPower += (welderPowers[j] / 2);
            } else {
                if (greenSerums > 0 && 2 * initialPower > welderPowers[j]) {
                    initialPower *= 2;
                    greenSerums -= 1;
                    initialPower += (welderPowers[j] / 2);
                } else if (blueSerums > 0 && 3 * initialPower > welderPowers[j]) {
                    initialPower *= 3;
                    blueSerums -= 1;
                    initialPower += (welderPowers[j] / 2);
                } else if (greenSerums > 1 && 4 * initialPower > welderPowers[j]) {
                    initialPower *= 4;
                    greenSerums -= 2;
                    initialPower += (welderPowers[j] / 2);
                } else {
                    result = j;
                    break;
                }
            }
        }
        cout<<result<<endl;
    }
    return 0;
}
