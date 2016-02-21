#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int idx = 1, x;
    while(cin >> x) {
        if (x == 0) {
            break;
        }
        cout << "Case " << idx << ": " <<  x << "\n";
        ++idx;
    }
}

