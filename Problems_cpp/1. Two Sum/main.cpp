//
//  main.cpp
//  1. Two Sum
//
//  Created by vincent xie on 6/1/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> m;
        vector<int> ans = {};
        
        for (int i = 0; i < nums.size(); i++) {
            
            // not find
            if (m.find(target - nums[i]) == m.end())
                m[nums[i]] = i;
            
            // element find
            else {
                ans.push_back(i);
                ans.push_back(m[target - nums[i]]);
                break;
            }
        }
        
        return ans;
    }
};

int main() {

    Solution s;
    vector<int> v = {1,2,3,4,5,6,8,11,12};
    int t = 10;
    
    vector<int> ans = s.twoSum(v, t);
    for (auto it = ans.begin(); it != ans.end(); it++) {
        cout << *it << ' ';
    }
    cout << endl;
};

