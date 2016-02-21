#include <iostream>
#include <string>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int a, b, c;
    cin >> a >> b >> c;
    if ((a < b) && (b < c)){
      cout << "Yes";
    }
    else {
      cout << "No";
    }
    cout << "\n";
}
