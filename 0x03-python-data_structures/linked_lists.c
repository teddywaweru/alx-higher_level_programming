#include "lists.h"
#include <stdlib.h>

/**
 * print_listint_t - prints all elements of a listint_t list
 * @h: pointer to the head of the list
 *
 * Return: number of nodes
 */
size_t print_listint_t(listint_t *h) {
  int count;
  count = 0;
  while (h != NULL) {

    h = h->next;
    count++;
  }
  return (count);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t
 * @n: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, int n) {
  // traverse through the list  find end
  // create new node
  // have last node point to new node
  // check if current list is NULL
  // check if new node is NULL
  listint_t *current;
  listint_t *new;

  current = *head;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return NULL;

  new->next = NULL;
  new->n = n;

  if (*head == NULL) {
    *head = new;
    return (new);
  }

  while (current->next != NULL) {
    current = current->next;
  }

  current->next = new;

  return (new);
}

/**
 * free_listint - free a listint_t
 * @head: pointer to a list to  be freed
 *
 * Return: void
 */
void free_listint(listint_t *head) {
  // create a temporary buffer for next value
  // drop current
  listint_t *current;
  while (head != NULL) {
    current = head;
    head = head->next;

    free(current);
  }
}
