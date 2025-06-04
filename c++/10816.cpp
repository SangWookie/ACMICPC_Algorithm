#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n;
    unordered_map<int, int> cards;
    vector<int> inputs;
    for (int i = 0; i < n; i++)
    {
        int input;
        cin >> input;
        inputs.push_back(input);
        cards.insert({input, 0});
    }
    for (int i = 0; i < n; i++)
    {
        cards[inputs[i]]++;
    }

    cin >> m;
    vector<int> compare;
    for (int i = 0; i < m; i++)
    {
        int input;
        cin >> input;
        compare.push_back(input);
        printf("%d ", cards[input]);
    }
}

// https://www.acmicpc.net/problem/10816