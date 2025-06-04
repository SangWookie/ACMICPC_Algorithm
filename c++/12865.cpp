#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <queue>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> obj;
    for (int i = 0; i < n; i++)
    {
        int inputW, inputV;
        cin >> inputW >> inputV;
        obj.push_back(make_pair(inputW, inputV));
    }

    // k행 n열의 2차원 배열을 만들어서 dp
    int **knapsack = new int *[k + 1];
    for (int i = 0; i < k + 1; i++)
    {
        knapsack[i] = new int[n + 1];
    }

    // 첫 번째 열과 첫 번째 행 0으로 초기화
    for (int i = 0; i < k + 1; i++)
    {
        knapsack[i][0] = 0;
    }
    for (int j = 0; j < n + 1; j++)
    {
        knapsack[0][j] = 0;
    }

    for (int j = 1; j < n + 1; j++)
    {
        int weight = obj[j - 1].first;
        int value = obj[j - 1].second;

        for (int i = 1; i < k + 1; i++)
        {
            if (weight > i)
            {
                knapsack[i][j] = knapsack[i][j - 1];
            }
            else
            { // max(knapsack[i-weight][j-1]+value, knapsack[i][j-1])
                if (knapsack[i - weight][j - 1] + value > knapsack[i][j - 1])
                {
                    knapsack[i][j] = knapsack[i - weight][j - 1] + value;
                }
                else
                {
                    knapsack[i][j] = knapsack[i][j - 1];
                }
            }
        }
    }
    // for (int j = 1; j < n + 1; j++)
    // {
    //     for (int i = 1; i < k + 1; i++)
    //     {
    //         cout << knapsack[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    cout << knapsack[k][n];
}