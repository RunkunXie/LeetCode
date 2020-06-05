//
//  main.cpp
//  50. Pow(x, n)
//
//  Created by vincent xie on 6/5/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my sol after hint
class Solution {
public:
    
    double fastPow(double x, long long N) {
        
        if (N == 0)
            return 1.0;
        
        if (N % 2 == 1)
            return x * fastPow(x*x, N / 2);
        else
            return fastPow(x*x, N / 2);
    }
    
    double myPow(double x, int n) {
        
        double ans;
        long long N = n;
         
        if (N < 0) {
            x = 1 / x;
            N = - N;
        }
        
        return fastPow(x, N);
        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
