/**
*    author:  kaneshige
*    created: 31.08.2021 00:49:27
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string n;
    cin >> n;
    int x = stoi(n.substr(n.size()-1));
    // cout << x << endl;
    set<int> s1 {3};
    set<int> s2 {2,4,5,7,9};
    if (s1.find(x) != s1.end()){
        cout << "bon" << endl;
    }else if(s2.find(x) != s2.end()){
        cout << "hon" << endl;
    }else{
        cout << "pon" << endl;
    }
}
