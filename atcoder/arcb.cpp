#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
 
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

void debu(string s){
  cout << s;
}

void de(){
  cout << "Test ";
}

int j(int n, int m){
  if ((n==1 && m==2) || (n==2 && m==3) || (n==3 && m==1)){
    return 0;
  }
  if ((n==1 && m==3) || (n==2 && m==1) || (n==3 && m==2)){
    return 1;
  }
  return 2;
}

int jw(int n){
  if (n==1)
    return 1;
  if (n==2)
    return 2;
  else
    return 0;
}

int jl(int n){
  if (n==1)
    return 2;
  if (n==2)
    return 0;
  else
    return 1;
}

int jd(int n){
  if (n==1)
    return 0;
  if (n==2)
    return 1;
  if (n==3)
    return 2;
}

int main(){
  int data[100001][2] = {};
  int rslt[100001][3] = {};
  int cnt[100001] = {};
  int n;
  cin >> n;
  vector<pair<int, int> > men;
  for(int i=0;i<n;++i) {
    int r,h;
    cin >> r >> h;
    data[i][0] = r;
    data[i][1] = h;
    rslt[r][h-1]++;
    cnt[r]++;
    men.push_back(pair<int, int>(r,h));
    // de();
  }

  // cout << "--input--" << endl;

  int rate_s = 0;
  int win_cnt[100001] = {};
  for (int i=0;i<100001;++i){
    win_cnt[i] = rate_s;
    rate_s = rate_s + cnt[i];
  }

  for(int i=0; i<men.size(); ++i) {
    int w = rslt[men[i].first][jw(men[i].second)];
    int l = rslt[men[i].first][jl(men[i].second)];
    int d = rslt[men[i].first][jd(men[i].second)] - 1;

    // cout << win_cnt[men[i].first] << " " << d << "----" << endl;
    cout << win_cnt[men[i].first] + w << " "
         << n - 1 - win_cnt[men[i].first] - w - d << " "
         << d
         << endl;
  }

}
