#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int member[4][3][10] = {0};
    int n;

    cin >> n;
    for (int i=0;i<n;++i) {
      int tou,fl,ro,num;
      cin >> tou >> fl >> ro >> num;
      member[tou-1][fl-1][ro-1] += num;
    }
    for (int tou=0;tou<4;++tou) {
      for (int fl=0;fl<3;++fl) {
        for (int ro=0;ro<10;++ro) {
            cout << " ";
          cout << member[tou][fl][ro];
          // else
            // cout << "\n";
        }
        // if (fl!=3-1)
          cout << "\n";
      }
      if (tou!=4-1)
        cout << "####################\n";
    }
}

