#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

void lists(){
  int ss[13];
  int hh[13];
  int cc[13];
  int dd[13];
  for (int i=0;i<13;++i) {
    ss[i] = 1;
    hh[i] = 1;
    cc[i] = 1;
    dd[i] = 1;
  }
  

  int n;
  cin >> n;
  for (int i=0;i<n;++i) {
    string s;
    cin >> s;
    int num;
    cin >> num;
    if (s=="S")
      ss[num-1] = 0;
    else if (s=="H")
      hh[num-1] = 0;
    else if (s=="D")
      dd[num-1] = 0;
    else if (s=="C")
      cc[num-1] = 0;
  }
  for (int i=0;i<13;++i){
    if (ss[i]==1)
      cout << "S " << i+1 << "\n";
  }
  for (int i=0;i<13;++i){
    if (hh[i]==1)
      cout << "H " << i+1 << "\n";
  }
  for (int i=0;i<13;++i){
    if (cc[i]==1)
      cout << "C " << i+1 << "\n";
  }
  for (int i=0;i<13;++i){
    if (dd[i]==1)
      cout << "D " << i+1 << "\n";
  }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    lists();

    // string sorts[4] = {"S", "H", "C", "D"};
    //
    // map<string, int[13]> d;
    // for (int so=0;so<4;++so){
    //   for (int nu=1;nu<14;++nu){
    //     d[sorts[so]][nu-1] = 1;
    //     // d[sorts[so]+ts] = 1;
    //   }
    // }
    //
    //
    // const string sh = "#", nl = "\n";
    // // const int S=0,H=1,C=2,D=3;
    // int n;
    // cin >> n;
    // vector<vector<int> > all;
    //
    // // S H C D
    // // for (int so=0;so<4;++so){
    // //   for (int nu=0;nu<13;++nu){
    // //     all[so].push_back(nu+1);
    // //   }
    // // }
    //
    // for (int i=0;i<n;++i) {
    //   string s;
    //   int t;
    //   string ts;
    //   cin >> s >> t;
    //   // sprintf(ts, "%d", t);
    //   d[s][t-1] = 0;
    // }
    // for (int j=0;j<4;++j) {
    //   for (int i=1;i<14;++i){
    //     if (d[sorts[j]][i] == 1){
    //       cout << sorts[j] << " " << i << nl;
    //     }
    //   }
    // }
}

