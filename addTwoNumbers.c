struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* head = p;

    int carry = 0;
    while (l1 || l2 || carry) {
        if (l1) carry += l1->val, l1 = l1->next;
        if (l2) carry += l2->val, l2 = l2->next;
        p->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        p = p->next;
        p->val = carry % 10;
        p->next = NULL;
        carry /= 10;
    }

    return head->next;
}