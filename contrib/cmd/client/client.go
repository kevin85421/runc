package main

import (
	"net"
	"log"
)

func main() {
	conn, err := net.Dial("tcp", "0.0.0.0:8888")
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	msg := []byte("newfstatat")
	_, err = conn.Write(msg)
	if err != nil {
		log.Fatal(err)
	}
}
