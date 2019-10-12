#include<iostream.h>
#include<conio.h>
#include<process.h>
class car_race
{
public:
int id[20],total,n,p;
void input();
void show();
void inc();
void dec();
void display();
}c;
int i;
void main()
{
clrscr();
int n,opt;
c.input();
while(1)
{
cout<<"\n Main Menu";
cout<<"\n 1.Enter a car\n 2. Delete a car";
cout<<"\n Enter your choice";
cin>>opt;
switch(opt)
{
case 1:cout<<"\n Enter the id of car you want to enter";
       c.input();
       n++;
       cout<<"\n";
       for(i=0;i<n;i++)
       c.show();
       cout<<"\n";
       c.inc();break;
case 2:c.dec();
       cout<<"\n";
       c.display();break;
case 3:exit(0);
}
getch();
}
}
void car_race::input()
{
int t=0,n;
if(t==0)
{
cout<<"\n Enter the no of car ";
cin>>n;
cout<<"\n Enter car's id:";
for(i=0;i<n;i++)
cin>>id[i];
total++;
t++;
}
else
{
i++;
cout<<"\n Enter the id of car";
cin>>id[i];
}
}
void car_race::inc()
{
cout<<"\n The total no of cars is"<<total;
}
void car_race::show()
{
cout<<"\t"<<id[i];
cout<<"\n";
}
void car_race::dec()
{
int t;
cout<<"\n Enter id of car you want to delete";
cin>>t;
for(i=0;i<total;i++)
{
if(t==id[i])
{
p=i;
}
}
cout<<"\n The position of id is"<<(p+1);
total--;
}
void car_race::display()
{
for(i=p;i<total;i++)
{
id[i]=id[i+1];
}
for(i=0;i<total;i++)
{
cout<<id[i];
cout<<"\n";
}
}