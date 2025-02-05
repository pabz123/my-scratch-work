//A nested program using a nested structure and pointers
#include<stdio.h>
#include<string.h>
struct names{
int i;
};
struct initials{
char love[20];
struct names b;
}__attribute((packed))__;
int main(){
    struct initials val = {.love = "precious",.b.i = 20};
struct initials *name = & val;
printf("your name is %s aged %d \n",name->love,name->b.i);
printf("the size of the structures is %d and %d\n",sizeof(struct names),sizeof(struct initials));
getchar();
}
