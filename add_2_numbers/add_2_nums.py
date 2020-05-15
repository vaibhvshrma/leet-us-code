class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    res = ListNode(0)
        
    head = res
    
    sm, cr = 0, 0
    
    while l1 and l2:
        res.val += l1.val + l2.val
        
        if res.val >= 10:
            res.val %= 10
            cr = 1
        else:
            cr = 0
        
        if l1.next is not None or l2.next is not None or cr:
            res.next = ListNode(cr)
        else:
            res.next = None
            
        res = res.next
        l1 = l1.next
        l2 = l2.next
            
    while l1 is not None:
        res.val += l1.val
        if l1.next:
            res.next = ListNode(0)
            res = res.next
        l1 = l1.next
        
    while l2:
        res.val += l2.val
        if l2.next:
            res.next = ListNode(0)
            res = res.next
        l2 = l2.next
        
    return head

def makeList(lst):
    ptr = ListNode(0)
    head = ptr

    for i in range(len(lst)-1):
        ptr.val = lst[i]
        ptr.next = ListNode(0)
        ptr = ptr.next
    
    ptr.val = lst[-1]
    ptr.next = None

    return head

def printList(l):
    while l:
        print(l.val, end = " ")
        l = l.next

def main():
    l1 = makeList(list(map(int, input().split())))
    l2 = makeList(list(map(int, input().split())))

    res = addTwoNumbers(l1, l2)

    printList(res)

if __name__ == '__main__':
    main()