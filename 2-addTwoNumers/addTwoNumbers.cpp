struct ListNode {
int val;
ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = new ListNode(0);
        ListNode* current = temp;
        int carry = 0;
        while(l1 || l2 || carry !=0){
            int n1 = l1 ? l1->val: 0;
            int n2 = l2 ? l2->val: 0;
            int suma = carry + n1 + n2;
            carry = suma/10;
            current->next = new ListNode(suma%10);
            current = current->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        ListNode* resultado = temp->next;
        return resultado;
    }
};