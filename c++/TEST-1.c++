#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

// Node structure for the binary tree
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

// Function to initialize an array with n random values
std::vector<int> initializeArray(int n) {
    std::vector<int> arr;
    for (int i = 0; i < n; i++) {
        arr.push_back(rand() % 100); // Generating random values between 0 and 99
    }
    return arr;
}

// Function to create an empty node with value E
Node* createEmptyNode(int E) {
    return new Node(E);
}

// Function to build a binary tree following the definition
Node* buildBinaryTree(const std::vector<int>& arr, int n, int E) {
    Node* root = new Node(arr[0]);

    // Create an array of empty nodes with value E
    std::vector<Node*> emptyNodes;
    for (int i = 0; i < n - 1; i++) {
        emptyNodes.push_back(createEmptyNode(E));
    }

    // Build the binary tree
    for (int i = 0; i < n - 1; i++) {
        Node* newNode = new Node(arr[i + 1]);
        newNode->left = root;
        newNode->right = emptyNodes[i];
        root = newNode;
    }

    return root;
}

// Function to display the tree information using inorder traversal
void displayTree(Node* root) {
    if (root) {
        displayTree(root->left);
        std::cout << root->data << " ";
        displayTree(root->right);
    }
}

// Function to search for a value in the tree using recursion
Node* searchValue(Node* root, int value) {
    if (!root)
        return nullptr;

    if (root->data == value)
        return root;

    Node* leftResult = searchValue(root->left, value);
    Node* rightResult = searchValue(root->right, value);

    if (leftResult)
        return leftResult;

    return rightResult;
}

// Function to insert a new node into the tree
Node* insertNode(Node* root, int value, int E) {
    if (!root)
        return new Node(value);

    if (root->data == E) {
        root->data = value;
        return root;
    }

    if (value < root->data)
        root->left = insertNode(root->left, value, E);
    else
        root->right = insertNode(root->right, value, E);

    return root;
}

// Function to remove a node from the tree
Node* removeNode(Node* root, int value, int E) {
    if (!root)
        return nullptr;

    if (value < root->data)
        root->left = removeNode(root->left, value, E);
    else if (value > root->data)
        root->right = removeNode(root->right, value, E);
    else {
        if (root->data == E) {
            // If a node with value E is found, it's just marked for deletion (set to E)
            root->data = E;
        } else if (!root->left) {
            Node* temp = root->right;
            delete root;
            return temp;
        } else if (!root->right) {
            Node* temp = root->left;
            delete root;
            return temp;
        }

        Node* temp = root->right;
        while (temp->left)
            temp = temp->left;

        root->data = temp->data;
        root->right = removeNode(root->right, temp->data, E);
    }

    return root;
}

int main() {
    srand(time(0));

    int n = 5; // Number of elements in the array
    int E = 42; // Value greater than any element in the array

    std::vector<int> arr = initializeArray(n);
    Node* root = buildBinaryTree(arr, n, E);

    // Display the tree
    std::cout << "Tree Inorder Traversal: ";
    displayTree(root);
    std::cout << std::endl;

    // Search for a value
    int valueToSearch = 20;
    Node* result = searchValue(root, valueToSearch);
    if (result) {
        std::cout << "Value " << valueToSearch << " found in the tree." << std::endl;
    } else {
        std::cout << "Value " << valueToSearch << " not found in the tree." << std::endl;
    }

    // Insert a new node
    int newValue = 10;
    root = insertNode(root, newValue, E);

    // Display the updated tree
    std::cout << "Tree Inorder Traversal after insertion: ";
    displayTree(root);
    std::cout << std::endl;

    // Remove a node
    int nodeToRemove = 7;
    root = removeNode(root, nodeToRemove, E);

    // Display the updated tree
    std::cout << "Tree Inorder Traversal after removal: ";
    displayTree(root);
    std::cout << std::endl;

    return 0;
}
