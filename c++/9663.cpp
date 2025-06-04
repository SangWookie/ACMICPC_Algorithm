#include <iostream>
#include <stack>
using namespace std;

void mark(int arr[15][15], pair<int, int> queen, int n)
{
    int c = queen.first;
    int r = queen.second;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (c == i || r == j || c + r == i + j || abs(c - r) == abs(i - j))
            {
                arr[i][j]++;
            }
        }
    }
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    stack<pair<int, int>> S;
    cin >> n;
    int board[15][15] = {0};
    int cnt = 0;

    // mark(board, 0, 0, n);

    // check if the place is available
    // push to stack
    // pop and go next row , if last row count
    int i = 0, j = 0;
    for (int i = 0; i < n; i++)
    {
        S.push(make_pair(0, i));
    }

    while (!S.empty())
    {
        pair<int, int> now = S.top();
        if (now.first == n - 1)
            cnt++;
        else
            mark(board, now, n);
    }
}