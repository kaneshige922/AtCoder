/**
*    author:  kaneshige
*    created: 31.08.2021 11:32:52
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    if (n%10 == 7 or n/10%10 == 7 or n/100%10 ==7){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
