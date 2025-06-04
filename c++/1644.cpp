#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <numeric>
using namespace std;
void primeChecker(int n, vector<int> &primeArr)
{
    bool *isPrime = new bool[n + 1];
    for (int i = 0; i < n + 1; i++)
    {
        isPrime[i] = true;
    }
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= n + 1; i++)
    {
        if (isPrime[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                isPrime[j] = false;
            }
        }
    }
    for (int i = 2; i <= n; i++)
    {
        if (isPrime[i])
        {
            primeArr.push_back(i);
        }
    }
    delete isPrime;
}

int main()
{
    int n, ans = 0;
    cin >> n;
    vector<int> primeArr;

    primeChecker(n, primeArr);
    sort(primeArr.rbegin(), primeArr.rend());

    if (primeArr.size() == 0) // 예외처리
    {
        cout << 0;
        return 0;
    }

    for (int i = 0; i < primeArr.size(); i++)
    {
        int sum = 0;
        for (int j = i; j < primeArr.size(); j++)
        {
            sum += primeArr[j];
            if (sum == n)
            {
                ans++;
            }
            else if (sum > n)
            {
                break;
            }
        }
    }

    cout << ans;
}