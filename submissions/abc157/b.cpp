/**
*    author:  kaneshige
*    created: 01.09.2021 21:35:33
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int a[3][3];
    int n;
    for (int i = 0;i < 3;i++){
        for (int j = 0; j < 3;j++){
            cin >> a[i][j];
        }
    }
    cin >> n;
    set<int> b;
    for (int i=0;i<n;i++){
        int x;
        cin >> x;
        b.insert(x);
    }
    bool ans[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            if (b.find(a[i][j])!=b.end()){
                ans[i][j] = true;
            }
        }
    }
    bool T = false;
    for (int i=0; i<3;i++){
        if (ans[i][0]&&ans[i][1]&&ans[i][2]){
            T = true;
        }
        if (ans[0][i]&&ans[1][i]&&ans[2][i]){
            T = true;
        }
    }
    if ((ans[0][0]&&ans[1][1]&&ans[2][2])||(ans[0][2]&&ans[1][1]&&ans[2][0])){
        T = true;
    }
    if (T){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
