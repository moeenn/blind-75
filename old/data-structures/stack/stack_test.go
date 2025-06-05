package stack

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestStack(t *testing.T) {
	stack := NewStack[int](5)
	assert.Equal(t, uint(5), stack.Capacity())

	firstOk := stack.Push(10)
	assert.True(t, firstOk)
	assert.Equal(t, uint(1), stack.Size())

	stack.Push(20)
	assert.Equal(t, uint(2), stack.Size())

	stack.Push(30)
	stack.Push(40)
	fifthOk := stack.Push(50)
	assert.True(t, fifthOk)
	assert.Equal(t, uint(5), stack.Size())

	sixthOk := stack.Push(60)
	assert.False(t, sixthOk)
	assert.Equal(t, uint(5), stack.Size())

	peeked := stack.Peek()
	assert.Equal(t, 50, *peeked)
	assert.Equal(t, uint(5), stack.Size())

	popped := stack.Pop()
	assert.Equal(t, 50, *popped)
	assert.Equal(t, uint(4), stack.Size())

	// remove all.
	for range 5 {
		stack.Pop()
	}
	assert.True(t, stack.Size() == 0)
}
