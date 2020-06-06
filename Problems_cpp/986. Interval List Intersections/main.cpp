//
//  main.cpp
//  986. Interval List Intersections
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my sol
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        
        vector<vector<int>> ans = {};
        int m = A.size(), n = B.size();
        int start_j = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = start_j; j < n; j++) {
                
                // B too left
                if (B[j][1] < A[i][0]) {
                    start_j++;
                    continue;
                }
                
                // B too right
                else if (A[i][1] < B[j][0]) {
                    break;
                }
                
                // just right
                else {
                    vector<int> cur = {max(A[i][0], B[j][0]),
                                       min(A[i][1], B[j][1])};
                    ans.push_back(cur);
                }
            }
        }
    
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
