#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Check if listint_t list contains a cycle
 * @head: Pointer to first node in listint_t list
 *
 * Return: 0 if no cycle detected, else 1
 */
int check_cycle(listint_t *list) {
  listint_t *slow, *fast;
  slow = fast = list;

  while (slow && fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;

    if (slow == fast) {
      return (1);
    }
  }
  return (0);
}
