package main

import (
	"fmt"
    "io/ioutil"
	"context"
	gogpt "github.com/sashabaranov/go-gpt3"
)

func main() {
	c := gogpt.NewClient("YOUR_API_KEY")
	
	ctx := context.Background()
	
	prompt, err := ioutil.ReadFile("prompts/summarize_for_a_2nd_grader.txt")
	
	req := gogpt.CompletionRequest{
		MaxTokens: 100,
		Temperature: 0.5,
		TopP: 1.0,
		Stop: []string{"\n\n"},
		FrequencyPenalty: 0.2,
		Prompt: string(prompt),
	}

	resp, err := c.CreateCompletion(ctx, "davinci", req)

	if err != nil {
		return
	}
	fmt.Println("-------------------------")
	fmt.Println(resp.Choices[0].Text)
	fmt.Println("-------------------------")

}
