/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;
        while ((curr != null) && (curr.next != null)) {
            if (curr.next.val == curr.val) { // 중복일 때는 다음 포인터를 다음다음 포인터로 연결시켜서 다음 포인터 삭제
                curr.next = curr.next.next;
            } else {
                curr = curr.next; // 중복 아닐 때만 현재 포인터를 다음으로 이동
            }
        }
        return head;
    }
}
