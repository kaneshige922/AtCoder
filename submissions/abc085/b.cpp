/**
*    author:  kaneshige
*    created: 05.09.2021 13:14:22
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    set<int> s;
    for(int i=0;i<n;i++){
        int d; cin >> d;
        s.insert(d);
    }
    cout << s.size() << endl;
}
