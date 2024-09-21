#include <iostream>
#include <stack>
using namespace std;


typedef struct Node
{
    int value;
    struct Node *pleft;
    struct Node *pright;
}Node;

typedef struct {
    Node* root;
}Tree;


// create tree: new each node and insert node to tree root
void CreateTree(Tree* pTree,int value)
{
    //create a Node,node value is value
    Node* pNode=(Node *)malloc(sizeof(Node));
    pNode -> value = value;
    pNode -> pleft= NULL;
    pNode -> pright =NULL;

    //insert this node the tree
    if(pTree -> root ==NULL )
    {
        // case: no tree
        pTree ->root = pNode;
    }
    else
    {
        //case: tree existed, insert to tree root
        Node * p= pTree->root;
        while(p != NULL){
            if(value < p->value) {// go into left child
                if (p->pleft == NULL) {
                    p->pleft = pNode;
                    return;
                }
                else{
                    p = p->pleft;
                }
            }
            else{ //go into right child
                if (p->pright == NULL) {
                    p->pright = pNode;
                    return;
                }
                else{
                    p = p->pright;
                }  

            }
        }
        return;
    }
}

// travel node in recursive
void travelNode(Node *pNode)
{
    if(pNode != NULL)
    {
       travelNode(pNode->pleft);
       printf("Travel node:%d\n",pNode->value);
       travelNode(pNode->pright); 
    }    
}

//delete node in recursive
void deleteNode(Node *pNode)
{
    if(pNode != NULL)
    {
       deleteNode(pNode->pleft);
       printf("Delete node:%d\n",pNode->value);
       deleteNode(pNode->pright); 
    }    
}

//midTravelTree non-recursive
void MidTravelTree(Tree *pTree)
{
    stack<Node*> s;  //need use stack
    Node* pNode = pTree->root;
    while(pNode !=NULL || !s.empty())
    {
        if(pNode!=NULL) {
            s.push(pNode);
            pNode = pNode->pleft;
        }
        else{
            pNode = s.top();
            s.pop();
            printf("%d\t",pNode->value);
            pNode = pNode->pright;   
        }   
    }
    printf("\n");
}


int main()
{
    cout << "Hello, this is BiTree create and travel" << endl;
    cout << "Test Data: {12,5,3,7,15,13,20};" << endl;
    // test data
    int arr[]={12,5,3,7,15,13,20};
    int len = sizeof(arr)/sizeof(arr[0]);  
    //create an empty tree
    Tree tree;
    tree.root = NULL;
    cout << "Create Tree" << endl;
    //use the test data to build tree
    for (int i=0; i<len; i++)
    {
        // printf("%d\t",arr[i]);  
        CreateTree(&tree,arr[i]);
    }
    cout << "Travel Tree" << endl;
    //travelNode(tree.root);
    MidTravelTree(&tree);
    cout << "Delete Tree" << endl;
    deleteNode(tree.root);

    cout << endl;
    return 0;
}
