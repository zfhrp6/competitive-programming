#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int m, f, r;
    while( cin >> m >> f >> r ){
      if ( m==-1 && f==-1 && r==-1 ){
        break;
      }

      if ( m==-1 || f==-1 ){
        cout << "F";
      }
      else if (m+f >= 80 ){
        cout << "A";
      }
      else if (65 <= m+f && m+f < 80){
        cout << "B";
      }
      else if (50 <= m+f && m+f < 65){
        cout << "C";
      }
      else if (30 <= m+f && m+f < 50){
        if (r >= 50){
          cout << "C";
        }
        else {
          cout << "D";
        }
      }
      else {
        cout << "F";
      }
      cout << "\n";
    }
}

