//
//  main.cpp
//  136. Single Number
//
//  Created by vincent xie on 5/29/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        
        int ans = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            ans ^= nums[i];
        }
        
        return ans;
    }
};
