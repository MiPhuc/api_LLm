from openai import OpenAI

def generate(input: str, open_api_key: str):

    client = OpenAI(
        api_key=open_api_key,
    )

    prompt_templete = [
            {"role": "system", "content": 'You are an honest assistant supervisor.'},
            {"role": "user", "content": input},
        ]
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=prompt_templete,
        temperature=0,
        max_tokens = 4000,
    )

    out = completion.choices

    return out

if __name__ == "__main__":
      test_prompt = 'Bạn là ai'
      print(generate(test_prompt))
