/**
*    author:  kaneshige
*    created: 01.09.2021 20:47:50
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    string s;
    cin >> s;
    int a = 0,b = 0;
    for (int i = 0; i < 3; i++){
        if (s[i] == 'A'){
            a ++;
        }
        if (s[i] == 'B'){
            b++;
        }
    }
    if (a >= 1 && b >= 1){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
