#include<stdio.h>
int main(){
int x= 2;
int y=3;
if(x==y){
    printf("the variables are equal\n");
}
printf("this demonstrates a for loop\n");
for(x==0;x<=20;x++){
    printf("%d\n",x);
}
printf("this demonstrates a while loop\n");
while(y<=20){
    y++;
    printf("%d\n",y);
}
/*this demonstrates a do while statement*/
do{
    printf("%d\n,x");}
    while(y<=20);
if(x==y){
    printf("the values are the same\n");
}
else if(y!=x){
    printf("the values are different\n");
}
int z;
step1:;
printf("this is the 1st step\n");
step2:;
printf("this is the 2nd step\n");
printf("enter the value to move to a step\n");
scanf("%d",&z);
if(z==1){
    goto step1;
}
else if(z==2){
goto step2;}

else{
    printf("enter either 1 or 2\n");
}
return 0;

}

