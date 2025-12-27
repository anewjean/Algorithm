public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;        // 한 칸
            fast = fast.next.next;   // 두 칸

            if (slow == fast) {      // cycle 존재
                return true;
            }
        }

        return false; // 빠른 포인터가 끝에 도달 → cycle 없음
    }
}
