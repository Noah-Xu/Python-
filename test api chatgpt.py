import openai
openai.api_key = "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"
def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    print(message)
askChatGPT("请告诉我中国的国土面积有多大")