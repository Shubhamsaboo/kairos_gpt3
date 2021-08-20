# Importing Dependencies
from chronological import read_prompt, fetch_max_search_doc, main


# Creates a seamntic search over the given document 'animal.txt' to fetch the top_most response 
async def fetch_top_animal(query):
    
    # function read_prompt takes in the text file animals.txt and split on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    
    # Return the top most response 
    # Default Config: engine="ada" (Fast and efficient for semantic search)
    return await fetch_max_search_doc(query, prompt_animals, engine="ada")

# Creates a seamntic search over the given document 'animal.txt' to fetch the top-3 responses
async def fetch_three_top_animals(query, n):
    
    # function read_prompt takes in the text file animals.txt and split on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    
    # Return the top-3 responses 
    # Default Config: engine="ada" (Fast and efficient for semantic search), n=number of responses to be returned 
    return await fetch_max_search_doc(query, prompt_animals, engine="ada", n=n)

# Designing the end-to-end async workflow, capable of running multiple prompts in parallel 
async def workflow():
    
    # Making async call to the search functions
    fetch_top_animal_res = await fetch_top_animal("monkey")
    fetch_top_three_animals_res = await fetch_three_top_animals("monkey", 3)

    # Printing the result in console
    print('-------------------------')
    print('Top Most Match for given Animal: {0}'.format(fetch_top_animal_res))
    print('-------------------------')
    print('Top Three Match for given Animal: {0}'.format(fetch_top_three_animals_res))
    print('-------------------------')

# invoke Chronology by using the main function to run the async workflow
main(workflow)