#include<iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	int minvalue = 101, maxindex=0,minindex=0,maxvalue=0;
	for(int i=0;i<n;i++)
	{int x;
	cin>>x;
		if(x>maxvalue){
			maxvalue=x;
			maxindex=i;} 
		if(x<=minvalue){
			minvalue=x;
			minindex=i;}
	}
	if(maxindex>minindex){
		cout<<(maxindex-1)+(n-minindex)-1;		
	}
	else{
		cout<<(maxindex-1)+(n-minindex);
	}
}
