#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int x, y;
    while(cin >> x >> y){
    if (!((x==0) && (y==0))){
        cout << min(x, y) << " " << max(x, y) << "\n";
    }
    else {
        break;
    }
    }
}

