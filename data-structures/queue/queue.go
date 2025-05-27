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

func (q Queue[T]) IsEmpty() bool {
	return q.back == q.front
}

func (q Queue[T]) IsFull() bool {
	return q.Size() == q.capacity
}

func (q Queue[T]) Size() uint {
	return q.back - q.front
}

func (q *Queue[T]) Enqueue(value T) bool {
	if q.IsFull() {
		return false
	}

	// back is at the last index and there is available space at the start of the
	// queue, shift all element towards the front.
	if q.back == (q.capacity) && q.front != 0 {
		size := q.Size()
		for i := range size {
			q.data[i] = q.data[i+q.front]
		}
		q.front = 0
		q.back = size
	}

	q.data[q.back] = value
	q.back++
	return true
}

func (q *Queue[T]) Dequeue() *T {
	if q.IsEmpty() {
		return nil
	}

	value := q.data[q.front]
	q.front++

	if q.IsEmpty() {
		q.back = 0
		q.front = 0
	}

	return &value
}

func (q Queue[T]) Peek() *T {
	if q.IsEmpty() {
		return nil
	}

	value := q.data[q.front]
	return &value
}
