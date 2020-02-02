#include <iostream>
#include <cstdlib>
using namespace std;

int tam_vet(){
    int n;
    cout<<"Digite o tamanho do vetor: ";
    cin>>n;
    return n;
}

int main(){
    
    int n=tam_vet();
    int *vetor;
    vetor= new int [n];

    for(int i=0;i<n;i++){
        cin>>vetor[i];
    }
    cout<<endl;
    for(int a=0;a<n;a++){
        cout<<" - "<<vetor[a]<<endl;
    }

    system("pause");
    return 0;
}