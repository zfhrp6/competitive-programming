#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    double r;
    const double pi = 4*atan(1);
    cin >> r;
    printf("%.8f %8f\n", r*r*pi, 2*r*pi);
    // cout << fixed << setprecision(6) << r*r*pi << " " << 2*r*pi << "\n";
}

