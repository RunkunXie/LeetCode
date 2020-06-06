//
//  main.cpp
//  1466. Reorder Routes to Make All Paths Lead to the City Zero
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

// my bfs sol
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        
        int count = 0;
        deque<int> dq {};
        unordered_set<int> visited = {};
        unordered_map<int, unordered_set<int>> graph = {};
        
        for (auto c : connections) {
            graph[c[0]].insert(c[1]);
            graph[c[1]].insert(-c[0]);
        }
        
        dq.push_back(0);
        
        while (visited.size() != n) {
            
            // new node
            int curr = dq.front();
            dq.pop_front();
            visited.insert(curr);
            
            // bfs nearby node c
            for (auto c : graph[curr]) {
                
                // visited
                if (visited.find(abs(c)) != visited.end())
                    continue;
                
                // curr -> c, need reverse
                if (c > 0)
                    count++;
                
                dq.push_back(abs(c));
            }
        }
        
        return count;
    }
};

// online dfs sol
class Solution {
public:
    int dfs(vector<vector<int>> &al, vector<bool> &visited, int from) {
        auto change = 0;
        visited[from] = true;
        for (auto to : al[from])
            if (!visited[abs(to)])
                change += dfs(al, visited, abs(to)) + (to > 0);
        return change;
    }
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<int>> al(n);
        for (auto &c : connections) {
            al[c[0]].push_back(c[1]);
            al[c[1]].push_back(-c[0]);
        }
        return dfs(al, vector<bool>(n) = {}, 0);
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
