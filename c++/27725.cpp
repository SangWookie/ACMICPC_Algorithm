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
    long long int k;
    cin >> n;
    int *p = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    cin >> k;
    long long int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        int prime = p[i];
        long long int power_num = prime;
        while (power_num <= k)
        {
            cnt += k / power_num;
            power_num *= prime;
        }
    }
    cout << cnt;
    return 0;
}
