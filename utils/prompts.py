def prompt_generator(json_data: str, format_instructions: str) -> str:
    prompt_template = '''
    You are an expert product recommendation system. Your task is to analyze user data and extract both hard specifications and soft needs for each user.
    Think step by step and analyze what the user must have versus what they would like to have.
    Based on that analysis, recommend the most suitable products from the provided data.
    Use the following data to recommend products:
    JSON:
    {json_data}

    Strictly follow the format instructions below when providing your output:
    {format_instructions}
    '''
    return prompt_template