package main

import (
	"io"
	"net/http"
)

// hello performs initial personal authentication
func hello(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello world!")
}

func main() {
	http.Handle("/", http.FileServer(http.Dir("./www")))
	http.ListenAndServe(":52279", nil)
}
