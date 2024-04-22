#include <iostream>
using namespace std;
int main() {
    int size,position;
    scanf("%d %d",&size,&position);
    int arr[size],nextRound;
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<size;i++){
        if(arr[i]>=arr[position-1]&&arr[i]>0){
            nextRound++;
        }
    }
    printf("%d",nextRound);
    return 0;
}