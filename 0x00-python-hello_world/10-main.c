/*
 * main - check the code
 * Return: Always 0
 */
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int main(void) {
  listint_t *head, *current, *temp;
  int i;

  head = NULL;

  add_nodeint(&head, 0);
  add_nodeint(&head, 1);
  add_nodeint(&head, 2);
  add_nodeint(&head, 3);
  add_nodeint(&head, 4);
  add_nodeint(&head, 98);
  add_nodeint(&head, 492);
  add_nodeint(&head, 890);
  add_nodeint(&head, 7800);
  print_listint(head);

  if (check_cycle(head) == 0) {
    printf("Section 1");
    printf("Linked list has no cycle\n");
  } else if (check_cycle(head) == 1) {
    printf("Section 1");
    printf("Linked list has cycle\n");
  }

  current = head;
  for (i = 0; i < 4; i++)
    current = current->next;
  temp = current->next;
  current->next = head;

  if (check_cycle(head) == 0) {
    printf("Section 2");
    printf("Linked list has no cycle\n");
  } else if (check_cycle(head) == 1) {
    printf("Section 2");
    printf("Linked list has cycle\n");
  }

  current = head;
  for (i = 0; i < 4; i++)
    current = current->next;
  current->next = temp;

  free_listint(head);

  return 0;
}
