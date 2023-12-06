#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head);
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *second_half, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Move fast by two and slow by one, until fast reaches the end. */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		/* Reverse the first half of the list as we move slow. */
		temp = slow;
		slow = slow->next;
		temp->next = prev_slow;
		prev_slow = temp;
	}

	/* If the list has an odd number of elements, skip the middle one. */
	if (fast != NULL)
		slow = slow->next;

	/* Compare the first half (prev_slow) with the second half (slow). */
	second_half = slow;
	while (prev_slow != NULL && second_half != NULL)
	{
		if (prev_slow->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		prev_slow = prev_slow->next;
		second_half = second_half->next;
	}

	/* Restore the original list by reversing the first half back. */
	prev_slow = NULL;
	while (slow != NULL)
	{
		temp = slow;
		slow = slow->next;
		temp->next = prev_slow;
		prev_slow = temp;
	}

	return (is_palindrome);
}
