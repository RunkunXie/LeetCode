//
//  main.cpp
//  1128. Number of Equivalent Domino Pairs
//
//  Created by vincent xie on 6/4/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

class Solution {
public:
    // my sol, time n^2
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        
        int ans = 0, n = dominoes.size();
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j ++) {
                if ((dominoes[i][0] == dominoes[j][0] &&
                     dominoes[i][1] == dominoes[j][1]) ||
                    (dominoes[i][0] == dominoes[j][1] &&
                     dominoes[i][1] == dominoes[j][0]))
                    ans += 1;
            }
        }
        
        return ans;
    }

    // my sol, string:int map, time n
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        
        int ans = 0, n = dominoes.size();
        unordered_map<string, int> m;
        
        for (int i = 0; i < n; i++) {
            string s = to_string(min(dominoes[i][0], dominoes[i][1])) + "_" + to_string(max(dominoes[i][0], dominoes[i][1]));
            if (m.find(s) != m.end())
                ans += ++m[s];
            else
                m[s] = 0;
        }
        
        return ans;
    }
    
    // online sol, hash function int:int, time n
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        
        unordered_map<int, int> count;
        int res = 0;
        for (auto& d : dominoes) {
            res += count[min(d[0], d[1]) * 10 + max(d[0], d[1])]++;
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
