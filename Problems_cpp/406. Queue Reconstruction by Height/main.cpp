//
//  main.cpp
//  406. Queue Reconstruction by Height
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my sol
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        
        sort(people.begin(), people.end(), [](vector<int> v1, vector<int> v2) {
            if (v1[0] > v2[0])
                return true;
            else if (v1[0] == v2[0] && v1[1] < v2[1])
                return true;
            return false;
        });
            
        vector<vector<int>> ans = {};
        for (auto p : people) {
            ans.insert(ans.begin() + p[1], p);
        }
        
        return ans;
    }
};

// ans
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        
        sort(people.begin(), people.end(), [](vector<int> v1, vector<int> v2) {
            return v1[0] == v2[0] ? v1[1] < v2[1] : v1[0] > v2[0];
        });
            
        vector<vector<int>> ans = {};
        for (auto p : people) {
            ans.insert(ans.begin() + p[1], p);
        }
        
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    
    
    return 0;
}
