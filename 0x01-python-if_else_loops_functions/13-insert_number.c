#include "lists.h"

/**
 * insert_node - Inserts a node into a linled list
 * @head: the head
 * @number: the number to insert
 *
 * Return: the new single linked list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint *h, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	h = *head;
	if (h == NULL || h->n >= number)
	{
		new->next = h;
		*head = new;
		return (new);
	}
	while (h && h->next && h->next->n < number)
		h = h->next;

	new->next = h->next;
	h->next = new;
	return (new);
}
