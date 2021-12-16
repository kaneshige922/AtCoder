/**
*    author:  kaneshige
*    created: 05.09.2021 13:56:24
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;

int main() {
    int n,m;
    cin >> n;
    map<string,int> score;
    for(int i=0;i<n;i++){
        string s;
        cin >> s;
        if(score.count(s)){
            score[s] += 1;
        }else{
            score[s] = 1;
        }
    }
    cin >> m;
    for(int i=0;i<m;i++){
        string s;
        cin >> s;
        if(score.count(s)){
            score[s] -= 1;
        }else{
            score[s] = -1;
        }
    }
    int ans = 0;
    for(auto p:score){
        ans = max(ans,p.second);
    }
    cout << ans << endl;
}
