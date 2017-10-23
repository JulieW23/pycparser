int sum (int *a, int n) {
    int sum = 0;

    for(int i = 0; i < n; i = i + 1) {
        sum = sum +  a[i];
    }
    return sum;
}

int max_init_sum (int *a, int n) {
    int mis;
    int i = 0;
    for( i = 0; i < n; i++) {
        mis = max(mis, sum(a, i));
    }

    return mis;
}

int main(int argc, char** argv) {
    int* a;
    int n;
    n = 1000;
    a = malloc(1000 * sizeof(int));
    return sum(a, 1000);
}

