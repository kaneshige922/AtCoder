/**
*    author:  kaneshige
*    created: 02.09.2021 22:07:05
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

void printvec(vector<vector<int>> v){
    for (int i=0;i<v.size();i++){
        for(int j=0;j<v[i].size();j++){
            cout << v[i][j] << " ";
        }
    cout << endl;
    }
}



int main() {
    int n,m;
    cin >> n >> m;
    vector <vector<int>> ab;
    for (int i=0;i<m;i++){
        vector<int> a(2);
        cin>>a[0]>>a[1];
        ab.push_back(a);
        }
    sort(ab.begin(),ab.end(),
    [](vector<int> alpha,vector<int> beta){
        if (alpha[0]!=beta[0]){return alpha[0]<beta[0];}
        else if(alpha[1]!=beta[1]){return alpha[1]>beta[1];}
        else{return true;}
    });
    //for (int i=0;i<m;i++){cout << ab[i][0] << " " << ab[i][1] << endl;}
    int first = 0,last = 0;
    int ans = 0;
    for (int i=0;i<m;i++){
        if (last <= ab[i][0]){
            ans += 1;
            first = ab[i][0];
            last = ab[i][1];
        }
        if(first < ab[i][0]){
            first = ab[i][0];
        }
        if(last > ab[i][1]){
            last = ab[i][1];
        }
    }
    cout << ans << endl;
    //printvec(ab);
}
