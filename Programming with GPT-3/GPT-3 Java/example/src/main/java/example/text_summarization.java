
package example;

// Importing Dependencies 
import java.util.*;  
import java.io.*;
import com.theokanning.openai.OpenAiService;
import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.engine.Engine;


class OpenAiApiExample {
    public static void main(String... args) throws FileNotFoundException {
        
        String token = "YOUR_API_KEY";
        OpenAiService service = new OpenAiService(token);

        //System.out.println("\nGetting Davinci engine...");
        //Engine davinci = service.getEngine("davinci");

        System.out.println("\nCreating completion...");
        
        File file = new File("D:\\GPT-3 Book\\Programming with GPT-3\\GPT-3 Java\\example\\src\\main\\java\\example\\prompts\\summarize_for_a_2nd_grader.txt");
  
        Scanner sc = new Scanner(file);
  
        // we just need to use \\Z as delimiter
        sc.useDelimiter("\\Z");

        String pp = sc.next();
              
        List<String> li = new ArrayList<String>();
        
        li.add("\n\n'''");
        
        System.out.println("ArrayList : " + li.toString());

        CompletionRequest completionRequest = CompletionRequest.builder().prompt(pp).maxTokens(100).temperature(0.5).topP(1.0).frequencyPenalty(0.2).stop(li).echo(true).build();      
        service.createCompletion("davinci", completionRequest).getChoices().forEach(System.out::println);
        
    }
}