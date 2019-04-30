
#include <bits/stdc++.h>
using namespace std;
#define watch(x) cout << (#x) << " is " << (x) << endl

void fis(int &number) 
{ 
    bool negative = false; 
    register int c;
    number = 0; 

    c = getchar(); 
    if (c=='-') 
    { 
        negative = true; 
        c = getchar(); 
    } 
    for (; (c>47 && c<58); c=getchar()) 
        number = number *10 + c - 48; 
    
    if (negative) 
        number *= -1; 
}



int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n,k,count=0,x;
	int i,j;
	fis(n);
	fis(k);
	watch(n);
	watch(k);
	for(i=0;i<n;i++){
		fis(x);
		if(x%k==0)
			count++;
	}
	printf("%d\n", count);
	return 0;
}

