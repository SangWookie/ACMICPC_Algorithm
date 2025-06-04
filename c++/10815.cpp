#include <iostream>
#include <set>
using namespace std;
int main()
{
    int n, m;
    cin >> n;
    set<int> cards;

    for (int i = 0; i < n; i++)
    {
        int input;
        cin >> input;
        cards.insert(input);
    }
    cin >> m;
    int *compare = new int[m];
    int *answer = new int[m];
    for (int i = 0; i < m; i++)
    {
        cin >> compare[i];
    }
    for (int i = 0; i < m; i++)
    {
        if (cards.find(compare[i]) != cards.end())
        {
            answer[i] = 1;
        }
        else
        {
            answer[i] = 0;
        }
    }
    for (int i = 0; i < m; i++)
    {
        cout << answer[i] << " ";
    }
}
// https://www.acmicpc.net/problem/10815