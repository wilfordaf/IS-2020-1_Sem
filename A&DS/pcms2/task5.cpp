#include <iostream>
#include <fstream>
using namespace std;

void qsort(long* arr, long first, long last, long k)
{
    if (k >= first && k <= last)
    {
        int pivotnum = (first+last) / 2;
        long pivot = arr[pivotnum];
        int i = first;
        int j = last;
        while (i <= j)
        {
            while (arr[i] < pivot && i <= last) i++;
            while (arr[j] > pivot && j >= first) j--;
            if (i <= j)
            {
                long t = arr[j];
                arr[j] = arr[i];
                arr[i] = t;
                i++;
                j--;
            }
        }
        if (j > first) qsort(arr, first, j, k);
        if (i < last) qsort(arr, i, last, k);
    }
}

int main()
{
    ifstream fin("kth.in");
    ofstream fout("kth.out");
    long n, k, A, B, C, a1, a2;
    fin >> n >> k >> A >> B >> C >> a1 >> a2;
    long* a = new long[n];
    a[0] = a1;
    a[1] = a2;
    for(int i = 2; i < n; i++)
    {
        a[i] = A * a[i - 2] + B * a[i - 1] + C;
    }
    qsort(a, 0, n-1, k-1 );
    fout << a[k-1];
    fin.close();
    fout.close();
    return 0;
}
