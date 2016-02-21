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

    const string sh = "#", nl = "\n";
    int n, _a;
    cin >> n;
    vector<int> a;

    for (int i=0;i<n;++i){
        cin >> _a;
        a.push_back(_a);
    }
    reverse(a.begin(), a.end());
    for (int i=0;i<a.size();++i){
        cout << a[i];
        if (i!=a.size()-1){
            cout << " ";
        }
        else {
            cout << nl;
        }
    }
}

