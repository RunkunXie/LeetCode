//
//  main.cpp
//  668. Kth Smallest Number in Multiplication Table
//
//  Created by vincent xie on 6/3/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    bool enough(int num, int k, int m, int n) {
            int count = 0;
            for (int i = 1; i <= m; i++) {
                count += min(num / i, n);
            }
            return count >= k;
        }
    
    int findKthNumber(int m, int n, int k) {
        
        int start = 1, end = m * n;
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (enough(mid, k, m, n))
                end = mid;
            else
                start = mid + 1;
        }
        
        return start;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
