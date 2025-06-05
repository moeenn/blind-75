package queue

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestQueue(t *testing.T) {
	t.Run("full queue / dequeue", func(t *testing.T) {
		q := NewQueue[int](5)
		assert.True(t, q.IsEmpty())
		for i := range 5 {
			assert.True(t, q.Enqueue(i+1))
		}

		assert.Equal(t, 1, *q.Peek())
		assert.True(t, q.Size() == 5)
		assert.True(t, q.IsFull())

		isEnqueued := q.Enqueue(10)
		assert.True(t, !isEnqueued)

		for i := range 5 {
			v := q.Dequeue()
			assert.NotNil(t, v)
			assert.Equal(t, i+1, *v)
		}
		assert.True(t, q.IsEmpty())
		assert.True(t, !q.IsFull())

		v := q.Dequeue()
		assert.Nil(t, v)
	})

	t.Run("partial queue / dequeue", func(t *testing.T) {
		q := NewQueue[int](3)
		assert.Nil(t, q.Peek())
		assert.True(t, q.Enqueue(10))
		assert.True(t, q.Enqueue(20))
		assert.NotNil(t, q.Dequeue())
		assert.True(t, q.Enqueue(30))
		assert.True(t, q.Enqueue(40))
		assert.True(t, q.IsFull())
		assert.True(t, !q.Enqueue(50))

		assert.NotNil(t, q.Dequeue())
		assert.True(t, q.Enqueue(60))
		assert.True(t, q.IsFull())
	})
}
