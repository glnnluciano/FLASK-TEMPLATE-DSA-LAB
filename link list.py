class Node:
    """A class representing a node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A class for singly linked list."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_beginning(self):
        """Delete a node from the beginning."""
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        """Delete a node from the end."""
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def display(self):
        """Display all elements in the linked list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Application


def linked_list_menu():
    linked_list = LinkedList()

    while True:
        print("\n--- Linked List Operations ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            value = input(
                "Enter the value to insert at the beginning: ").strip()
            linked_list.insert_at_beginning(value)
            print(f"{value} inserted at the beginning.")

        elif choice == "2":
            value = input("Enter the value to insert at the end: ").strip()
            linked_list.insert_at_end(value)
            print(f"{value} inserted at the end.")

        elif choice == "3":
            linked_list.delete_at_beginning()
            print("Deleted node from the beginning.")

        elif choice == "4":
            linked_list.delete_at_end()
            print("Deleted node from the end.")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

        # Automatically display the linked list after every operation
        print("Current Linked List:")
        linked_list.display()


# Run the program
if __name__ == "__main__":
    linked_list_menu()
