#include <iostream>
using namespace std;

int main() {
    int r, c,counter=0;
    cin >> r >> c;
    char arry[r][c];
     for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            arry[i][j] = '.';
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if(i%2==0){
                arry[i][j]='#';
                // if(counter==0){
                //     counter=1;
                // }   
                // else{
                //     counter=0;
                // }
            }
            else{
                if (i % 4 == 1) {
                arry[i][c - 1] = '#'; // Fill the last column
            } else if (i % 4 == 3) {
                arry[i][0] = '#'; // Fill the first column
            }
            }
        }  
    }
     // for (int i = 0; i < r; i++) {
    //     for (int j = 0; j < c; j++) {
    //           if (i % 2 == 0) {
    //             arry[i][j] = '#';
    //         }
            
    //     }
    //     if(i%2!=0){
    //             if(counter==0){
    //                 arry[i][c-1]='#';
    //             }
    //             if(counter==1){
    //                arry[i][0]='#';
    //             }
    //         }
    //     if()
    // }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << arry[i][j];
        }
        cout << "\n";
    }
    return 0;
}
