#ifndef LISTS_H
#define LIST_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>


/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s {
	int n;
	struct listint_s next
} listint_t;

listint_t* add_nodeint(listint_t**, const int);
size_t print_listint(listint *);
int check_cycle(listint *);
void free_listint(listint *);

#endif /* LISTS_H */
