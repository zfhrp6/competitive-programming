#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n, x;
    while (cin >> n >> x) {
      int cnt = 0;
      if (n==0 && x==0){
        break;
      }
      for (int i=1;i<=n;++i){
        for (int j=1;j<i;++j){
          for (int k=1;k<j;++k){
            if (i==j || j==k || k==j){
              continue;
            }
            if (i+j+k==x){
              ++cnt;
            }
          }
        }
      }
      cout << cnt << "\n";
    }
}

