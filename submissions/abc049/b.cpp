/**
*    author:  kaneshige
*    created: 06.09.2021 01:07:37
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
    int n,k,l;
    cin >> n>> k >> l;
    UnionFind road(n);
    for(int i=0;i<k;i++){
        int p,q;
        cin >> p >> q;
        road.unite(p-1,q-1);
    }
    /*
    map<int,set<int>> rd;
    for(int i=0;i<n;i++){
        rd[road.find(i)].insert(i);
    }
    */
    UnionFind rail(n);
    for(int i=0;i<l;i++){
        int p,q;
        cin >> p >> q;
        rail.unite(p-1,q-1);
    }
    /*
    map<int,set<int>> rl;
    for(int i=0;i<n;i++){
        rl[rail.find(i)].insert(i);
    }
    */
    unordered_map<int,unordered_map<int,int>> rdrl;
    for(int i=0;i<n;i++){
        int df = road.find(i);
        int lf = rail.find(i);
        if(rdrl.count(df)){
            if(rdrl[df].count(lf)){
                rdrl[df][lf] += 1;  
            }else{
                rdrl[df][lf] = 1;
            }
        }else{
            rdrl[df][lf] = 1;
        }
    }
    for(int i=0;i<n;i++){
        cout << rdrl[road.find(i)][rail.find(i)] << " ";
    }
    /* ŒvŽZ—Ê(N^2)
    for(int i=0;i<n;i++){
        vector<int> result;
        set_intersection(rd[road.find(i)].begin(),rd[road.find(i)].end()
            ,rl[rail.find(i)].begin(),rl[rail.find(i)].end(),back_inserter(result));
        cout << result.size() << " ";
    }
    */
    cout << endl;
}
