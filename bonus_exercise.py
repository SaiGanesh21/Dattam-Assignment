from groq import Groq

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama3-groq-8b-8192-tool-use-preview",
    messages=[
        {
            "role": "user",
            "content": "Write a python standalone script to detect language of input text and translate it to english"
        }
    ],
)
print(completion.choices[0].message.content)