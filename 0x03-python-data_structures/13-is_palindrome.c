#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Checks i it is a  palindrome
  * @head: head
  *
  * Return: 0 if  not palindrome, 1 if it is.
  */
int is_palindrome(listint_t **head)
{
    listint_t *start = NULL, *end = NULL;
    unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    start = *head;
    len = listint_len(start);
    len_cyc = len * 2;
    len_list = len_cyc - 2;
    end = *head;

    for (; i < len_cyc; i = i + 2)
    {
        if (start[i].n != end[len_list].n)
            return (0);

        len_list = len_list - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - Gets a node
  * @head: head of linked list
  * @index: index to find.
  *
  * Return: specific node of linkedlist
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iter_times == index)
				return (current);

			current = current->next;
			++iter_times;
		}
	}

	return (NULL);
}

/**
  * slistint_len - Counts elements in the linkedlist.
  * @h: linked list to be counted
  *
  * Return: Number of elements
  */
size_t listint_len(const listint_t *h)
{
	int length = 0;

	while (h != NULL)
	{
		++length;
		h = h->next;
	}

	return (length);
}




/**
Adonijah Kiplimo

*/



