#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <unordered_map>
#include <string>
#include <stack>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m, k;
    cin >> n >> m >> k;
    if (k < n + m - 1)
    {
        cout << "NO";
        return 0;
    }

    vector<vector<int>> arr;
    for (int i = 0; i < n; i++)
    {
        vector<int> element(m);
        arr.push_back(element);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            arr[i][j] = i + j + 1;
        }
    }

    cout << "YES\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}
