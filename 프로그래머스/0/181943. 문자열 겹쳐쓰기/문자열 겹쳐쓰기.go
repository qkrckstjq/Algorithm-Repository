import "fmt"

func solution(my_string string, overwrite_string string, s int) string {
    fmt.Scan(&my_string, overwrite_string, s)

	result := ""
	for i := 0; i < s; i++ {
		result += string(my_string[i])
	}
	result += overwrite_string
	for i := s + len(overwrite_string); i < len(my_string); i++ {
		result += string(my_string[i])
	}
	return result
}