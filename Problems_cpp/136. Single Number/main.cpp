//
//  main.cpp
//  136. Single Number
//
//  Created by vincent xie on 5/29/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream> 
#include <vector>
using namespace std;

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

int main() {
    
    Solution s;
    vector<int> v = {1,1,2,2,3,3,4,5,5};
    
    cout << s.singleNumber(v) << endl;
    
};

