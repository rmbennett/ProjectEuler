#include <iostream>

using namespace std;

int fibonacci(int max){
	int x = 1;
	int y = 1; 
	int temp = 0;
	int total = 0;
	while(x < max)
	{	
 		temp = x + y;
		y = x; 
		x = temp;
		if(x%2 == 0)
		total += x;	

	}
	return total;

}	


int main(){
	int max = 4000000;
	int total = fibonacci(max);
	cout << total;
}
