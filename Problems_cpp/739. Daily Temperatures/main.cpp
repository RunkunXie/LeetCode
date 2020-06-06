//
//  main.cpp
//  739. Daily Temperatures
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        
        int n = T.size();
        vector<int> ans (n, 0);
        vector<int> dq = {};
        
        for (int i = 0; i < n; i++) {
            
            // deque push
            while (!dq.empty() && T[i] > T[dq.back()]) {
                ans[dq.back()] = i - dq.back();
                dq.pop_back();
            }
            dq.push_back(i);
            
        }
        
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
