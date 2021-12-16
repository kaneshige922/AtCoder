/**
*    author:  kaneshige
*    created: 05.09.2021 22:51:33
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> path(n);
    map<vector<int>,int> length;
    for(int i=0;i<n-1;i++){
        int u,v,w;
        cin >> u >> v >> w;
        path[u-1].push_back(v-1);
        path[v-1].push_back(u-1);
        vector<int> uv{u-1,v-1};
        length[uv] = w;
    }
    vector<bool> ans(n,0);
    deque<int> q;
    unordered_set<int> v;
    q.push_back(0);
    v.insert(0);
    while (q.size()!=0){
        int now = q.front();
        q.pop_front();
        for(int i : path[now]){
            if(!(v.count(i))){
                q.push_back(i);
                v.insert(i);
                if(length[{min(now,i),max(now,i)}]%2 == 0){
                    ans[i] = ans[now];
                }else{
                    ans[i] = not(ans[now]);
                }

            }
        }

    }
    for(int i=0;i<n;i++){
        cout << ans[i] << endl;
    }
}
