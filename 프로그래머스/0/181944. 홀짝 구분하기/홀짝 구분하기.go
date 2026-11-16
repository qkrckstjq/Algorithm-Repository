package main

import "fmt"

func main() {
	var num int
	fmt.Scan(&num)

	if num % 2 == 0 {
		fmt.Printf("%d is even", num)
	} else {
		fmt.Printf("%d is odd", num)
	}
}