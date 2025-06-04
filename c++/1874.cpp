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

    int n;
    cin >> n;
    int *arr = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    stack<int> S;
    list<char> output;
    int in = 1, it = 0;

    while (in != n + 2)
    {
        if (!S.empty() && S.top() == arr[it])
        {
            it++;
            S.pop();
            output.push_back('-');
        }
        else
        {
            S.push(in);
            in++;
            if (in != n + 2)
                output.push_back('+');
        }
    }
    if (output.size() == (long long unsigned)n * 2)
        for (char ptr : output)
        {
            cout << ptr << "\n";
        }
    else
        cout << "NO";
}
