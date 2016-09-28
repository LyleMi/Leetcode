struct ListNode* reverseList(struct ListNode* head) {
    if(!head || !head->next) return head;
    struct ListNode* t0 = head;
    struct ListNode* t1 = head->next;
    head->next = NULL;
    while(t1->next != NULL){
        t0 = t1->next;
        t1->next = head;
        head = t1;
        t1 = t0;
        t0 = head;
    }
    t1->next = t0;
    return t1;
}