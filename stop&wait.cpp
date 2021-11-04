#include<iostream>
#include<time.h>
#include<conio.h>
#include<stdio.h>
#include<cstdlib>
#include<unistd.h>
#include<ctime>
using namespace std;
int main(){
    int i,j,frames;
    int x,x1=10,x2;
    frames=10;
    i=1;
    j=1;
    cout<<"Number of Frames:"<<frames;
    getch();
    while(frames>0){
            cout<<"\n Sending Frame is "<<i;
            x=rand()%10;
                if(x%10==0){
                    for(x2=1;x2<11;x2++){
                        sleep(x2);
                        cout<<"\n Waiting time "<<x2<<" seconds";
                            
                    }
                    cout<<"\n TIMEOUT";
                    cout<<"\n Sending frames "<<i;
                    x=rand()%10;
                }
                cout<<"\n ack for above frame ";
                frames=frames-1;
                i+=1;
                j+=1;   
    }
    getch();
    cout<<"\n\n\n End of the Protocol";
    return 0;
}
