/**
*    author:  kaneshige
*    created: 03.09.2021 15:24:02
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    string s,t;
    cin >> s >> t;
    string ans;
    bool a = false;
    for (int i=0;i<s.size()-t.size()+1;i++){
        bool ps =true;
        string u;
        int cnt = 0;
        for(int j=0;j<s.size();j++){
            if (i<=j&&j<i+t.size()){
                if(s[j]==t[cnt] || s[j]== '?'){
                    u += t[cnt];
                    cnt++;
                }else{
                    ps = false;
                    break;
                }
            }else if(s[j]=='?'){
                u += "a";
            }else{
                u += s[j];
            }
        }
        if(ps){
            ans = u;
            a = true;
        }
    }
    if(a){
        cout << ans << endl;
    }else{
        cout << "UNRESTORABLE" << endl;
    }
}
