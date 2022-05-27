// Online C++ compiler to run C++ program online
#include <iostream>

int main() {
    // Write C++ code here
    int N = 4;
    int h[N] = [1, 4, 2, 4];
    int result[N];
    for (int i = 0; i < N; i++) {
        int compare[N];
        for (int j = 0; j < N; j++) {
            int cost = h[j];
            int fee;
            if (i = j) {
                fee = 0;
            } else {
                fee = abs(j - i);
            }
            compare.push_back(cost + fee);
        }
        result.push_back(min(compare))
    }
    std::cout << result;
    std::cout << "Hello world!";

    return 0;
}