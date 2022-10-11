#include<iostream>
using namespace std;
int fibo(int n){
    if(n<=1 )
    {
        return n;
    }
    int last=fibo(n-1);
    int slast=fibo(n-2);
    
    return last + slast;

}
int main(){
   int result = fibo(6);
   cout<<"Result is : "<<result;
   return 0;
}