package linkedlist

type Node[T any] struct {
	Data T
	Next *Node[T]
}

type LinkedList[T any] struct {
	Head *Node[T]
	size uint
}

func NewLinkedList[T any]() *LinkedList[T] {
	return &LinkedList[T]{
		Head: nil,
		size: 0,
	}
}

func (list LinkedList[T]) Size() uint {
	return list.size
}

func (list *LinkedList[T]) Append(value T) {
	newNode := &Node[T]{Data: value, Next: nil}
	if list.Head == nil {
		list.Head = newNode
		list.size++
		return
	}

	// go to the last node.
	currentNode := list.Head
	for ; currentNode.Next != nil; currentNode = currentNode.Next {
	}

	currentNode.Next = newNode
	list.size++
}

func (list *LinkedList[T]) Prepend(value T) {
	newNode := &Node[T]{Data: value, Next: nil}
	if list.Head == nil {
		list.Head = newNode
		list.size++
		return
	}

	newNode.Next = list.Head
	list.Head = newNode
	list.size++
}

func (list LinkedList[T]) Iter() <-chan T {
	result := make(chan T)
	go func() {
		currentNode := list.Head
		for ; currentNode != nil; currentNode = currentNode.Next {
			result <- currentNode.Data
		}

		close(result)
	}()

	return result
}

type ValueWithIndex[T any] struct {
	Value T
	Index uint
}

func (list LinkedList[T]) IterWithIndex() <-chan ValueWithIndex[T] {
	result := make(chan ValueWithIndex[T])
	go func() {
		var i uint = 0
		currentNode := list.Head
		for ; currentNode != nil; currentNode = currentNode.Next {
			result <- ValueWithIndex[T]{Value: currentNode.Data, Index: i}
			i++
		}

		close(result)
	}()

	return result
}

func (list LinkedList[T]) At(index uint) *T {
	if index >= list.size {
		return nil
	}

	for entry := range list.IterWithIndex() {
		if entry.Index == index {
			return &entry.Value
		}
	}

	return nil
}

func (list *LinkedList[T]) Remove(index uint) bool {
	if index >= list.size {
		return false
	}

	if index == 0 {
		list.Head = list.Head.Next
		list.size--
		return true
	}

	current := list.Head
	var prev *Node[T] = nil
	var i uint = 0

	for ; current != nil; current = current.Next {
		if index == i {
			prev.Next = current.Next
			list.size--
			return true
		}

		prev = current
		i++
	}

	return false
}
