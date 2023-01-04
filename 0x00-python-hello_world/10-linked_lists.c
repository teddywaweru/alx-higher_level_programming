#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to the header of a linked list
 *
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h) {
  int x = 0;
  const listint_t *current;

  current = h;

  while (current != NULL) {
    x++;
    current = current->next;
  }
  return (x);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t
 * @head: ointer to a pointer of the start of the list
 * @n: interger to be included in node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n) {
  listint_t *new;

  new = malloc(sizeof(listint_t));

  if (new == NULL) {
    return (NULL);
  }
  new->n = n;
  new->next = *head;
  *head = new;
  return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to first node of list to be freed
 *
 * Return: NULL
 */
void free_listint(listint_t *head) {
  listint_t *current;

  while (head != NULL) {
    current = head;
    head = head->next;

    free(current);
  }
}
