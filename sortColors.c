#define swap(x,y) if((x)!=(y)) (x)^=(y),(y)^=(x),(x)^=(y)

void sortColors(int* A, int n) {
    int second=n-1, zero=0;
    for (int i=0; i<=second; i++) {
        while (A[i]==2 && i<second) {swap(A[i], A[second]);second--;}
        while (A[i]==0 && i>zero) {swap(A[i], A[zero]);zero++;}
    }
}