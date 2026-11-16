package main

import (
	"fmt"
	"unicode"
)

func main() {
	str := ""
	fmt.Scan(&str)

	result := ""
	for _, c := range str {
		if unicode.IsUpper(c) {
			result += string(unicode.ToLower(c))
		} else {
			result += string(unicode.ToUpper(c))
		}
	}
	fmt.Print(result)
}