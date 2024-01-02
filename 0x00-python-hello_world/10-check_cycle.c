#include "lists.h"

/**
 * check_cycle - Function to check if there is cycle in list
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *y = list;

	if (!list)
		return (0);

	while (1)
	{
		if (x->next != NULL && x->next->next != NULL)
		{
			x = x->next->next;
			y = y->next;

			/* Circle is found if nodes match*/
			if (x == y)
				return (1);
		}
		else
			return (0);
	}
}
