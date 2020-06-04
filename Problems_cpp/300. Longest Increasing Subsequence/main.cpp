//
//  main.cpp
//  300. Longest Increasing Subsequence
//
//  Created by vincent xie on 6/4/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // my sol under hint, time n^2
    int lengthOfLIS(vector<int>& nums) {
        
        int n = nums.size();
        if (n == 0)
            return 0;
        
        vector<int> dp (n, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j])
                    dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        
        return *max_element(dp.begin(), dp.end());
    }
    
    // follow up: bisect time nlogn ans
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << INT_MAX;
    return 0;
}
