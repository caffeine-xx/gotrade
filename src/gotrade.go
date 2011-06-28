package main
import (
  fmt "fmt"
  strconv "strconv"
  reflect "reflect"
)

type FixBuffer struct {
  buffer []byte
  pos int
}

func scanTo(buf []byte, from int, to uint8) int {
  var npos = from
  for npos < len(buf) && buf[npos] != to {
    npos ++
  }
  return npos
}

func (b *FixBuffer) NextTag() int {
  npos := scanTo(b.buffer, b.pos, '=')
  tag := toInt(b.buffer[b.pos:npos])
  b.pos = npos+1
  return tag
}

func (b *FixBuffer) NextValue() []byte {
  npos := scanTo(b.buffer, b.pos, ' ')
  value := b.buffer[b.pos:npos]
  b.pos = npos+1
  return value
}

func (b FixBuffer) HasNext() bool {
  return b.pos < len(b.buffer)
}

func Header (b *FixBuffer) (string,int) {
  // Get "8=FIX4.4"
  b.NextTag()
  b.NextValue()

  // Get length
  b.NextTag()
  length := toInt(b.NextValue())

  // Get MsgType
  b.NextTag()
  typ := b.NextValue()
  return string(typ), length
}

func toInt (s []byte) int {
  i, _ := strconv.Atoi(string(s))
  return i
}

func main() {
  var msg = []byte("8=FIX.4.4 9=64 35=A 49=DEMOXZVQ 56=MBT 34=596 52=20100315-23:58:15 98=0 108=30 10=015")
  fb := FixBuffer{msg,0}
  t := reflect.TypeOf(FixBuffer{})
  fmt.Println(t.Name())
  msgType, length := Header(&fb)
  fmt.Printf("l %i, r %i, t %s\n", length, len(fb.buffer)-fb.pos, msgType)
  for fb.HasNext() {
    fmt.Printf("tag: %i\n", fb.NextTag())
    fmt.Println(string(fb.NextValue()))
  }
}
