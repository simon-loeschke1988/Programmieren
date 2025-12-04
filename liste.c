#include <stdio.h>
#include <stdlib.h>

// Definition eines Listenelements (Node)
struct Node
{
    int data;          // Wert des Knotens
    struct Node *next; // Zeiger auf den nächsten Knoten
};

// Funktion, um einen neuen Knoten zu erstellen
struct Node *createNode(int value)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

// Funktion, um einen Knoten am Ende hinzuzufügen
void append(struct Node **head, int value)
{
    struct Node *newNode = createNode(value);

    // Wenn die Liste leer ist
    if (*head == NULL)
    {
        *head = newNode;
        return;
    }

    // Sonst bis zum letzten Element laufen
    struct Node *temp = *head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}

// Funktion, um die Liste auszugeben
void printList(struct Node *head)
{
    struct Node *current = head;
    while (current != NULL)
    {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Hauptprogramm
int main()
{
    struct Node *head = NULL; // Anfang der Liste (leer)

    append(&head, 10);
    append(&head, 20);
    append(&head, 30);

    printf("Inhalt der Liste:\n");
    printList(head);

    return 0;
}
