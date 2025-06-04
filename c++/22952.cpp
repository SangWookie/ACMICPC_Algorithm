#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int *a = new int[n];
    int mid;
    int dif = 0;
    if (n % 2 == 0)
        mid = n / 2;
    else
        mid = n / 2 + 1;

    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            a[i] = mid + dif++;
        }
        else
        {
            a[i] = mid - dif;
        }
    }
    if (n % 2 == 0)
        a[n - 1] = n;

    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
}
