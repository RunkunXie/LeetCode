//
//  main.cpp
//  1029. Two City Scheduling
//
//  Created by vincent xie on 6/3/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std; // using sort, vector

class Solution {
public:
    // ans
    int twoCitySchedCost(vector<vector<int>>& costs) {
        // Sort by a gain which company has
        // by sending a person to city A and not to city B
        sort(begin(costs), end(costs),
             [](const vector<int> &o1, const vector<int> &o2) { // lambda expression
          return (o1[0] - o1[1] < o2[0] - o2[1]);
        });

        int total = 0;
        int n = costs.size() / 2;
        for (int i = 0; i < n; ++i)
            total += costs[i][0] + costs[i + n][1];
        return total;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
