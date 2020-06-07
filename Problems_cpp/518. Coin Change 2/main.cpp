//
//  main.cpp
//  518. Coin Change 2
//
//  Created by vincent xie on 6/7/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my sol
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        
        int n = coins.size();
        
        vector<int> dp (amount + 1);
        dp[0] = 1;
        
        for (auto c : coins) {
            for (int i = 1; i < amount + 1; i++) {
                if (i - c >= 0)
                    dp[i] += dp[i - c];
            }
        }
        
        return dp[amount];
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
