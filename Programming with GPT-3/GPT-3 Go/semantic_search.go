package main

import (
	"fmt"
  
	"context"

	gogpt "github.com/sashabaranov/go-gpt3"
)

func main() {
	c := gogpt.NewClient("YOUR_API_KEY")
	
	ctx := context.Background()
	
	searchReq := gogpt.SearchRequest{
		Documents: []string{"White House", "hospital", "school"},
		Query:     "the president",
	}
	searchResp, err := c.Search(ctx, "ada", searchReq)
	if err != nil {
		return
	}
	fmt.Println(searchResp.SearchResults)
	
	max := array[0]

    for i := 1; i < array_size; i++ {

        if max < array[i] {

            max = array[i]
        }
    }

    fmt.Printf("\nMax element is : %d", max)
	searchResp.SearchResults

}
