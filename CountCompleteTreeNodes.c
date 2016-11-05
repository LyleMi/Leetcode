// first version

int height(struct TreeNode* root) {
    return root ? 1 + height(root->left) : -1;
}

int countNodes(struct TreeNode* root) {
    int h = height(root);
    return h < 0 ? 0 :
           height(root->right) == h - 1 ? (1 << h) + countNodes(root->right)
           : (1 << h - 1) + countNodes(root->left);
}

// second version

int countNodes(struct TreeNode* root) {

    if (!root) return 0;
    int hl = 0, hr = 0;
    struct TreeNode *l = root, *r = root;

    while (r) {
        hr++;
        r = r->right;
        l = l->left;
    }
    hl = hr;
    while (l) {hl++; l = l->left;}
    if (hl == hr) return (1 << hl) - 1;

    return 1 + countNodes(root->left) + countNodes(root->right);
}

// third

int countNodes(struct TreeNode* root) {
    if (!root) return 0;
    int height = 0, sum = 0, i = 0;
    struct TreeNode *t = root, *t0 = NULL;
    while (t) t = t->left, height++; //get the height of the tree;
    t = root;
    int level = height - 2; //levels under the child of root;
    while (level > -1) //collect the bottom-level nodes by halving them apart;
    {
        t0 = t->left;
        for (i = 0; i < level; ++i) t0 = t0->right;
        if (t0) { sum += 1 << level; t = t->right; } //rightmost node is not null;
        else t = t->left;
        level--; //move to the next level;
    }
    if (t) sum++; //if it's a complete tree, collect the last right node;
    return sum + ((1 << (height - 1)) - 1);
}