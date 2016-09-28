struct TreeNode* invertTree(struct TreeNode* root) {
    if(!root) return 0;
    if(root->left) invertTree(root->left);
    if(root->right) invertTree(root->right);
    struct TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;
}