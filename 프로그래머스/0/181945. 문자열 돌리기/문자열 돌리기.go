package main

import "fmt"

func main() {
	a := ""
	fmt.Scan(&a)

	for _, w := range a {
		fmt.Println(string(w))
	}
}