#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    int num;

    if (a == b && b == c) // 3개가 모두 같을 때
    {
        num = 10000 + a * 1000;
    }
    else if (a == b || b == c || a == c) // 2개가 같을 때
    {
        if (a == b || a == c)
            num = 1000 + a * 100;
        else
            num = 1000 + b * 100;
    }
    else // 모두 다를 때
    {
        num = max(a, max(b, c)) * 100;
    }

    cout << num;
    return 0;
}
