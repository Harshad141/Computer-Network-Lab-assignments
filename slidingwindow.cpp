#include<iostream>
#include<ctime>
#include<time.h>
#include<stdio.h>
#include<cstdlib>
using namespace std;
int main()
{
 int framenumber,N;
 int no_tr=0;
 srand(time(NULL));
 cout<<"Number of Packets : ";
 cin>>framenumber;
 cout<<"Size of window : ";
 cin>>N;
 int i=1;
 while(i<=framenumber)
 {
     int x=0;
     for(int j=i;j<i+N && j<=framenumber;j++)
     {
         cout<<"Sent Packet "<<j<<endl;
         no_tr+=1;
     }
     for(int j=i;j<i+N && j<=framenumber;j++)
     {
         int temp = rand()%2;
         if(!temp)
             {
                 cout<<"Acknowledgment for Frame "<<j<<endl;
                 x+=1;
             }
         else
             {   cout<<"Frame "<<j<<" Not Received"<<endl;
                 cout<<"Retransmitting Window"<<endl;
                 break;
             }
     }
     cout<<endl;
     i+=x;
 }
 cout<<"(Total transmission) : "<<no_tr<<endl;
 return 0;
}
