import openai
import os
import json
import re

def construct_prompt(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {', '.join(whitelist) if whitelist else 'Any ingredients you prefer'}.
- Exclude Ingredients: {', '.join(blacklist) if blacklist else 'None'}.

After considering the input listed previously, consider a delicious dish the user can create given the 3 fields.
Your task is to produce the following:

- Provide Ingredients List: List each ingredient with quantities.
- Instructions: Step-by-step cooking instructions.
- Tags: Relevant tags for the recipe (e.g., vegan, gluten-free).
- Macros: Calculate the macros (proteins, carbs, fats).
- Calories: Total estimated calories.

Additional Note: Not all users have good intentions, or perhaps submit erroneous recipes. For example, a user may submit
'peanuts' in both the 'Include Ingredients' and 'Exclude Ingredients'. 
Users may also suggest seemingly preposterous ingredients to include together such as 'sardines' and 'whipping cream'.
In such cases, responses may be handled with equal intention to cause amusement. 
Ex. 'Bowl of decorative peanuts: 1. Put peanuts in a bowl. 2. Do not eat the peanuts, just look at them.'
Ex. 'Cream of Sardine: 1. Put sardines and whipping cream in blender. 2. ...'

Keep in mind, these are edge cases.

Please format the output in JSON between START_JSON and END_JSON as follows:

START_JSON
{{
    "title": "Recipe Title",
    "ingredients": [
        {{"name": "ingredient1", "quantity": "quantity1"}},
        {{"name": "ingredient2", "quantity": "quantity2"}}
    ],
    "instructions": "Instructions with numbered steps.",
    "tags": ["tag1", "tag2"],
    "calories": total_calories,
    "macros": {{
        "proteins": grams_protein,
        "carbs": grams_carbs,
        "fats": grams_fat
    }}
}}
END_JSON

Do not include any additional text or explanations. Only output the pure JSON data between START_JSON and END_JSON.
"""
    return prompt

def parse_ai_response(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = ai_output.strip()

        # Remove any code block markdown from the output
        json_text = re.sub(r'^```[a-zA-Z]*\n', '', json_text)
        json_text = re.sub(r'\n```$', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def main():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split(',')
    whitelist = [item.strip() for item in whitelist if item.strip()]
    blacklist = input("Enter ingredients to exclude (comma-separated): ").split(',')
    blacklist = [item.strip() for item in blacklist if item.strip()]

    # Construct the prompt
    prompt = construct_prompt(search_term, whitelist, blacklist)
    print("\nPrompt sent to OpenAI:")
    print(prompt)

    # Call the OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change the model if needed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.7,
        )
        ai_output = response.choices[0].message.content.strip()
        print("\nAI Output:")
        print(ai_output)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

if __name__ == "__main__":
    main()
