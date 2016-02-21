#include <iostream>
using namespace std;

void call(int n){
  int i = 1;
 CHECK_NUM:
  int x = i;
  if ( x % 3 == 0 ){
    cout << " " << i;
    goto END_CHECK_NUM;
  }
 INCLUDE3:
  if ( x % 10 == 3 ){
    cout << " " << i;
    goto END_CHECK_NUM;
  }
  x /= 10;
  if ( x ) goto INCLUDE3;
 END_CHECK_NUM:
  if ( ++i <= n ) goto CHECK_NUM;

  cout << endl;
}

void call_no_goto(int n){
  for (int i=1;i<=n;++i) {
    if (i % 3 == 0 ) {
      cout << " " << i;
    }
    else {
      int t = i;
      while (t > 0) {
        if (t % 10 == 3){
          cout << " " << i;
          break;
        }
        t /= 10;
      }
    }
  }
  cout << "\n";
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  int n;
  cin >> n;
  call_no_goto(n);
}
