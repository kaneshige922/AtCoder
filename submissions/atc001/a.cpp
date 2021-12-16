/**
*    author:  kaneshige
*    created: 05.09.2021 14:38:21
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;


// int find(int x,int y,vector<int>par=par,vector<int>rank=rank);
// void unite(int x,int y,vector<int>par=par,vector<int>rank=rank);
// void same(int x,int y,vector<int>par=par,vector<int>rank=rank);


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
        /*
        if(find(x) == find(y)){
            cout << "Yes" << endl;
        }else{
            cout << "No" << endl;
        }
        */
    }
};

int main() {
    int n,q;
    cin >> n >> q;
    UnionFind tree(n);
    for(int i=0;i<q;i++){
        int p; 
        cin >> p;
        int x,y;
        cin >> x >> y;
        if(p == 0){
            tree.unite(x,y);
        }else{
            if(tree.same(x,y)){
                cout << "Yes" << endl;
            }else{
                cout << "No" << endl;
            }
        }
    }
}

