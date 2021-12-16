#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long ab[n][2];
    for (int i = 0; i < n; i++){
        for (int j = 0;j < 2; j++){
            cin >> ab[i][j];
        }
    }
    /*
    for (int i = 0; i < n; i++){
        for (int j = 0;j < 2; j++){
            cout << ab[i][j] << " ";
        }
        cout << endl;
    }
    */
    long long ans = 0;
    for (int i = 0; i < n; i++){
        ans += (ab[i][1]-ab[i][0]+1)*(ab[i][1]+ab[i][0])/2;
    }
    cout << ans << endl;
}
