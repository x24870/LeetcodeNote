package main

type item interface{}

type stack struct {
	items []item
}

func NewStack() *stack {
	s := stack{items: []item{}}
	return &s
}

func (s *stack) IsEmpty() bool {
	if len(s.items) == 0 {
		return true
	}
	return false
}

func (s *stack) Push(v int) {
	s.items = append(s.items, v)
}

func (s *stack) Pop() item {
	if s.IsEmpty() {
		return nil
	}
	top := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return top
}

func (s *stack) Peek() item {
	if s.IsEmpty() {
		return nil
	}

	return s.items[len(s.items)-1]
}

// stack definition: all elements in stack > arr[i]
func dailyTemperatures(temperatures []int) []int {
	ret := make([]int, len(temperatures))
	s := NewStack()

	for idx := len(temperatures) - 1; idx >= 0; idx-- {
		if s.IsEmpty() {
			ret[idx] = 0
		} else if temperatures[s.Peek().(int)] > temperatures[idx] {
			ret[idx] = 1
		} else {
			for !s.IsEmpty() && temperatures[s.Peek().(int)] <= temperatures[idx] {
				s.Pop()
			}
			if s.IsEmpty() {
				ret[idx] = 0
			} else {
				ret[idx] = s.Peek().(int) - idx
			}
		}
		s.Push(idx)
	}

	return ret
}
