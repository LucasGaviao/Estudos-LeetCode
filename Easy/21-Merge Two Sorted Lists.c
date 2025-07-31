#include <stdio.h>
struct ListNode {
    int val;
    struct ListNode *next;
 };

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (!list1) return list2;
    if (!list2) return list1;

    struct ListNode merge;
    struct ListNode *ref = &merge;
    merge.next = NULL;

    while (list1 && list2){
        if (list1->val <= list2->val){
            ref->next = list1;
            list1 = list1->next;    
        } else {
            ref->next = list2;
            list2 = list2->next;
        }
        ref = ref->next;
    } 

    ref->next = (list1? list1:list2);

    return merge.next;
}