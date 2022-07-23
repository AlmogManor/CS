char c = 'a'; // always 1 byte, CAN also be used for numbers, not only letters
short sh = 1; // always 2 bytes
int i = 1; // on 16-biy systems 2 bytes, otherwise 4 bytes
long l = 1; // on 32-bit systems 4 bytes, on 64-bit 8 bytes
long long ll = 1; // at least 8 bytes

unsigned int us = 1; // (assuming 4 bytes) ranges from [0, 2^32 - 1]
signed int s = -1; // (assuming 4 bytes) ranges from [-2^31, 2^31-1]

float f = 0.5; // 4 bytes, 6 decimal places
double d = 0.5; // 8 bytes, 15 decimal places
long double ld = 0.5; // 10 bytes, 19 decimal places

// NOTE: C does not support a boolean type

// This is not an exhaustive list of unions and structs, this is just a little taste

// This will be the size of int, since it is the bigger of the two
union TypeName {
	char x;
	int y;
} variable_name

// This will create a new struct with the type "struct StructName"
// yes, the "struct" is part of the type (making the type two words)
// we will se how to get around this with a typedef later
struct StructName {
	int x;
	char y;
};
// We can create an instance of the struct:
struct StructName instanceName = {5, 'a'};
// We can access the fields with:
instanceName.x = 7;
char y = instanceName.y;

// typedef allows us to rename types:
typedef struct WhatEverYouWantButKeepItTheSameAsStructName {
    int x;
    char y;
} StructName;
// and now we can:
StructName instanceName = {5, 'a'};

