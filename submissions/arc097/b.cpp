/**
*    author:  kaneshige
*    created: 06.09.2021 16:55:40
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;

struct UnionFind{
    vector<int> par;
    vector<int> rank;
    UnionFind(int n){
        for(int i=0;i<n;i++){
            par.push_back(-1);
            rank.push_back(0);
        }
    }
    int find(int x){
        if(par[x] == -1){
            return x;
        }else{
            return find(par[x]);
        }
    }
    void unite(int x,int y){
        x = find(x);
        y = find(y);
        if(x == y){ 
            return;
        }
        if(rank[x]<rank[y]){
            par[x] = y;
        }else{
            par[y] = x;
            if(rank[x]==rank[y]){
                rank[x] += 1;
            }
        }
    }
    bool same(int x,int y){
        return find(x) == find(y);
    }
};

int main() {
    int n,m;
    cin >> n >> m;
    vector<int> p;
    for(int i=0;i<n;i++){
        int pi; cin >> pi;
        p.push_back(pi-1);
    }
    UnionFind tree(n);
    for(int i=0;i<m;i++){
        int x,y;
        cin >> x >> y;
        tree.unite(x-1,y-1); 
    }
    unordered_map<int,unordered_set<int>> numl;
    for(int i=0;i<n;i++){
        int j = tree.find(i);
        numl[j].insert(i);
    }
    int ans = 0;
    for(int i=0;i<n;i++){
        if(numl[tree.find(i)].count(p[i])){
            ans ++;
        }
    }
    cout << ans << endl;
}
