#include "lists.h"

/**
 *check_cycle - finds a loop in a single list linked
 *@head: head pointer
 *Return: 1 if is find loop or 0 if not
 */

int check_cycle(listint_t *head)
{
	int *node1, *node2;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		node1 = (int *)&head;
		node2 = (int *)&head->next;
		if (head->next == NULL)
			return (0);

		if (*node1 - *node2 <= 0)
			return (1);

		head = head->next;
	}
	return (0);
}
