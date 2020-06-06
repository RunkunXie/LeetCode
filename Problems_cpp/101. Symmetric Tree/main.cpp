//
//  main.cpp
//  101. Symmetric Tree
//
//  Created by vincent xie on 6/6/20.
//  Copyright © 2020 vincent xie. All rights reserved.
//

#include <iostream>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// my sol
class Solution {
public:
    
    bool dfs(TreeNode* left, TreeNode* right) {
        
        if (!left && !right)
            return true;
        else if (!left || !right)
            return false;
        else {
            return (left->val == right->val &&
                    dfs(left->left, right->right) &&
                    dfs(left->right, right->left));
        }
    }
    
    bool isSymmetric(TreeNode* root) {
        return root ? dfs(root->left, root->right) : true;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
