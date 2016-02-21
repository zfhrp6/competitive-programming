#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void v_print(vector<int> v){
  for (int i=0;i<v.size();++i){
    cout << " d" << v.at(i);
  }
  cout << "\n";
}

void vv_print(vector<vector<int> > v){
    for (int i=0;i<v.size();++i){
      v_print(v.at(i));
    }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int r, c;
    cin >> r >> c;

    vector< vector<int> > mat;
    for (int i=0;i<r;++i) {
      vector< int > row;
      for (int j=0;j<c;++j) {
        int num;
        cin >> num;
        row.push_back(num);
      }
      // v_print(row);
      mat.push_back(row);
    }
    vv_print(mat);

    vector<int> colsum;
    cout << "size: " << colsum.size();
    for (int _r;_r<r;++_r){
      int rowsum = 0;
      // cout << "_r" << _r;
      for (int _c;_c<c;++_c){
    cout << "hoge\n";
    cout << "size: " << colsum.size() << "\n";
        rowsum += mat[_r][_c];
        cout << mat[_r][_c] << " ";
    cout << "piyo\n";
    cout << "size: " << colsum.size() << "\n";
    cout << "kkk" << colsum.size() << " " << _c;
        if (colsum.size() < _c){
          colsum.push_back(mat[_r][_c]);
    cout << "fuga\n";
    cout << "size: " << colsum.size() << "\n";
        }
        else {
          colsum[_c] = colsum[_c] + mat[_r][_c];
    cout << "hoga\n";
    cout << "size: " << colsum.size() << "\n";

        }
      }
      cout << rowsum << "\n";
    }

    int allsum = 0;
    for (int i;i<colsum.size();++i) {
      cout << colsum[i] << " ";
      allsum += colsum[i];
    }
    cout << allsum << "\n";
}

