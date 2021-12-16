/**
*    author:  kaneshige
*    created: 07.09.2021 19:19:25
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

struct BFS
{
    vector<vector<ll>> path;
    vector<bool> visit;
    vector<ll> dis;
    BFS(ll n,vector<vector<ll>> p){
        path.resize(n);
        path = p;
        visit.resize(n);
        dis.resize(n);
        rep(i,n){
            visit[i] = false;
            dis[i] = 0ll;
        }
    }
    void bfs(ll s){
        visit[s] = true;
        dis[s] = 0;
        queue <ll> que;
        que.push(s);
        while (!que.empty()){
            ll h = que.front(); que.pop();
            for(auto i:path[h]){
                if(!(visit[i])){
                    dis[i] = dis[h] + 1ll;
                    visit[i] = true;
                    que.push(i);
                }
            }
        }  
    }
};





int main() {
    int n; cin>>n;
    vector<vector<ll>> path(n);
    rep(i,n-1){
        ll a,b; cin >> a >>b;
        path[a-1].push_back(b-1);
        path[b-1].push_back(a-1);
    }
    BFS g1(n,path);
    BFS g2(n,path);
    g1.bfs(0);
    ll next; ll d = 0;
    rep(i,n){
        if (g1.dis[i] > d){
            next = i;
            d = g1.dis[i];
        } 
    }
    g2.bfs(next);
    ll ans = 0;
    rep(i,n){
        ans = max(ans,g2.dis[i]+1);
    }
    cout << ans << endl;
}
