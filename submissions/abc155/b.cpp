/**
*    author:  kaneshige
*    created: 02.09.2021 10:47:30
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0;i<n;i++){
        int a;
        cin >> a;
        if (a%2==0){
            if(a%3!=0 && a%5!=0){
                cout <<"DENIED" << endl;
                exit(0);
            }
        }
    }
    cout << "APPROVED" << endl;
}
