#include<stdio.h>
#include<math.h>
int gcd(int a, int b){
while(b != 0){
int temp = b;
b=a%b;
a = temp;
}
return a;
 }
int main(){
int num1,num2;
printf("Enter the two numbers:");
scanf("%d  %d",&num1,&num2);
int result = gcd(num1, num2);
printf("The GCD of %d and %d is %d\n",num1,num2,result);
getchar();
}
