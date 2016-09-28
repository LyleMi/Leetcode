/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(!root) return 0;
    int a=maxDepth(root->left);
    int b=maxDepth(root->right);
    return (((a>b)?a:b)+1); 
}