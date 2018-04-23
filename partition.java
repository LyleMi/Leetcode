class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode less = new ListNode(0);
        ListNode greater = new ListNode(0);
        ListNode curLess = less;
        ListNode curGreater = greater;
        while (head != null) {
            if (head.val < x) {
                curLess.next = head;
                curLess = head;
            } else {
                curGreater.next = head;
                curGreater = head;
            }
            head = head.next;
        }
        curGreater.next = null;
        curLess.next = greater.next;
        return less.next;
    }
}
