/**
*    author:  kaneshige
*    created: 02.09.2021 11:14:41
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    string a,b,u;
    int x,y;
    cin >>a>>b>>x>>y>>u;
    if (a==u){
        x--;
    }else{
        y--;
    }
    cout << x << " " << y << endl;
}
