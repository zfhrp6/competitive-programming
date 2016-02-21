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
    int n, m;
    vector<vector<int> > mat;
    vector<int> vec;

    cin >> n >> m;

    for (int row=0;row<n;++row){
      vector<int> tmp_row;
      for (int col=0;col<m;++col){
        int tmp_el;
        cin >> tmp_el;
        tmp_row.push_back(tmp_el);
      }
      mat.push_back(tmp_row);
    }
    for (int row=0;row<m;++row){
      int tmp_el;
      cin >> tmp_el;
      vec.push_back(tmp_el);
    }

    vector<int> ret_vec;
    for (int row=0;row<n;++row){
      int tmp=0;
      for (int col=0;col<m;++col){
        tmp += mat[row][col] * vec[col];
      }
      ret_vec.push_back(tmp);
    }

    for (int row=0;row<n;++row){
      cout << ret_vec[row] << "\n";
    }
}

