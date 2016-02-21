#include <iostream>
#include <algorithm>
using namespace std;
const int length = 3;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int W, H, x, y, r;
    cin >> W >> H >> x >> y >> r;
    int left, up, down, right;

    left = x - r;
    up = y + r;
    down = y - r;
    right = x + r;
    if ((left < 0) || (up > H) || (down < 0) || (right > W) ){
        cout << "No";
    }
    else {
        cout << "Yes";
    }
    cout << "\n";
}

