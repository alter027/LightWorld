#include<bits/stdc++.h>
using namespace std;

struct node{
	int num;
	int val;
	bool operator<(const node& b) const
    {return val < b.val;}
 };
priority_queue<node> P;
int N = 100;

void InputData(void){
	int tmp,input;
	int i,j;
	for(i=0;i<N;i++){
		tmp=0;
		for(j=0;j<N;j++){
			scanf("%d",&input);
			tmp+=input;
		}
		node tri;
		tri.num=i+1;
		tri.val=tmp;
		P.push(tri);
	}
 }

int main(void){
	InputData();
	for(int i=0;i<40;i++){
		printf("%d ",P.top().num);
		P.pop();
	}
	return 0;
 }