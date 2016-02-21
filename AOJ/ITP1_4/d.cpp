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

    long n, s=0, _min, _max;
    cin >> n;
    _min = LONG_MAX;
    _max = LONG_MIN;
    for (int i=0;i<n;++i){
        int t;
        cin >> t;
        s = s + t;
        _min = (_min > t) ? t : _min;
        _max = (_max < t) ? t : _max;
    }
    cout << _min << " " << _max << " " << s << "\n";
}

