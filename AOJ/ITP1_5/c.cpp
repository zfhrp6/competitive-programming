#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <climits>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    const string sh = "#", nl = "\n", dt = ".";
    int h, w;

    while(cin >> h >> w){
        if ((h==0) && (w==0)){
            break;
        }
        for (int row=0;row<h;++row){
            for (int i=0;i<w;++i){
                if ((row+i)%2==0){
                    cout << sh;
                }
                else {
                    cout << dt;
                }
            }
            cout << nl;
        }
        cout << nl;
    }
}

