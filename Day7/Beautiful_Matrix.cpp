#include <iostream>
#include <cstdlib> 
using namespace std;
int main(){
	int Arr[5][5],reali,realj;
	for(int i =0;i<5;i++){
		for(int j=0;j<5;j++){
			cin >> Arr[i][j];
			if(Arr[i][j]==1){
				reali=abs(2-i);
				realj=abs(2-j);
			}
		}
	}
	cout<<reali+realj;
//	while(reali!=2 && realj!=2){
//		if(reali<2){
//			reali++;
//			steps++;
//		}
//		else if(reali>2){
//			reali--;
//			steps++;
//		}
//		else if(realj<2){
//			realj++;
//			steps++;
//		}
//		else if(realj>2){
//			realj--;
//			steps++;
//		}
//	}
//	cout << steps-1 << endl;
}
//here i find it difficult for first time as i was using the second loop to itrrate the steps like if i is less than 2
//i will increase and i was increasing the step in it i saw a solution online and he told me to find the distance between 
//i and 2 and j and 2 this will give you the steps 
