#include "lists.h"

/**
 * check_cycle - check for a loop
 * @list: head of the list
 *
 * Return: 0 if theres no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *tail = list;

	if (list == NULL)
		return (0);

	while (tail && tail->next)
	{
		head = head->next;
		tail = tail->next->next;
		if (head == tail)
		{
			return (1);
		}
	}
	return (0);
}
