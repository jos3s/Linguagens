#include <iostream>
#include <cmath>
#include <stdlib.h>

using namespace std;
#define PI 3.14

int main(){
    int raio;
    float area, perim;

    cout <<"Digite o valor do raio:"<<endl;
    cin >> raio;

    perim=2*PI*raio;
    area=PI*pow(raio,2);

    cout<<"O perimetro tem :"<<perim<< " metros" <<endl;
    cout<<"A área tem :"<<area<< " metros" <<endl;

    system("pause");
    return 0;
} 