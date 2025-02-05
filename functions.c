#include <stdio.h>
int product();
void product1(int x, int y);
//void product2(void);
int main(){
//int product();
//int a,b;
//printf("Enter two values:");
//scanf("%d %d",&a ,&b);
//int c = a*b;
  //product(a,b);
// printf("The product is %d\n",c);
void product1(int x, int y);
    return 0;
}
int product(){
int x,y;
printf("Enter the two values:");
scanf("%d and %d",&x, &y);
int pdt;
pdt = x*y;
printf("The product is %d.",pdt);
return pdt;
}
/*void product1(int x, int y){
  int d,e;
  int k = d*e;
  printf("%d",k);
}
void product2(void){
  int x,y,z;
  printf("Enter three values:",x,y,z);
  scanf("%d %d %d", &x,&y,&z);
  int i = x*y*z;
printf("%d",i);
}*/
