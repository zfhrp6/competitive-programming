#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int a, b, c, cnt;
    cin >> a >> b >> c;
    for (int i=a;i<=b;++i){
        (c%i)==0 ? ++cnt : cnt ;
    }
    cout << cnt << "\n";
}

