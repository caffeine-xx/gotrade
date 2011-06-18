package main

import (
	"fmt"
	"regexp"
	"os"
  "xml"
  "io/ioutil"
  "io"
  "file"
)

func main() {
	b := make([]byte, 100)
	os.Stdin.Read(b)
	os.Stdout.Write(b)
	var test,err = regexp.Compile(".*")
	matched := test.Match([]byte("foo"))
	if(err != nil) {
		fmt.Println(err.String())
		return
	}
	if matched {
		fmt.Println("matched")
	} else {
		fmt.Println("not matched")
	}
}
