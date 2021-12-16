/**
*    author:  kaneshige
*    created: 08.09.2021 23:28:09
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

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

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

int main() {
    int h,w; cin >> h >> w;
    int col[h][w];
    rep(i,h){
        rep(j,w){
            col[i][j] = false;
        }
    }
    UnionFind tree(h*w);
    int q; cin >> q;
    rep(i,q){
        int t; cin >> t;
        if (t==1){
            int r,c; cin >> r>> c;
            col[r-1][c-1] = true;
            rep(j,4){
                int xx = r-1+dx[j]; int yy = c-1+dy[j];
                if(xx<0 || h<=xx || yy<0 || w<=yy){continue;}
                if(col[xx][yy]){
                    tree.unite((r-1)*w+c-1,xx*w+yy);
                }
            }
        }else{
            int ra,ca,rb,cb; cin >> ra >> ca >> rb >>cb;
            if(col[ra-1][ca-1] && col[rb-1][cb-1] && tree.same(w*(ra-1)+ca-1,w*(rb-1)+cb-1)){
                cout << "Yes" << endl;
            }else
            {
                cout << "No" << endl;
            }
        }
        
    }

}
