#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int r, c;
    int mat[200][200];

    cin >> r >> c;

    int el;
    int rsum, csum;
    for (int row=0;row<r;++row){
      rsum=0;
      for (int col=0;col<c;++col){
        cin >> el;
        mat[row][col] = el;
        rsum += el;
      }
      mat[row][c] = rsum;
    }

    for (int col=0;col<c;++col){
      csum = 0;
      for (int row=0;row<r;++row){
        csum += mat[col][row];
      }
      mat[r][col] = csum;
      cout << "csum: " << csum;
    }

    int allsum=0;
    for (int row=0;row<r;++row){
      allsum += mat[row][c];
    }
    mat[r][c] = allsum;

    for (int row=0;row<r+1;++row){
      for (int col=0;col<c+1;++col){
        cout << mat[row][col];
        if (col==c){
          cout << "\n";
        }
        else {
          cout << " ";
        }
      }
    }
}

