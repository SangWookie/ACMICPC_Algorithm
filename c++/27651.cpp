#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int *a = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    long long int *sum = new long long int[n];
    sum[0] = a[0];
    for (int i = 1; i < n; i++)
    {
        sum[i] = a[i] + a[i - 1];
    }

    long long int head, thorax, abdomen;
}
