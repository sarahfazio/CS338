import json
import os
from openai import OpenAI
from api_connections import open_ai_key

from user_profiles import example_profile, example_user_profile, user_profile

def gpt_call_first(profile_data):

  question = str(profile_data) + " Using the inputted json of multiple reddit users profiles above, for each user return a list of up to 5 games the user definitely plays and up to 5 game genres the user might be interested in in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}'"
  
  # Make the API call
  client = OpenAI(
      # This is the default and can be omitted
      api_key= open_ai_key(),
  )

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          }
      ],
      model="gpt-4o",
  )

  response = chat_completion.choices[0].message.content
  #response = json.dumps(response)
  response = response.replace("json","")
  response = response.split("```")[1]
  response = json.loads(response)
  #response = json.loads(response[3:-3])
  return response

def length_checker(profile_data):
  if len(str(profile_data)) > 30000:
    if len(profile_data) == 1:
      return {}
    x = int(len(profile_data)/2)
    profile_data1 = profile_data[:x]
    profile_data2 = profile_data[x:]
    res1 = length_checker(profile_data1)
    res2 = length_checker(profile_data2)
    response = {**res1,**res2}
    return response
  else:
    return gpt_call_first(profile_data)
  


def summarize_gaming_activity(profile_data, comparison_profile=user_profile, compare = True):

  #profile_string = json.dumps(profile_data)

  # Define the prompt
  # question = profile_string + "Using the inputted json of multiple reddit users profiles above, for each user return a list of 5 games and 5 game genres the user might be interested in in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}'"
  #profile_array = [profile_data[:5], profile_data[5:10]]
  #second_question = str(profile_array[1]) + " Using the inputted json of multiple reddit users profiles above, for each user return a list of up to 5 games the user definitely plays and up to 5 game genres the user might be interested in in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}'"
  
  # Make the API call
  client = OpenAI(
      # This is the default and can be omitted
      api_key= open_ai_key(),
  )

  # chat_completion = client.chat.completions.create(
  #     messages=[
  #         {
  #             "role": "user",
  #             "content": question,
  #         }
  #     ],
  #     model="gpt-4o",
  # )

  # second_chat_completion = client.chat.completions.create(
  #     messages=[
  #         {
  #             "role": "user",
  #             "content": second_question,
  #         }
  #     ],
  #     model="gpt-4o",
  # )

  # response = chat_completion.choices[0].message.content
  # response = json.dumps(response)
  # response = response.replace("json","")
  # response = json.loads(response)
  # response = json.loads(response[3:-3])
  # response2 = second_chat_completion.choices[0].message.content
  # response2 = json.dumps(response2)
  # response2 = response2.replace("json","")
  # response2 = json.loads(response2)
  # response2 = json.loads(response2[3:-3])
  #response.update(response2)
  response = length_checker(profile_data)

  if compare:
    question2 = str(response) + " Use this outputted json to select only the 5 users that best matches the profile below based on the similarity between the games they play and game genres they play returning only a json of the list of users in order of similarity with all the games and game genres they play in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}' " + str(comparison_profile)
  else:
    print("Generating summary without stored comparison")
    question2 = str(response) + "Using the inputted json of multiple reddit users profiles above, for each user return a list of 5 games and 5 game genres the user might be interested in in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}'"


  chat_completion2 = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question2,
          }
      ],
      model="gpt-4o",
  )

  match_response = chat_completion2.choices[0].message.content
  match_response = match_response.replace("json","")
  match_response = match_response.split("```")[1]
  match_response = json.loads(match_response)

  return match_response

# Print the response
#print("Answer:", summarize_gaming_activity(example_profile))

def summarize_user_profile(profile_data):
  #profile_data = example_user_profile
  question = str(profile_data) + "Using the inputted json of a reddit user profile above, return a list of up to 5 games the user definitely plays, up to 5 game genres the user might be interested in, a summary of the game and game types the user plays and enjoys, up to 5 interests the user has outside of gaming, and a summary of these non gaming interests in json format following this example '{Gaming: {Games: (List of names of games), Game Genres: (List of names of genres)}, Gaming Summary: (Summary of enjoyed games and game types), Non Gaming Interests: {Interests: (List of non gaming interests), Interest Summary: (Summary of non gaming interests)}}'"

  # Make the API call
  client = OpenAI(
      # This is the default and can be omitted
      api_key= open_ai_key(),
  )

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          }
      ],
      model="gpt-4o",
  )

  response = chat_completion.choices[0].message.content
  response = response.replace("json","")
  response = response.split("```")[1]
  response = json.loads(response)

  return response

#print(summarize_user_profile("y"))