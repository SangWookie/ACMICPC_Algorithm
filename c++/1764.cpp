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

    int n, m;
    cin >> n >> m;
    set<string> listen;
    vector<string> unknown;
    string input;
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        listen.insert(input);
    }
    for (int i = 0; i < m; i++)
    {
        cin >> input;
        if (listen.find(input) != listen.end())
        {
            unknown.push_back(input);
        }
    }

    sort(unknown.begin(), unknown.end());
    cout << unknown.size() << "\n";
    for (auto it = unknown.begin(); it < unknown.end(); it++)
    {
        cout << *it << "\n";
    }
}
