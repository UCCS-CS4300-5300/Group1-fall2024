
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


import openai
import os
import json
import re

def x_construct_prompt__mutmut_orig(search_term, whitelist, blacklist):
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

def x_construct_prompt__mutmut_1(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'XXany cuisineXX'}".
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

def x_construct_prompt__mutmut_2(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {'XX, XX'.join(whitelist) if whitelist else 'Any ingredients you prefer'}.
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

def x_construct_prompt__mutmut_3(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {', '.join(None) if whitelist else 'Any ingredients you prefer'}.
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

def x_construct_prompt__mutmut_4(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {', '.join(whitelist) if whitelist else 'XXAny ingredients you preferXX'}.
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

def x_construct_prompt__mutmut_5(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {', '.join(whitelist) if whitelist else 'Any ingredients you prefer'}.
- Exclude Ingredients: {'XX, XX'.join(blacklist) if blacklist else 'None'}.

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

def x_construct_prompt__mutmut_6(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {', '.join(whitelist) if whitelist else 'Any ingredients you prefer'}.
- Exclude Ingredients: {', '.join(None) if blacklist else 'None'}.

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

def x_construct_prompt__mutmut_7(search_term, whitelist, blacklist):
    prompt = f"""
You are a chef that creates recipes. A user is asking for a custom recipe given the following 3 fields:

- Recipe Name: A creative title for the recipe relevant to "{search_term if search_term else 'any cuisine'}".
- Include Ingredients: {', '.join(whitelist) if whitelist else 'Any ingredients you prefer'}.
- Exclude Ingredients: {', '.join(blacklist) if blacklist else 'XXNoneXX'}.

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

def x_construct_prompt__mutmut_8(search_term, whitelist, blacklist):
    prompt = None
    return prompt

x_construct_prompt__mutmut_mutants = {
'x_construct_prompt__mutmut_1': x_construct_prompt__mutmut_1, 
    'x_construct_prompt__mutmut_2': x_construct_prompt__mutmut_2, 
    'x_construct_prompt__mutmut_3': x_construct_prompt__mutmut_3, 
    'x_construct_prompt__mutmut_4': x_construct_prompt__mutmut_4, 
    'x_construct_prompt__mutmut_5': x_construct_prompt__mutmut_5, 
    'x_construct_prompt__mutmut_6': x_construct_prompt__mutmut_6, 
    'x_construct_prompt__mutmut_7': x_construct_prompt__mutmut_7, 
    'x_construct_prompt__mutmut_8': x_construct_prompt__mutmut_8
}

def construct_prompt(*args, **kwargs):
    result = _mutmut_trampoline(x_construct_prompt__mutmut_orig, x_construct_prompt__mutmut_mutants, *args, **kwargs)
    return result 

construct_prompt.__signature__ = _mutmut_signature(x_construct_prompt__mutmut_orig)
x_construct_prompt__mutmut_orig.__name__ = 'x_construct_prompt'



def x_parse_ai_response__mutmut_orig(ai_output):
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

def x_parse_ai_response__mutmut_1(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'XXSTART_JSON(.*?)END_JSONXX', ai_output, re.DOTALL)
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

def x_parse_ai_response__mutmut_2(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', None, re.DOTALL)
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

def x_parse_ai_response__mutmut_3(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', re.DOTALL)
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

def x_parse_ai_response__mutmut_4(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = None
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

def x_parse_ai_response__mutmut_5(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(2).strip()
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

def x_parse_ai_response__mutmut_6(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = None
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

def x_parse_ai_response__mutmut_7(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = None

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

def x_parse_ai_response__mutmut_8(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = ai_output.strip()

        # Remove any code block markdown from the output
        json_text = re.sub(r'XX^```[a-zA-Z]*\nXX', '', json_text)
        json_text = re.sub(r'\n```$', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_9(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = ai_output.strip()

        # Remove any code block markdown from the output
        json_text = re.sub(r'^```[a-zA-Z]*\n', 'XXXX', json_text)
        json_text = re.sub(r'\n```$', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_10(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = ai_output.strip()

        # Remove any code block markdown from the output
        json_text = re.sub(r'^```[a-zA-Z]*\n', '', None)
        json_text = re.sub(r'\n```$', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_11(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = ai_output.strip()

        # Remove any code block markdown from the output
        json_text = re.sub(r'^```[a-zA-Z]*\n', '',)
        json_text = re.sub(r'\n```$', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_12(ai_output):
    """Extract recipe components from AI response."""
    try:
        # Extract JSON between START_JSON and END_JSON
        match = re.search(r'START_JSON(.*?)END_JSON', ai_output, re.DOTALL)
        if match:
            json_text = match.group(1).strip()
        else:
            json_text = ai_output.strip()

        # Remove any code block markdown from the output
        json_text = None
        json_text = re.sub(r'\n```$', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_13(ai_output):
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
        json_text = re.sub(r'XX\n```$XX', '', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_14(ai_output):
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
        json_text = re.sub(r'\n```$', 'XXXX', json_text)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_15(ai_output):
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
        json_text = re.sub(r'\n```$', '', None)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_16(ai_output):
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
        json_text = re.sub(r'\n```$', '',)

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_17(ai_output):
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
        json_text = None

        # Parse the JSON data
        recipe_data = json.loads(json_text)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_18(ai_output):
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
        recipe_data = json.loads(None)
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_19(ai_output):
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
        recipe_data = None
        return recipe_data
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_20(ai_output):
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
        print("XXJSON decoding error:XX", e)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_21(ai_output):
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
        print("JSON decoding error:", None)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_22(ai_output):
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
        print("JSON decoding error:",)
        print("Raw AI output:", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_23(ai_output):
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
        print("XXRaw AI output:XX", ai_output)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_24(ai_output):
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
        print("Raw AI output:", None)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_25(ai_output):
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
        print("Raw AI output:",)
        raise ValueError("Failed to parse AI response")

def x_parse_ai_response__mutmut_26(ai_output):
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
        raise ValueError("XXFailed to parse AI responseXX")

x_parse_ai_response__mutmut_mutants = {
'x_parse_ai_response__mutmut_1': x_parse_ai_response__mutmut_1, 
    'x_parse_ai_response__mutmut_2': x_parse_ai_response__mutmut_2, 
    'x_parse_ai_response__mutmut_3': x_parse_ai_response__mutmut_3, 
    'x_parse_ai_response__mutmut_4': x_parse_ai_response__mutmut_4, 
    'x_parse_ai_response__mutmut_5': x_parse_ai_response__mutmut_5, 
    'x_parse_ai_response__mutmut_6': x_parse_ai_response__mutmut_6, 
    'x_parse_ai_response__mutmut_7': x_parse_ai_response__mutmut_7, 
    'x_parse_ai_response__mutmut_8': x_parse_ai_response__mutmut_8, 
    'x_parse_ai_response__mutmut_9': x_parse_ai_response__mutmut_9, 
    'x_parse_ai_response__mutmut_10': x_parse_ai_response__mutmut_10, 
    'x_parse_ai_response__mutmut_11': x_parse_ai_response__mutmut_11, 
    'x_parse_ai_response__mutmut_12': x_parse_ai_response__mutmut_12, 
    'x_parse_ai_response__mutmut_13': x_parse_ai_response__mutmut_13, 
    'x_parse_ai_response__mutmut_14': x_parse_ai_response__mutmut_14, 
    'x_parse_ai_response__mutmut_15': x_parse_ai_response__mutmut_15, 
    'x_parse_ai_response__mutmut_16': x_parse_ai_response__mutmut_16, 
    'x_parse_ai_response__mutmut_17': x_parse_ai_response__mutmut_17, 
    'x_parse_ai_response__mutmut_18': x_parse_ai_response__mutmut_18, 
    'x_parse_ai_response__mutmut_19': x_parse_ai_response__mutmut_19, 
    'x_parse_ai_response__mutmut_20': x_parse_ai_response__mutmut_20, 
    'x_parse_ai_response__mutmut_21': x_parse_ai_response__mutmut_21, 
    'x_parse_ai_response__mutmut_22': x_parse_ai_response__mutmut_22, 
    'x_parse_ai_response__mutmut_23': x_parse_ai_response__mutmut_23, 
    'x_parse_ai_response__mutmut_24': x_parse_ai_response__mutmut_24, 
    'x_parse_ai_response__mutmut_25': x_parse_ai_response__mutmut_25, 
    'x_parse_ai_response__mutmut_26': x_parse_ai_response__mutmut_26
}

def parse_ai_response(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_ai_response__mutmut_orig, x_parse_ai_response__mutmut_mutants, *args, **kwargs)
    return result 

parse_ai_response.__signature__ = _mutmut_signature(x_parse_ai_response__mutmut_orig)
x_parse_ai_response__mutmut_orig.__name__ = 'x_parse_ai_response'



def x_main__mutmut_orig():
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

def x_main__mutmut_1():
    # Set your OpenAI API key
    openai.api_key = os.getenv("XXOPENAI_API_KEYXX")
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

def x_main__mutmut_2():
    # Set your OpenAI API key
    openai.api_key = None
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

def x_main__mutmut_3():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if  openai.api_key:
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

def x_main__mutmut_4():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("XXEnter your OpenAI API key: XX").strip()

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

def x_main__mutmut_5():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = None

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

def x_main__mutmut_6():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("XXEnter a recipe name or theme (leave blank for any): XX").strip()
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

def x_main__mutmut_7():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = None
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

def x_main__mutmut_8():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("XXEnter ingredients to include (comma-separated): XX").split(',')
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

def x_main__mutmut_9():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split('XX,XX')
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

def x_main__mutmut_10():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = None
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

def x_main__mutmut_11():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split(',')
    whitelist = None
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

def x_main__mutmut_12():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split(',')
    whitelist = [item.strip() for item in whitelist if item.strip()]
    blacklist = input("XXEnter ingredients to exclude (comma-separated): XX").split(',')
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

def x_main__mutmut_13():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split(',')
    whitelist = [item.strip() for item in whitelist if item.strip()]
    blacklist = input("Enter ingredients to exclude (comma-separated): ").split('XX,XX')
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

def x_main__mutmut_14():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split(',')
    whitelist = [item.strip() for item in whitelist if item.strip()]
    blacklist = None
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

def x_main__mutmut_15():
    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter your OpenAI API key: ").strip()

    # Get user inputs
    search_term = input("Enter a recipe name or theme (leave blank for any): ").strip()
    whitelist = input("Enter ingredients to include (comma-separated): ").split(',')
    whitelist = [item.strip() for item in whitelist if item.strip()]
    blacklist = input("Enter ingredients to exclude (comma-separated): ").split(',')
    blacklist = None

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

def x_main__mutmut_16():
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
    prompt = construct_prompt(None, whitelist, blacklist)
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

def x_main__mutmut_17():
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
    prompt = construct_prompt(search_term, None, blacklist)
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

def x_main__mutmut_18():
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
    prompt = construct_prompt(search_term, whitelist, None)
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

def x_main__mutmut_19():
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
    prompt = construct_prompt( whitelist, blacklist)
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

def x_main__mutmut_20():
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
    prompt = construct_prompt(search_term, blacklist)
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

def x_main__mutmut_21():
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
    prompt = construct_prompt(search_term, whitelist,)
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

def x_main__mutmut_22():
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
    prompt = None
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

def x_main__mutmut_23():
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
    print("XX\nPrompt sent to OpenAI:XX")
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

def x_main__mutmut_24():
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
    print(None)

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

def x_main__mutmut_25():
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
            model="XXgpt-3.5-turboXX",  # You can change the model if needed
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

def x_main__mutmut_26():
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
            messages=[{"XXroleXX": "user", "content": prompt}],
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

def x_main__mutmut_27():
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
            messages=[{"role": "XXuserXX", "content": prompt}],
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

def x_main__mutmut_28():
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
            messages=[{"role": "user", "XXcontentXX": prompt}],
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

def x_main__mutmut_29():
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
            max_tokens=801,
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

def x_main__mutmut_30():
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
            temperature=1.7,
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

def x_main__mutmut_31():
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
        response = openai.ChatCompletion.create(  # You can change the model if needed
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

def x_main__mutmut_32():
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
            model="gpt-3.5-turbo",
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

def x_main__mutmut_33():
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

def x_main__mutmut_34():
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

def x_main__mutmut_35():
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
        response = None
        ai_output = response.choices[0].message.content.strip()
        print("\nAI Output:")
        print(ai_output)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_36():
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
        ai_output = response.choices[1].message.content.strip()
        print("\nAI Output:")
        print(ai_output)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_37():
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
        ai_output = response.choices[None].message.content.strip()
        print("\nAI Output:")
        print(ai_output)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_38():
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
        ai_output = None
        print("\nAI Output:")
        print(ai_output)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_39():
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
        print("XX\nAI Output:XX")
        print(ai_output)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_40():
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
        print(None)

        # Parse the AI output
        recipe_data = parse_ai_response(ai_output)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_41():
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
        recipe_data = parse_ai_response(None)
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_42():
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
        recipe_data = None
        print("\nGenerated Recipe:")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_43():
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
        print("XX\nGenerated Recipe:XX")
        print(json.dumps(recipe_data, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_44():
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
        print(json.dumps(None, indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_45():
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
        print(json.dumps(recipe_data, indent=5))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_46():
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
        print(json.dumps( indent=4))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

def x_main__mutmut_47():
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
        print(json.dumps(recipe_data,))

    except Exception as e:
        print(f"Error during recipe generation: {e}")

x_main__mutmut_mutants = {
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13, 
    'x_main__mutmut_14': x_main__mutmut_14, 
    'x_main__mutmut_15': x_main__mutmut_15, 
    'x_main__mutmut_16': x_main__mutmut_16, 
    'x_main__mutmut_17': x_main__mutmut_17, 
    'x_main__mutmut_18': x_main__mutmut_18, 
    'x_main__mutmut_19': x_main__mutmut_19, 
    'x_main__mutmut_20': x_main__mutmut_20, 
    'x_main__mutmut_21': x_main__mutmut_21, 
    'x_main__mutmut_22': x_main__mutmut_22, 
    'x_main__mutmut_23': x_main__mutmut_23, 
    'x_main__mutmut_24': x_main__mutmut_24, 
    'x_main__mutmut_25': x_main__mutmut_25, 
    'x_main__mutmut_26': x_main__mutmut_26, 
    'x_main__mutmut_27': x_main__mutmut_27, 
    'x_main__mutmut_28': x_main__mutmut_28, 
    'x_main__mutmut_29': x_main__mutmut_29, 
    'x_main__mutmut_30': x_main__mutmut_30, 
    'x_main__mutmut_31': x_main__mutmut_31, 
    'x_main__mutmut_32': x_main__mutmut_32, 
    'x_main__mutmut_33': x_main__mutmut_33, 
    'x_main__mutmut_34': x_main__mutmut_34, 
    'x_main__mutmut_35': x_main__mutmut_35, 
    'x_main__mutmut_36': x_main__mutmut_36, 
    'x_main__mutmut_37': x_main__mutmut_37, 
    'x_main__mutmut_38': x_main__mutmut_38, 
    'x_main__mutmut_39': x_main__mutmut_39, 
    'x_main__mutmut_40': x_main__mutmut_40, 
    'x_main__mutmut_41': x_main__mutmut_41, 
    'x_main__mutmut_42': x_main__mutmut_42, 
    'x_main__mutmut_43': x_main__mutmut_43, 
    'x_main__mutmut_44': x_main__mutmut_44, 
    'x_main__mutmut_45': x_main__mutmut_45, 
    'x_main__mutmut_46': x_main__mutmut_46, 
    'x_main__mutmut_47': x_main__mutmut_47
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, *args, **kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'



if __name__ == "__main__":
    main()
