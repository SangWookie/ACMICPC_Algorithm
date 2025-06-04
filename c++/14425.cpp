#include <iostream>
#include <set>
using namespace std;
int main()
{
    set<string> dict;
    int n, m, count = 0;
    string input;

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        cin >> input;
        dict.insert(input);
    }
    for (int i = 0; i < m; i++)
    {
        cin >> input;
        if (dict.find(input) != dict.end())
        {
            count++;
        }
    }
    cout << count;
}
// https://www.acmicpc.net/problem/14425