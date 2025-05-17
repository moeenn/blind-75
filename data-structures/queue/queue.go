package queue

type Queue[T any] struct {
	data     []T
	back     uint
	front    uint
	capacity uint
}

func NewQueue[T any](capacity uint) *Queue[T] {
	return &Queue[T]{
		data:     make([]T, capacity),
		back:     0,
		front:    0,
		capacity: capacity,
	}
}

func (q Queue[T]) isEmpty() bool {
	return q.back == q.front
}

func (q Queue[T]) isFull() bool {
	return q.Size() == q.capacity
}

func (q Queue[T]) Size() uint {
	return q.back - q.front
}

func (q *Queue[T]) Enqueue(value T) bool {
	if q.isFull() {
		return false
	}

	q.data[q.back] = value
	q.back++
	return true
}

func (q *Queue[T]) Dequeue() *T {
	if q.isEmpty() {
		return nil
	}

	value := q.data[q.front]
	q.front++

	return &value
}
