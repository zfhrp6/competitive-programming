#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int a,b;
    string op;
    while(cin >> a >> op >> b){
        int ret;
        if (op == "?"){
            break;}
        else if (op == "+"){
            ret = a + b;
        }
        else if (op == "-"){
            ret = a - b;
        }
        else if (op == "/"){
            ret = (int)(a/b);
        }
        else if (op == "*"){
            ret = a*b;
        }
        cout << ret << "\n";
        // cout << fixed << setprecision(6) << r*r*pi << " " << 2*r*pi << "\n";
    }
}

