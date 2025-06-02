package linkedlist

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLinkedList(t *testing.T) {
	list := NewLinkedList[int]()
	list.Append(10)
	list.Append(20)
	list.Append(30)
	list.Append(40)
	list.Append(50)
	list.Prepend(200)
	list.Prepend(100)

	var expectedSize uint = 7
	assert.Equal(t, expectedSize, list.Size())

	allElements := make([]int, 7)
	for n := range list.Iter() {
		for i := range expectedSize {
			allElements[i] = n
		}
	}
	assert.Equal(t, int(expectedSize), len(allElements))

	first := list.At(0)
	assert.Equal(t, 100, *first)

	third := list.At(2)
	assert.Equal(t, 10, *third)

	last := list.At(6)
	assert.Equal(t, 50, *last)

	isRemoved := list.Remove(0)
	assert.True(t, isRemoved)
	assert.Equal(t, uint(6), list.Size())

	isRemoved = list.Remove(5)
	assert.True(t, isRemoved)
	assert.Equal(t, uint(5), list.Size())

	isRemoved = list.Remove(2)
	assert.True(t, isRemoved)
	assert.Equal(t, uint(4), list.Size())
}
