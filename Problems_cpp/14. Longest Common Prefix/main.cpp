//
//  main.cpp
//  14. Longest Common Prefix
//
//  Created by vincent xie on 6/5/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        

        string ans = "";
        int cur_len = 0, min_len = INT_MAX;
        
        if (strs.size() == 0)
            return ans;
        
        for (auto s : strs) {
            int tmp_len = s.size();
            min_len = min(min_len, tmp_len);
        }
        
        if (min_len == 0)
            return ans;
        
        while (cur_len < min_len) {
            
            bool common = true;
            char c = strs[0][cur_len];
            
            for (auto s : strs) {
                if (s[cur_len] != c)
                    common = false;
            }
            
            if (common)
                ans += c;
            else
                break;
            
            cur_len++;
        }
        
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    
    Solution s;
    
    vector<string> strs = {
        "flower","flow","flight"
    };
    cout << s.longestCommonPrefix(strs) << endl;
    
    return 0;
}
