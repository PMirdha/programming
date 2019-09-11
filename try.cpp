
#include <bits/stdc++.h>
using namespace std;
#define watch(x) cout << (#x) << " is " << (x) << endl
typedef vector<vector<int> > imat;
typedef vector<int> va;

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

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int r,c,count=0,x;
	int i,j;
	imat mat = fis_mat(r, c);
	solve(mat, r, c);

	return 0;
}

