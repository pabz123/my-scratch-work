#include <stdio.h>
main() {
//sizeof() is one of the library functions in C
 	printf( "\nA char is %d bytes", sizeof( char ));
	printf( "\nAn int is %d bytes", sizeof( int ));
	printf( "\nA short is %d bytes", sizeof( short ));
	printf( "\nA long is %d bytes", sizeof( long ));
	printf( "\nAn unsigned char is %d bytes", sizeof( unsigned char ));
	printf( "\nAn unsigned int is %d bytes", sizeof( unsigned int ));
	printf( "\nAn unsigned short is %d bytes", sizeof( unsigned short ));
	printf( "\nAn unsigned long is %d bytes", sizeof( unsigned long ));	
	printf( "\nA float is %d bytes", sizeof( float ));
	printf( "\nA double is %d bytes\n", sizeof( double ));
return 0;
 }
