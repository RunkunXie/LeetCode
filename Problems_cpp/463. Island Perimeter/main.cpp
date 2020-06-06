//
//  main.cpp
//  463. Island Perimeter
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my dfs sol, time n*m, complex but could expand to multiple islands situation
class Solution {
public:
    
    int dfs(vector<vector<int>>& grid, int i, int j, int ans) {
        
        // check i, j within grid, and grid[i][j] == 1
        int m = grid.size(), n = grid[0].size();
        if (!(0 <= i && i < m && 0 <= j && j < n))
            return ans;
        if (grid[i][j] != 1)
            return ans;
        
        // 4 directions
        vector<vector<int>> direct = {
            {-1, 0}, {0, 1}, {1, 0}, {0, -1}
        };
        
        // add current block to ans
        int connect = 0;
        for (auto d : direct) {
            int newi = i + d[0], newj = j + d[1];
            if (0 <= newi && newi < m && 0 <= newj && newj < n) {
                if (grid[newi][newj] == 2)
                    connect++;
            }
        }
        ans = ans + (4 - connect * 2);
        grid[i][j] = 2;
        
        // dfs 4 directions
        for (auto d : direct) {
            ans = dfs(grid, i + d[0], j + d[1], ans);
        }
        
        return ans;
    }
    
    int islandPerimeter(vector<vector<int>>& grid) {
        
        int ans = 0;
        int m = grid.size(), n = grid[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    ans = dfs(grid, i, j, ans);
                    break;
                }
            }
        }
        
        return ans;
    }
};

// my sol after online hint, time n*m
class Solution {
public:
    
    int islandPerimeter(vector<vector<int>>& grid) {
        
        int ans = 0, repeat = 0;
        int m = grid.size(), n = grid[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    ans++;
                    if (i > 0 and grid[i - 1][j] == 1) repeat++;
                    if (j > 0 and grid[i][j - 1] == 1) repeat++;
                }
            }
        }
        
        return 4 * ans - repeat * 2;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
