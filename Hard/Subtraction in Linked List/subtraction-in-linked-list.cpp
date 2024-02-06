//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// Node Class
class Node {
public:
    int data;
    Node* next;

    Node(int val) : data(val), next(NULL) {}
};

// Linked List Class
class LinkedList {
public:
    Node* head;
    Node* tail;

    LinkedList() : head(NULL), tail(NULL) {}

    // creates a new node with given value and appends it at the end of the linked list
    void insert(int val) {
        if (head == NULL) {
            head = new Node(val);
            tail = head;
        } else {
            tail->next = new Node(val);
            tail = tail->next;
        }
    }
};


// } Driver Code Ends
//User function Template for C++

class Solution {
public:
   Node* reverseList(Node* head) {
        if(head == NULL || head->next == NULL)
        {
            return head;
        }
        Node* prev = NULL;
        Node* current = head;
        Node* next = current->next;
        while(current!=NULL)
        {
            current->next = prev;
            prev = current;
            current = next;
            if(next!=NULL)
            {
                next = next->next;
            }
        }
        head = prev;
        return head;
   }
   int length(Node* head){
       int len = 0;
       while(head){
           len++;
           head = head->next;
       }
       return len;
   }
    Node* subLinkedList(Node* head1, Node* head2) {
        // Your implementation of subLinkedList goes here
        // Make sure to return the head of the resulting linked list
        //eliminating 0's
        while(head1 && head1->data == 0){
            head1 = head1->next;
        }
        while(head2 && head2->data == 0){
            head2 = head2->next;
        }
        
        if(!head1 && !head2){
            Node* head = new Node(0);
            return head;
        }
        
        int n1 = length(head1);
        int n2 = length(head2);
        if(n2>n1){
            swap(head1,head2);
        }
        if(n1 == n2){
            Node* temp1 = head1,*temp2 = head2;
            while(temp1->data == temp2->data){
                temp1 = temp1->next;
                temp2 = temp2->next;
                if(!temp1){
                    return new Node(0);
                }
            }
            if(temp2->data > temp1->data){
                swap(head1,head2);
            }
        }
        head1 = reverseList(head1);
        head2 = reverseList(head2);
        Node* newList = NULL;
        Node* last = NULL;
        Node* temp1 = head1;
        Node* temp2 = head2;
        while(temp1){
            int small = 0;
            if(temp2){
                small = temp2->data;
            }
            if(temp1->data<small){
                temp1->next->data = temp1->next->data - 1;
                temp1->data = temp1->data + 10;
            }
            Node* newNode = new Node(temp1->data - small);
            if(newList == NULL){
                newList  = newNode;
                last = newNode;
            }else{
                last->next = newNode;
                last = last->next;
            }
            temp1 = temp1->next;
            if(temp2){
                temp2 = temp2->next;
            }
        }
        newList = reverseList(newList);
        while(newList && newList->data == 0){
            newList = newList->next;
        }
        return newList;
    }
};

//{ Driver Code Starts.

// prints the elements of linked list starting with head
void printList(Node* n) {
    while (n) {
        cout << n->data;
        n = n->next;
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        LinkedList LL1;
        string l1,l2;
        cin>>l1;
        for (int j = 0; j < n; ++j) {
            int x=(l1[j]-'0');
            LL1.insert(x);
        }

        int m;
        cin >> m;
        LinkedList LL2;
        cin>>l2;
        for (int j = 0; j < m; ++j) {
            int x=(l2[j]-'0');
            LL2.insert(x);
        }

        Solution ob;
        Node* res = ob.subLinkedList(LL1.head, LL2.head);
        printList(res);
    }

    return 0;
}

// } Driver Code Ends