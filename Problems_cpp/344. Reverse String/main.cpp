//
//  main.cpp
//  344. Reverse String
//
//  Created by vincent xie on 6/4/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    void reverseString(vector<char>& s) {
        
        int n = s.size();
        
        int start = 0, end = n - 1;
        while (start < end) {
            char c = s[start];
            s[start] = s[end];
            s[end] = c;
            
            start++;
            end--;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
