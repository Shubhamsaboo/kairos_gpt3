# Importing Dependencies
from chronological import read_prompt, fetch_max_search_doc, main, cleaned_completion

# Creates a seamntic search over the given document 'animal.txt' to fetch the top-3 responses 
async def fetch_top_n_animals(query, n):

    # function read_prompt takes in the text file animals.txt and split on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    
    # Return the top-3 responses 
    # Default Config: engine="ada" (Fast and efficient for semantic search), n=number of responses to be returned
    return await fetch_max_search_doc(query, prompt_animals, engine="ada", n=n)

# Fucntion chains together the response of one prompt and plug it to another to create a complex solution
async def find_each_animals_favorite_food(animals):
    
    # function read_prompt takes in the the text file 'favorite_food', which allows to plug in varaible to acheive the QA task
    # Refer to the prompt to understand more, it uses the python 'f' string for formatting  
    prompt_favorite_food = read_prompt('favorite_food')
    
    # Empty list to store the food choices of all the animals 
    favorite_foods = []
    
    # Running multiple completions in loop, to get the favorite food for all 'n' animals
    for animal in animals:
        # Calling the completion method along with the specific GPT-3 parameters
        # Default Config: engine="davinci", temperature=0.2, stop=["\n\n"]
        res = await cleaned_completion(prompt_favorite_food.format(animal), engine="davinci", temperature=0.2, stop=["\n\n"])
        favorite_foods.append({ animal: res})
    return favorite_foods

# Designing the end-to-end async workflow, capable of running multiple prompts in parallel 
async def workflow():

    # Fetching the top_n animals using the the function
    animals = await fetch_top_n_animals('monkey', 3)

    # Fetching the favourite food for each of those three animals
    favorite_foods = await find_each_animals_favorite_food(animals)

    # Printing the result in console
    print(favorite_foods)

# invoke Chronology by using the main function to run the async workflow
main(workflow)