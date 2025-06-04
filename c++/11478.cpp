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

    string input, tmp;
    set<string> sub_string;
    cin >> input;
    for (int i = 1; i <= input.size(); i++)
    {
        for (int j = 0; j < input.size() - i + 1; j++)
        {
            tmp = input.substr(j, i);
            sub_string.insert(tmp);
        }
    }
    cout << sub_string.size();
}
