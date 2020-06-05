//
//  main.cpp
//  GTS Practice
//
//  Created by vincent xie on 6/4/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <deque>

using namespace std;

vector<vector<int>> findDecreasingSeq(vector<int> &v) {
        
    vector<vector<int>> ans = {};

    int n = v.size();
    if (n < 3)
        return {};
    
    for (int i = 0; i < n - 2; i++) {
        vector<int> cur = {v[i]};
        for (int j = i + 1; j < n - 1; j++) {
            if (v[j] < v[i]) {
                cur.push_back(v[j]);
                for (int k = j + 1; k < n; k++) {
                    if (v[k] < v[j]) {
                        cur.push_back(v[k]);
                        ans.push_back(cur);
                        cur.pop_back();
                    }
                }
                cur.pop_back();
            }
        }
    }
    
    return ans;
}

void print2DVector (vector<vector<int>> &v) {
    for (auto it : v) {
        for (auto it2 : it) {
            cout << it2 << " ";
        }
        cout << endl;
    }
}

int main() {

    vector<int> v1 = {7,5,12,3,1};
    auto ans1 = findDecreasingSeq(v1);
    print2DVector(ans1); // 7 5 3, 7 5 1, 5 3 1, 12 3 1

    return 0;
}
