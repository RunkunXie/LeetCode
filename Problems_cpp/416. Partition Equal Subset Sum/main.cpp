//
//  main.cpp
//  416. Partition Equal Subset Sum
//
//  Created by vincent xie on 6/4/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    // """my sol, time n^2"""
    bool canPartition(vector<int>& nums) {
        
        int n = nums.size();
        int acc = accumulate(nums.begin(), nums.end(), 0);
        if (acc % 2 == 1)
            return false;
        int target = acc / 2;
        
        unordered_set<int> available = {0};
        for (auto num : nums) {
            unordered_set<int> ava(available);
            for (auto a : ava) {
                if (available.find(a + num) == available.end())
                    available.insert(a + num);
            }
            
            if (available.find(target) != available.end())
                return true;
        }
        
        return false;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
