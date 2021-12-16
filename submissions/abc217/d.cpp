/**
*    author:  kaneshige
*    created: 04.09.2021 21:26:47
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
    int l,q;cin>>l>>q;
    vector<vector<int>> cx(q,vector<int>(2,0));
    for(int i=0;i<q;i++){
        cin >> cx[i][0] >> cx[i][1];
    }
    //printvec(cx);
    set<int> wood{0,l};
    for(int i=0;i<q;i++){
        if(cx[i][0]==1){
            wood.insert(cx[i][1]);
        }else{
            auto a = wood.lower_bound(cx[i][1]);
            int x = *a;
            a--;
            int y = *a;
            cout << x - y << endl;
        }
    }
}
