# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 리스트 노드
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        arr1 = []
        arr2 = []

        while l1 != None:
            arr1.append(str(l1.val))
            l1 = l1.next

        while l2 != None:
            arr2.append(str(l2.val))
            l2 = l2.next

        self.reverse(arr1)
        self.reverse(arr2)
        
        num1 = int("".join(arr1))
        num2 = int("".join(arr2))

        num_result = num1 + num2
        str_result = str(num_result)
        temp = list(str_result)
        self.reverse(temp)
        # print(temp)

        answer = self.recursive(temp, 0)
        # print(answer)

        return answer        

    def reverse(self, arr):
        i = 0
        j = len(arr) - 1

        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    
    def recursive(self, arr, i):
        if i == len(arr) - 1:
            return ListNode(int(arr[i]), None)

        child = self.recursive(arr, i + 1)
        return ListNode(int(arr[i]), child)

    