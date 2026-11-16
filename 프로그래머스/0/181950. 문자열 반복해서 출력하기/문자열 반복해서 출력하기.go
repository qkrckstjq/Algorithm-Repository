package main

import (
	"fmt"
)

func main() {
	var str string
	var num int

	fmt.Scanf("%s %d", &str, &num)

	result := ""
	for i := 0; i < num; i++ {
		result += str
	}

	fmt.Print(result)
}
