//
//  main.cpp
//  74. Search a 2D Matrix
//
//  Created by vincent xie on 6/3/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        if (matrix.size() == 0)
            return false;
        if (matrix[0].size() == 0)
            return false;
            
        int m = matrix.size();
        int n = matrix[0].size();
        int start = 0;
        int end = m * n - 1;
        int mid;
        int i, j;
        
        while (start <= end) {
            mid = start + (end - start) / 2;
            i = mid / n;
            j = mid % n;
            if (matrix[i][j] == target)
                return true;
            else if (matrix[i][j] > target)
                end = mid - 1;
            else
                start = mid + 1;
        }
        
        return false;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
