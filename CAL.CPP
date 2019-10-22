#include<stdio.h>
#include<conio.h>
#include<process.h>
#include<dos.h>
#include<time.h>
void main()
{
clrscr();
int opt,b,l,m;
long int i,n,a[10000],s;
time_t beg1,end1,beg2,end2;
double diff,diff1;
printf("\n Enter no of values");
scanf("%ld",&n);
for(i=1;i<=n;i++)
{
a[i]=i;
printf("%ld\t",a[i]);
}
printf("\n Main Menu");
printf("\n 1.Linear Search\n2.Bineary Search\n3.Exit");
printf("\n Enter your choice");
scanf("%d",&opt);
switch(opt)
{
case 1:printf("\n Enter no you want to search");
       scanf("%ld",&s);
       beg1=clock();
       for(i=1;i<=n;i++)
       {
       delay(10);
       if(a[i]==s)
       {
       printf("\n Number  found");
       break;
       }
       }
       end1=clock();
       diff=(double)((end1-beg1)/CLOCKS_PER_SEC);
       printf("\n Time taken in linear search is %lf",diff);
       break;
case 2:printf("\n Enter no to be search");
       scanf("%ld",&s);
       l=n;
       b=1;
       beg2=clock();
       while(b<=l)
       {
       m=(l+b)/2;
       if(a[m]>s)
       {
       l=m-1;
       }
       else if(a[m]==s)
       {
       printf("\n Number found");
       break;
       }
       else
       {
       b=m+1;
       }
       delay(5);
       }
       end2=clock();
       diff1=(double)((end2-beg2)/CLOCKS_PER_SEC);
       printf("\t Time taken in binary search is %lf",diff1);
       break;
case 3:exit(0);
}
getch();
}


