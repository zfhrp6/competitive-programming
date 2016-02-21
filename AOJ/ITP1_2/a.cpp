#include <iostream>
#include <string>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int a, b;
    cin >> a >> b;
    cout << "a ";
    if (a > b){
      cout << ">";
    }
    else if (a < b){
      cout << "<";
    }
    else {
      cout << "==";
    }
    cout << " b" << "\n";
}
