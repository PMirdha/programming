#include <bits/stdc++.h>
using namespace std;
#define watch(x) cout << (#x) << " is " << (x) << endl

const int INF = 0x3f3f3f3f;

typedef long long ll;
typedef pair w;
typedef vector va;
typedef vector vb;
typedef vector vc;

void variables(){
	auto a = 100; // a will become 'int'
	auto b = 1LL; // b will become 'long long'
	auto c = 1.0; // c will become 'double'
	auto d = "variable"; // d will become 'string'
	// initialize DP memoization table with -1
	memset(memo, -1, sizeof memo); 

	// to clear array of integers
	memset(arr, 0, sizeof arr);

	// index++; if (index >= n) index = 0;
	index = (index + 1) % n; 

	// index--; if (index < 0) index = n - 1;
	index = (index + n - 1) % n; 

	// for rounding to nearest integer
	int ans = (int)((double)d + 0.5); 

	// min/max shortcut to update max/min
	ans = min(ans, new_computation);
}

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

int fis_mat(int &r, int &c, char type){
	r=c=0;
	fast_int_scan(r);
	fast_int_scan(c);
	int mat[r][c];
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++)
			fast_int_scan(mat[i][j]);
	}
	return mat
}