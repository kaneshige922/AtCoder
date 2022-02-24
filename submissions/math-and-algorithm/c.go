package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func s2ilist(s []string) []int {
	x := make([]int, 0)
	var si int
	for i := 0; i < len(s); i++ {
		si, _ = strconv.Atoi(s[i])
		x = append(x, si)
	}
	return x
}

func main() {

	nextLine()
	a := s2ilist(strings.Split(nextLine(), " "))
	ans := 0
	for i := 0; i < len(a); i++ {
		ans += a[i]
	}
	fmt.Println(ans)

}
