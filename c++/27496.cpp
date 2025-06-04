#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    const int alc_low = 129;
    const int alc_high = 138;
    int n, l;
    cin >> n >> l;
    int *a = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    queue<int> q;
    int total = 0;
    int max = 0;
    for (int i = 0; i < n; i++)
    {
        if (q.size() == (long long unsigned int)l)
        {
            total -= q.front();
            q.pop();
        }
        q.push(a[i]);
        total += a[i];

        if (total >= alc_low && total <= alc_high)
        {
            max++;
        }
    }

    cout << max;
    delete a;
}
