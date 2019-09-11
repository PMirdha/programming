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

// Fast Integer Scan
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

typedef vector<vector<int> > imat;
imat fis_mat(int &r, int &c){
	r=c=0;
	fis(r);
	fis(c);
	imat mat(r);
	for(int i=0;i<r;i++){
		mat[i] = va(c);
		for(int j=0;j<c;j++)
			fis(mat[i][j]);
	}
	return mat;
}