#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int a, b;
    cin >> a >> b;
    cout << (int)(a/b) << " " << (int)(a%b) << " " << fixed << (double)a/b << "\n";
}

