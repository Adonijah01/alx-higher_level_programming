#include <stdlib.h>

#include "lists.h"

/**

  * insert_node - inserts number to  sorted singly linked list

  * @head: pointer to thee list.

  * @number: num to be inserted.

  * Return: address new node or NULL if it fail

  */

listint_t *insert_node(listint_t **head, int number)

{

	listint_t *before, *new_Node;



	new_Node = malloc(sizeof(listint_t));

	if (new_Node != NULL)

	{

		new_Node->n = number;

		if (*head == NULL || (*head)->n >= new_Node->n)

		{

			new_Node->next = *head;

			*head = new_Node;

			return (new_Node);

		}

		else

		{

			before = *head;

			while (before->next != NULL && before->next->n < new_Node->n)

				before = before->next;

			new_Node->next = before->next;

			before->next = new_Node;

			return (new_Node);

		}

	}

	return (NULL);

}