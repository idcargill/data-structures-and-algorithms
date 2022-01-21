# Animal Shelter

## Challenge Summary
<!-- Description of the challenge -->
1. Create a class called AnimalShelter which holds only dogs and cats.
2. The shelter operates using a first-in, first-out approach.
3. Implement Methods:

- enqueue
      Arguments: animal\
      animal can be either a dog or a cat object.
- dequeue
      Arguments: pref
      pref can be either "dog" or "cat"\
      Return: either a dog or a cat, based on preference.
      If pref is not "dog" or "cat" then return null.

## Whiteboard Process

![White Board](stack-queue-animal-shelter.png)

## Approach & Efficiency

Animal shelter is a class that creates Nodes from the Animal class.
When animals are created, input is validated to only accept a 'cat' or 'dog'.
Animals added to the shelter are put in a queue. To find the desired pet, the queue is traversed with the front element being put into a stack. Once the desired pet is found the pet is returned.
Elements in the temporary stack are popped off and set back in the queue at the front. 

### Big0

Time: O(1)
Space: O(1)

## Solution

Animal Class
> cat = Animal('cat')

Shelter Class
> shelter = AnimalShelter()

Methods: enqueue
> shelter.enqueue('cat')
add a animal class to shelter queue

Method: dequeue
> shelter.dequeue('cat')
returns desired pet or none
