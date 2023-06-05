#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has cycle in it.
 * @list: pointer to beginning of the node
 * Return: 0 if no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
