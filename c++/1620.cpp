#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

string books_rev[100001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    string input;
    unordered_map<string, int> books;

    cin >> n >> m;
    for (int i = 0; i < n; i++) // 입력
    {
        cin >> input;
        books.insert({input, i + 1}); // 문자로 숫자를 찾기 위한 unordered map
        books_rev[i + 1] = input;     // 숫자로 문자를 찾기 위한 배열
    }
    for (int i = 0; i < m; i++)
    {
        cin >> input;
        if (input[0] >= '0' && input[0] <= '9') // 입력이 숫자인지 판별
        {
            int iter = stoi(input);
            cout << books_rev[iter] << '\n'; // 숫자로 문자찾기
        }
        else
        {
            cout << books.find(input)->second << '\n'; // 문자로 숫자찾기
        }
    }
}
// https://www.acmicpc.net/problem/1620