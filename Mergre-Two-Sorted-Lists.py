# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2) -> ListNode:
        
        loc1 = list1
        loc2 = list2
        
        # new list
        head = curr = ListNode(0)

        while (loc1 and loc2):
        
            # if l1 node > l2 node push l2 node
            if (loc1.val > loc2.val):
                curr.next = loc2
                loc2 = loc2.next
                
            # else push l1 node
            else:
                curr.next = loc1
                loc1 = loc1.next

            curr = curr.next
        
        # push the remaining node
        curr.next = loc1 or loc2

        return head.next;
            

# make list 1
n1 = ListNode(1, None)
n2 = ListNode(2, None)
n3 = ListNode(4, None)

n1.next = n2
n2.next = n3

# make list 2
v1 = ListNode(1, None)
v2 = ListNode(3, None)
v3 = ListNode(4, None)

v1.next = v2
v2.next = v3

# TEST
sol = Solution()
r1 = sol.mergeTwoLists(n1, v1)

#print
temp = r1
while (temp.next):
    print(temp.val)
    temp = temp.next
print(temp.val)