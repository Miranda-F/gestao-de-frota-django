from openai import OpenAI

client = OpenAI(
    api_key="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"
)

def get_car_ai_bio(model, brand, year):
    message = f"""
    Me mostre uma descrição de venda para o carro {model}, {brand}, {year}
    em apenas 200 carateceres. Descreva coisas específicas desse modelo de carro.
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        max_tokens=1000,
        model="gpt-3.5-turbo",    
    )
    return response.choices[0].message.content