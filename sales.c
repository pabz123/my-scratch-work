
//monthly sales
#include<stdio.h>
int findhighestsale(int sugar[3], int soap[3],int rice[3]);
int main(){
//declaring our sales, including the most sold item
int highest=0;
int best_sales;
//a for loop to obtain the sold items over 3 months1
for(int i=0;i<3;i++){
printf("Enter sales for each month %d: \n", i+1);
scanf("%d %d %d", &sugar[i], &soap[i] , &rice[i]);
int total = (sugar[i] + soap[i] + rice[i]);

//if statement to obtain the highest sales
if(total > highest){
highest = total;
best_sales = i+1;}}

//1 for sugar, 2 for soap, 3 for rice
//int findhighestsale(){}

int total_sugar = sugar[0]+ sugar[1]+ sugar[2];
int total_soap = soap[0]+soap[1]+soap[2];
int total_rice = rice[0]+rice[1]+rice[2];
printf("Total sales of sugar is: %d\n",total_sugar);
printf("Total sales of soap is: %d\n",total_soap);
printf("Total sales of rice is: %d\n",total_rice);

switch(best_sales){
case 1 : printf("sugar has the highest sales of: %d units\n", sugar[0] + sugar[1] + sugar[2]);
break;
case 2 : printf("soap has the highest sales of: %d units\n",soap[0] + soap[1] + soap[2] );
break;
case 3 : printf("rice has the highest sales of: %d units\n",rice[0] + rice[1] + rice[2]);
break;}
getchar();
return 0;
}

//int findhighestsale(){

//
