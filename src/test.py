import os

if __name__ == "__main__":

    from openai import OpenAI
    api_key = os.getenv('OPENAI_API_KEY')

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": "Write a one-sentence bedtime story about a unicorn."
            }
        ]
    )

    print(completion.choices[0].message.content)