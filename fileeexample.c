#include <stdio.h>
int main(){	
	FILE *fp;
	fp = fopen("tmp.txt", "w");
	fprintf(fp,"This is a test\n");
	fclose(fp);
	return 0;
}
