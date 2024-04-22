#include<iostream>
using namespace std;
int main(){
    int numrow;
    scanf("%d",&numrow);
    int a,b,c,answ=0;
    for(int i=0;i<numrow;i++){
        scanf("%d",&c);
        scanf("%d",&b);
        scanf("%d",&a);
        if(2<=a+b+c){
        	answ++;
		}
    }
	printf("%d",answ);
}
