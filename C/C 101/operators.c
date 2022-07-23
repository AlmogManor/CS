// Arithmatic:
int a = 1;
int b = 2;

int c;
c = a + b; // addition
c = a - b; // subtraction
c = a * b; // multiplication
c = a / b; // division
// keep in mind: division infers the type from the left operand, meaning:
int x = 5;
int y = 2;
float z = 2.5f;

x / y // will be 2 (int)
x / z // will be 2 (int)
z / x // will be 0.5f (float)

c = a % b; // modulus (returns the remainder from division)

a++; // a = a + 1
a--; // a = a - 1

c = a++; // c = a; Then do a = a + 1
c = ++a; // a = a + 1; Then do c = a


// Bitwise operators
char x = 0b00000001;
char y = 0b00000010;
char z;

z = x | y; // OR, z = 0b00000011

x = 0b00000011;
y = 0b00000001;
z = x & y; // AND, z = 0b00000001

z = x ^ z; // XOR, z = 0b00000010

z = !x; // NOT, z = 0b11111100

z = x << 2; // bit shifting, z = 0b00001100
z = x >> 1; // bit shifting the other way

// All of the operators mentioned above also work with =
a += b; // a = a + b
z |= y; // z = z | y
