import os
import openai
import argparse
import re
from typing import List

openai.api_key = ("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")

Max_Input_Lengeh = 32

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--input","-i",type=str,required=True)
  args = parser.parse_args()
  user_input = args.input

  print(f"User input: {user_input}")
  if validate_length(user_input):
    generate_branding_snippet(user_input)
    generate_keywords(user_input)
  else:
    raise ValueError(
      f"Input length is too long. You must enter the keywords less character less than {Max_Input_Lengeh} .Submitted input is"
      f"{user_input}"
    )


# 这里是输入length的认证
def validate_length(prompt:str) ->bool:
  return len(prompt) <= Max_Input_Lengeh


# 这里是广告词
def generate_branding_snippet(prompt:str)->str:
  openai.api_key = ("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")
  enriched_prompt=f"Generate upbeat branding snippet for  {prompt}"
  print(enriched_prompt)
  response=openai.Completion.create(
    engine="text-davinci-002",
    prompt=enriched_prompt,
    max_tokens=32
  )
# Extract output text.
  branding_text: str = response["choices"][0]["text"]

  # Strip whitespace.
  branding_text = branding_text.strip()

  # Add ... to truncated statements.
  last_char = branding_text[-1]
  if last_char not in {".", "!", "?"}:
      branding_text += "..."

  print(f"Snippet: {branding_text}")
  return branding_text


# 这里是keywords
def generate_keywords(prompt: str) -> List[str]:
  openai.api_key = ("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")
  enriched_prompt = f"Generate related branding keywords for {prompt}: "
  print(enriched_prompt)
  response=openai.Completion.create(
    engine="text-davinci-002",
    prompt=enriched_prompt,
    max_tokens=32
  )
  # Extract output text.
  keywords_text: str = response["choices"][0]["text"]

  # Strip whitespace.
  keywords_text = keywords_text.strip()
  keywords_array = re.split(",|\n|;|-", keywords_text)
  keywords_array = [k.lower().strip() for k in keywords_array]
  keywords_array = [k for k in keywords_array if len(k) > 0]

  print(f"Keywords: {keywords_array}")
  return keywords_array

if __name__ == "__main__":
    main()