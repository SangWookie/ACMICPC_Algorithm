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

    int a, b;
    cin >> a >> b;
    set<int> set_A;
    int input, elem = 0, common = 0;
    for (int i = 0; i < a; i++)
    {
        cin >> input;
        set_A.insert(input);
    }
    for (int i = 0; i < b; i++)
    {
        cin >> input;
        if (set_A.find(input) == set_A.end())
        {
            elem++;
        }
        else
        {
            common++;
        }
    }
    int answer = a - common + elem;
    cout << answer;
}
