int minDepth(struct TreeNode* root) {
    if(!root) return 0;
    int l = minDepth(root->left);
    int r = minDepth(root->right);
    return ( ( !l || !r ) ? ( l + r ) : ( l > r ? r : l ) ) + 1;
}