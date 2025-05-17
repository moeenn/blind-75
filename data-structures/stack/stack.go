package stack

type Stack[T any] struct {
	data         []T
	capacity     uint
	currentIndex uint
}

func NewStack[T any](capacity uint) *Stack[T] {
	return &Stack[T]{
		data:         make([]T, capacity),
		capacity:     capacity,
		currentIndex: 0,
	}
}

func (s Stack[T]) Capacity() uint {
	return s.capacity
}

func (s Stack[T]) Size() uint {
	return s.currentIndex
}

func (s *Stack[T]) Push(value T) bool {
	if s.currentIndex == s.capacity {
		return false
	}

	s.data[s.currentIndex] = value
	s.currentIndex++
	return true
}

func (s Stack[T]) Peek() *T {
	if s.currentIndex == 0 {
		return nil
	}

	value := s.data[s.currentIndex-1]
	return &value
}

func (s *Stack[T]) Pop() *T {
	value := s.Peek()
	if value != nil {
		s.currentIndex--
	}

	return value
}

func (s Stack[T]) Iter() <-chan T {
	result := make(chan T)
	var i uint = 0
	go func() {
		for ; i < s.currentIndex; i++ {
			result <- s.data[i]
		}
		close(result)
	}()

	return result
}
