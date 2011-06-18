package main
import (
  "os"
  "xml"
  "fmt"
)

type Email struct {
  Where string "attr"
  Addr  string
}

type Result struct {
  XMLName xml.Name "result"
  Name  string
  Phone string
  Email []Email
  Groups  []string "group>value"
}

type Fix struct {
  Major string "attr"
  Minor string "attr"
  Fields []Field "fields>field"
}

type Field struct {
  Number string "attr"
  Name string "attr"
  Type string "attr"
  Value []Value
}

type Value struct {
  Enum string "attr"
  Description string "attr"
}

func main() {
  var file,_ = os.Open("./FIX44.xml")
  r := new(Fix)
  // f := new(Field)
  var err = xml.Unmarshal(file, &r)
  if err != nil {
    fmt.Println(err)
  } else {
    fmt.Println(r)
  }
}
