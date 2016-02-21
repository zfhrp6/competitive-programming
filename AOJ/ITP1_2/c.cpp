#include <iostream>
#include <algorithm>
using namespace std;
const int length = 3;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int num[length];
    for (int i=0; i<length; i++){
      cin >> num[i];
    }
    // cin >> num[0] >> num[1] >> num[2];

    sort(num, num + length);
    for (int i=0;i<length; i++){
      cout << num[i];
      if (i<length-1) {
        cout << " ";
      }
    }
    cout << "\n";
}
