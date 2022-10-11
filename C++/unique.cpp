#include<iostream>
using namespace std;
int find(int arr[],int size){
    int ans=0;
    for (int i = 0; i < size; i++)
    {
        ans=ans^arr[i];
    }
    return ans;
}
int main(){
    int arr[5]={2,3,2,3,1};
    int ans=find(arr,5);
    cout<<"Answer is : "<<ans<<endl;
    return 1;
}