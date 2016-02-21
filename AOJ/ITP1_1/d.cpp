#include <iostream>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int sec;
    cin >> sec;
    cout << (int)(sec/3600) << ":" << (int)((sec%3600)/60) << ":" << (int)(sec%60) << "\n";
}
