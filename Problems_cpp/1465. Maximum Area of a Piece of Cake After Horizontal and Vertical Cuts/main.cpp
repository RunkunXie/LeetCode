//
//  main.cpp
//  1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my sol time nmlognlogm
class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());


        double max_h = horizontalCuts[0], max_w = verticalCuts[0];
        
        for (int i = 1; i < horizontalCuts.size(); i++)
            max_h = max(max_h, (double) horizontalCuts[i] - horizontalCuts[i - 1]);
        for (int j = 1; j < verticalCuts.size(); j++)
            max_w = max(max_w, (double) verticalCuts[j] - verticalCuts[j - 1]);
        
        max_h = max(max_h, (double) h - horizontalCuts.back());
        max_w = max(max_w, (double) w - verticalCuts.back());
        
        int ans = fmod((max_h * max_w), (pow(10, 9) + 7));
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
