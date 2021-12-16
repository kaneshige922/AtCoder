/**
*    author:  kaneshige
*    created: 31.08.2021 02:39:17
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n,k;
    cin >> n >> k;
    set<int> S;
    for (int i = 0; i < k;i++){
        int d;
        cin >> d;
        for (int j = 0; j < d;j++){
            int a;
            cin >> a;
            S.insert(a);
        }
    }
    cout << n - S.size() << endl;
}
