//
//  main.cpp
//  34. Find First and Last Position of Element in Sorted Array
//
//  Created by vincent xie on 6/2/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
        if (nums.size() == 0)
            return {-1, -1};
        
        int start = 0;
        int end = nums.size() - 1;
        int mid;
        
        int left = -1;
        int right = -1;
        
        // find right
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (nums[mid] <= target)
                start = mid;
            else
                end = mid;
        }
        
        if (nums[end] == target)
            right = end;
        else if (nums[start] == target)
            right = start;
        else
            return {left, right};
        
        // find left
        start = 0;
        end = nums.size() - 1;
        
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (nums[mid] >= target)
                end = mid;
            else
                start = mid;
        }
        
        if (nums[start] == target)
            left = start;
        else if (nums[end] == target)
            left = end;
        
        return {left, right};
        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
