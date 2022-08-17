import concurrent
import openai

MAX_WORKERS = 5

def get_aspects(prompt):
    #enter your prompt here
    gpt_prompt = """Instructions: Find out the persons main career.
Example: Taylor Swift

Answer: Singer/songwriter

Example: {prompt}

Answer:
    """
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response['choices'][0]['text']

# replace this list as required
PROMPT = ['Sundar Pichai', 'Benazir Bhutto', 'Cristiano Ronaldo'] 

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(get_aspects, prompt): prompt for prompt in PROMPTS}
    for future in concurrent.futures.as_completed(futures):
        print(futures[future], future.result())
       