import json
import os
from openai import OpenAI
from api_connections import open_ai_key

example_profile = {"user1":
{
  "username": "minecraft_builder123",
  "account_info": {
    "created_at": "2022-05-16T12:34:56Z",
    "karma": {
      "post_karma": 5345,
      "comment_karma": 2487,
      "total_karma": 7832
    },
    "awards_received": 10
  },
  "subreddits_participating": [
    {
      "name": "r/Minecraft",
      "subscribed_since": "2022-06-01T08:15:30Z",
      "flair": "Redstone Engineer"
    },
    {
      "name": "r/MinecraftBuilds",
      "subscribed_since": "2022-06-10T10:25:00Z",
      "flair": "Master Builder"
    },
    {
      "name": "r/Redstone",
      "subscribed_since": "2022-07-05T09:10:45Z",
      "flair": None
    },
    {
      "name": "r/MinecraftMemes",
      "subscribed_since": "2023-01-20T12:00:00Z",
      "flair": None
    },
    {
      "name": "r/MinecraftSuggestions",
      "subscribed_since": "2023-02-10T11:30:00Z",
      "flair": None
    }
  ],
  "posts": [
    {
      "post_id": "abc123",
      "subreddit": "r/Minecraft",
      "title": "Check out my latest redstone contraption!",
      "content": "I spent over a week designing this automatic crop farm. It's fully powered by redstone, and I managed to optimize it so it produces about 200 crops per hour! I've included a step-by-step guide in the video linked below for anyone interested in replicating it. Thoughts and feedback are appreciated!",
      "post_url": "https://www.reddit.com/r/Minecraft/comments/abc123/",
      "upvotes": 456,
      "downvotes": 12,
      "awards_received": 3,
      "created_at": "2023-10-10T15:22:13Z",
      "comments": [
        {
          "comment_id": "comment_1",
          "author": "minecraft_enthusiast",
          "content": "Wow, this is amazing! Can you share the world file? I'd love to experiment with your design and maybe tweak it a bit!",
          "upvotes": 50,
          "downvotes": 1,
          "created_at": "2023-10-10T16:30:25Z"
        },
        {
          "comment_id": "comment_2",
          "author": "minecraft_builder123",
          "content": "Thanks! Sure thing. Here’s the world file download link: [world file link]. Let me know how your tweaks turn out!",
          "upvotes": 75,
          "downvotes": 0,
          "created_at": "2023-10-10T17:00:45Z"
        }
      ]
    },
    {
      "post_id": "def456",
      "subreddit": "r/MinecraftBuilds",
      "title": "My medieval castle build - thoughts?",
      "content": "Hey everyone! After spending a month working on this medieval castle, I finally finished it. The build includes a fully furnished interior, towers, battlements, and a working drawbridge. I’m pretty proud of how it turned out, but I’d love to get your feedback on the design and detailing.",
      "post_url": "https://www.reddit.com/r/MinecraftBuilds/comments/def456/",
      "upvotes": 789,
      "downvotes": 8,
      "awards_received": 2,
      "created_at": "2023-09-25T13:12:00Z",
      "comments": [
        {
          "comment_id": "comment_3",
          "author": "block_master",
          "content": "This is incredible! I love the attention to detail in the stonework and how you've mixed cobblestone with mossy blocks to give it that ancient feel.",
          "upvotes": 100,
          "downvotes": 2,
          "created_at": "2023-09-25T14:45:12Z"
        },
        {
          "comment_id": "comment_4",
          "author": "minecraft_builder123",
          "content": "Thanks! Yeah, I tried to give the castle an aged look. The mossy cobblestone really helped achieve that effect!",
          "upvotes": 55,
          "downvotes": 1,
          "created_at": "2023-09-25T15:30:25Z"
        }
      ]
    },
    {
      "post_id": "ghi789",
      "subreddit": "r/Redstone",
      "title": "Redstone circuitry tip for newbies",
      "content": "For anyone struggling with redstone, using comparators can significantly reduce the tick delay in your circuits. A lot of beginners overlook comparators, but they’re key for more complex contraptions. Here’s a quick guide explaining how they work and how you can incorporate them into your designs.",
      "post_url": "https://www.reddit.com/r/Redstone/comments/ghi789/",
      "upvotes": 305,
      "downvotes": 6,
      "awards_received": 1,
      "created_at": "2023-08-20T16:00:45Z",
      "comments": [
        {
          "comment_id": "comment_5",
          "author": "redstone_learner",
          "content": "This helped a lot! I was struggling with the delay on my automatic smelter, and adding the comparator solved it. Thanks!",
          "upvotes": 65,
          "downvotes": 0,
          "created_at": "2023-08-20T17:30:15Z"
        },
        {
          "comment_id": "comment_6",
          "author": "minecraft_builder123",
          "content": "Glad to hear it! Comparators are super useful once you get the hang of them. Let me know if you need any more help!",
          "upvotes": 30,
          "downvotes": 0,
          "created_at": "2023-08-20T18:15:45Z"
        }
      ]
    },
    {
      "post_id": "jkl987",
      "subreddit": "r/MinecraftMemes",
      "title": "When you find diamonds but then fall into lava...",
      "content": "[Image meme] Caption: 'Me after finding diamonds: I'm rich! *Lava: I'm about to end this man's whole career*'. Thought this was relatable after last night’s session... Lost 8 diamonds and full iron gear. FML.",
      "post_url": "https://www.reddit.com/r/MinecraftMemes/comments/jkl987/",
      "upvotes": 1200,
      "downvotes": 30,
      "awards_received": 5,
      "created_at": "2023-07-15T12:22:13Z",
      "comments": [
        {
          "comment_id": "comment_7",
          "author": "creeper_expert",
          "content": "Happens every time! Lava is the true final boss of Minecraft. RIP those diamonds.",
          "upvotes": 400,
          "downvotes": 5,
          "created_at": "2023-07-15T13:30:00Z"
        },
        {
          "comment_id": "comment_8",
          "author": "minecraft_builder123",
          "content": "I know, right? I even had a water bucket on me and STILL couldn’t save myself!",
          "upvotes": 350,
          "downvotes": 2,
          "created_at": "2023-07-15T14:00:00Z"
        }
      ]
    },
    {
      "post_id": "mno654",
      "subreddit": "r/MinecraftSuggestions",
      "title": "New biomes idea: Crystal Caverns",
      "content": "Imagine an underground biome filled with glowing crystals, bioluminescent plants, and unique mobs that drop rare resources. These caverns could be a treasure trove for explorers, with some of the crystals being useful for crafting new items like light sources or enchantment-boosting tools. Thoughts?",
      "post_url": "https://www.reddit.com/r/MinecraftSuggestions/comments/mno654/",
      "upvotes": 650,
      "downvotes": 25,
      "awards_received": 4,
      "created_at": "2023-06-05T10:22:13Z",
      "comments": [
        {
          "comment_id": "comment_9",
          "author": "idea_miner",
          "content": "That sounds amazing! It would definitely add more excitement to underground exploration. And the crystals could look so cool with Minecraft's lighting engine.",
          "upvotes": 175,
          "downvotes": 4,
          "created_at": "2023-06-05T11:15:45Z"
        },
        {
          "comment_id": "comment_10",
          "author": "minecraft_builder123",
          "content": "Exactly! I was thinking the glowing crystals could even be used as environmental hazards—like they could damage mobs that touch them.",
          "upvotes": 150,
          "downvotes": 1,
          "created_at": "2023-06-05T11:45:30Z"
        }
      ]
    }
  ],
  "comments": [
    {
      "comment_id": "comment_11",
      "post_id": "rst852",
      "subreddit": "r/Minecraft",
      "content": "The new Caves & Cliffs update is absolutely incredible! I can’t believe how much more depth (literally) they’ve added to the underground. I’ve spent hours just exploring caves and mining for resources.",
      "upvotes": 250,
      "downvotes": 10,
      "created_at": "2023-04-10T15:30:45Z"
    },
    {
      "comment_id": "comment_12",
      "post_id": "uvw123",
      "subreddit": "r/MinecraftBuilds",
      "content": "Your underwater base is amazing! I’m curious, though—how did you manage to keep the water out while you were building? Sponges or a clever trick with doors?",
      "upvotes": 300,
      "downvotes": 12,
      "created_at": "2023-05-05T17:10:15Z"
    },
    {
      "comment_id": "comment_13",
      "post_id": "xyz456",
      "subreddit": "r/Redstone",
      "content": "For anyone having trouble with redstone doors, I highly recommend using sticky pistons and making sure you space out your repeaters to get the perfect timing. It’ll save you a ton of frustration.",
      "upvotes": 200,
      "downvotes": 7,
      "created_at": "2023-03-15T11:22:35Z"
    },
    {
      "comment_id": "comment_14",
      "post_id": "rst852",
      "subreddit": "r/Minecraft",
      "content": "Agreed, the cliffs are absolutely breathtaking. It really feels like Mojang went all out with this update!",
      "upvotes": 225,
      "downvotes": 3,
      "created_at": "2023-04-11T14:20:45Z"
    },
    {
      "comment_id": "comment_15",
      "post_id": "uvw456",
      "subreddit": "r/MinecraftMemes",
      "content": "Skeletons with enchanted bows are nightmare fuel. I swear they have better aim than the Ender Dragon!",
      "upvotes": 500,
      "downvotes": 20,
      "created_at": "2023-06-12T19:00:25Z"
    }
  ],
  "saved_posts": [
    {
      "post_id": "qrs852",
      "subreddit": "r/Minecraft",
      "title": "A comprehensive guide to finding netherite",
      "post_url": "https://www.reddit.com/r/Minecraft/comments/qrs852/"
    }
  ]
},
"user2": {
  "username": "minecraft_builder123",
  "account_info": {
    "created_at": "2022-05-16T12:34:56Z",
    "karma": {
      "post_karma": 5345,
      "comment_karma": 2487,
      "total_karma": 7832
    },
    "awards_received": 10
  },
  "subreddits_participating": [
    {
      "name": "r/Minecraft",
      "subscribed_since": "2022-06-01T08:15:30Z",
      "flair": "Redstone Engineer"
    },
    {
      "name": "r/MinecraftBuilds",
      "subscribed_since": "2022-06-10T10:25:00Z",
      "flair": "Master Builder"
    },
    {
      "name": "r/Redstone",
      "subscribed_since": "2022-07-05T09:10:45Z",
      "flair": None
    },
    {
      "name": "r/MinecraftMemes",
      "subscribed_since": "2023-01-20T12:00:00Z",
      "flair": None
    },
    {
      "name": "r/MinecraftSuggestions",
      "subscribed_since": "2023-02-10T11:30:00Z",
      "flair": None
    }
  ],
  "posts": [
    {
      "post_id": "abc123",
      "subreddit": "r/Minecraft",
      "title": "Check out my latest redstone contraption!",
      "content": "I spent over a week designing this automatic crop farm. It's fully powered by redstone, and I managed to optimize it so it produces about 200 crops per hour! I've included a step-by-step guide in the video linked below for anyone interested in replicating it. Thoughts and feedback are appreciated!",
      "post_url": "https://www.reddit.com/r/Minecraft/comments/abc123/",
      "upvotes": 456,
      "downvotes": 12,
      "awards_received": 3,
      "created_at": "2023-10-10T15:22:13Z",
      "comments": [
        {
          "comment_id": "comment_1",
          "author": "minecraft_enthusiast",
          "content": "Wow, this is amazing! Can you share the world file? I'd love to experiment with your design and maybe tweak it a bit!",
          "upvotes": 50,
          "downvotes": 1,
          "created_at": "2023-10-10T16:30:25Z"
        },
        {
          "comment_id": "comment_2",
          "author": "minecraft_builder123",
          "content": "Thanks! Sure thing. Here’s the world file download link: [world file link]. Let me know how your tweaks turn out!",
          "upvotes": 75,
          "downvotes": 0,
          "created_at": "2023-10-10T17:00:45Z"
        }
      ]
    },
    {
      "post_id": "def456",
      "subreddit": "r/MinecraftBuilds",
      "title": "My medieval castle build - thoughts?",
      "content": "Hey everyone! After spending a month working on this medieval castle, I finally finished it. The build includes a fully furnished interior, towers, battlements, and a working drawbridge. I’m pretty proud of how it turned out, but I’d love to get your feedback on the design and detailing.",
      "post_url": "https://www.reddit.com/r/MinecraftBuilds/comments/def456/",
      "upvotes": 789,
      "downvotes": 8,
      "awards_received": 2,
      "created_at": "2023-09-25T13:12:00Z",
      "comments": [
        {
          "comment_id": "comment_3",
          "author": "block_master",
          "content": "This is incredible! I love the attention to detail in the stonework and how you've mixed cobblestone with mossy blocks to give it that ancient feel.",
          "upvotes": 100,
          "downvotes": 2,
          "created_at": "2023-09-25T14:45:12Z"
        },
        {
          "comment_id": "comment_4",
          "author": "minecraft_builder123",
          "content": "Thanks! Yeah, I tried to give the castle an aged look. The mossy cobblestone really helped achieve that effect!",
          "upvotes": 55,
          "downvotes": 1,
          "created_at": "2023-09-25T15:30:25Z"
        }
      ]
    },
    {
      "post_id": "ghi789",
      "subreddit": "r/Redstone",
      "title": "Redstone circuitry tip for newbies",
      "content": "For anyone struggling with redstone, using comparators can significantly reduce the tick delay in your circuits. A lot of beginners overlook comparators, but they’re key for more complex contraptions. Here’s a quick guide explaining how they work and how you can incorporate them into your designs.",
      "post_url": "https://www.reddit.com/r/Redstone/comments/ghi789/",
      "upvotes": 305,
      "downvotes": 6,
      "awards_received": 1,
      "created_at": "2023-08-20T16:00:45Z",
      "comments": [
        {
          "comment_id": "comment_5",
          "author": "redstone_learner",
          "content": "This helped a lot! I was struggling with the delay on my automatic smelter, and adding the comparator solved it. Thanks!",
          "upvotes": 65,
          "downvotes": 0,
          "created_at": "2023-08-20T17:30:15Z"
        },
        {
          "comment_id": "comment_6",
          "author": "minecraft_builder123",
          "content": "Glad to hear it! Comparators are super useful once you get the hang of them. Let me know if you need any more help!",
          "upvotes": 30,
          "downvotes": 0,
          "created_at": "2023-08-20T18:15:45Z"
        }
      ]
    },
    {
      "post_id": "jkl987",
      "subreddit": "r/MinecraftMemes",
      "title": "When you find diamonds but then fall into lava...",
      "content": "[Image meme] Caption: 'Me after finding diamonds: I'm rich! *Lava: I'm about to end this man's whole career*'. Thought this was relatable after last night’s session... Lost 8 diamonds and full iron gear. FML.",
      "post_url": "https://www.reddit.com/r/MinecraftMemes/comments/jkl987/",
      "upvotes": 1200,
      "downvotes": 30,
      "awards_received": 5,
      "created_at": "2023-07-15T12:22:13Z",
      "comments": [
        {
          "comment_id": "comment_7",
          "author": "creeper_expert",
          "content": "Happens every time! Lava is the true final boss of Minecraft. RIP those diamonds.",
          "upvotes": 400,
          "downvotes": 5,
          "created_at": "2023-07-15T13:30:00Z"
        },
        {
          "comment_id": "comment_8",
          "author": "minecraft_builder123",
          "content": "I know, right? I even had a water bucket on me and STILL couldn’t save myself!",
          "upvotes": 350,
          "downvotes": 2,
          "created_at": "2023-07-15T14:00:00Z"
        }
      ]
    },
    {
      "post_id": "mno654",
      "subreddit": "r/MinecraftSuggestions",
      "title": "New biomes idea: Crystal Caverns",
      "content": "Imagine an underground biome filled with glowing crystals, bioluminescent plants, and unique mobs that drop rare resources. These caverns could be a treasure trove for explorers, with some of the crystals being useful for crafting new items like light sources or enchantment-boosting tools. Thoughts?",
      "post_url": "https://www.reddit.com/r/MinecraftSuggestions/comments/mno654/",
      "upvotes": 650,
      "downvotes": 25,
      "awards_received": 4,
      "created_at": "2023-06-05T10:22:13Z",
      "comments": [
        {
          "comment_id": "comment_9",
          "author": "idea_miner",
          "content": "That sounds amazing! It would definitely add more excitement to underground exploration. And the crystals could look so cool with Minecraft's lighting engine.",
          "upvotes": 175,
          "downvotes": 4,
          "created_at": "2023-06-05T11:15:45Z"
        },
        {
          "comment_id": "comment_10",
          "author": "minecraft_builder123",
          "content": "Exactly! I was thinking the glowing crystals could even be used as environmental hazards—like they could damage mobs that touch them.",
          "upvotes": 150,
          "downvotes": 1,
          "created_at": "2023-06-05T11:45:30Z"
        }
      ]
    }
  ],
  "comments": [
    {
      "comment_id": "comment_11",
      "post_id": "rst852",
      "subreddit": "r/Minecraft",
      "content": "The new Caves & Cliffs update is absolutely incredible! I can’t believe how much more depth (literally) they’ve added to the underground. I’ve spent hours just exploring caves and mining for resources.",
      "upvotes": 250,
      "downvotes": 10,
      "created_at": "2023-04-10T15:30:45Z"
    },
    {
      "comment_id": "comment_12",
      "post_id": "uvw123",
      "subreddit": "r/MinecraftBuilds",
      "content": "Your underwater base is amazing! I’m curious, though—how did you manage to keep the water out while you were building? Sponges or a clever trick with doors?",
      "upvotes": 300,
      "downvotes": 12,
      "created_at": "2023-05-05T17:10:15Z"
    },
    {
      "comment_id": "comment_13",
      "post_id": "xyz456",
      "subreddit": "r/Redstone",
      "content": "For anyone having trouble with redstone doors, I highly recommend using sticky pistons and making sure you space out your repeaters to get the perfect timing. It’ll save you a ton of frustration.",
      "upvotes": 200,
      "downvotes": 7,
      "created_at": "2023-03-15T11:22:35Z"
    },
    {
      "comment_id": "comment_14",
      "post_id": "rst852",
      "subreddit": "r/Minecraft",
      "content": "Agreed, the cliffs are absolutely breathtaking. It really feels like Mojang went all out with this update!",
      "upvotes": 225,
      "downvotes": 3,
      "created_at": "2023-04-11T14:20:45Z"
    },
    {
      "comment_id": "comment_15",
      "post_id": "uvw456",
      "subreddit": "r/MinecraftMemes",
      "content": "Skeletons with enchanted bows are nightmare fuel. I swear they have better aim than the Ender Dragon!",
      "upvotes": 500,
      "downvotes": 20,
      "created_at": "2023-06-12T19:00:25Z"
    }
  ],
  "saved_posts": [
    {
      "post_id": "qrs852",
      "subreddit": "r/Minecraft",
      "title": "A comprehensive guide to finding netherite",
      "post_url": "https://www.reddit.com/r/Minecraft/comments/qrs852/"
    }
  ]
}
}

def summarize_gaming_activity(profile_data):
  #profile_string = json.dumps(profile_data)

  # Define the prompt
  # question = profile_string + "Using the inputted json of multiple reddit users profiles above, for each user return a list of 5 games and 5 game genres the user might be interested in in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}'"
  question = str(profile_data) + " Using the inputted json of multiple reddit users profiles above, for each user return a list of up to 5 games the user definitely plays and 5 game genres the user might be interested in in json format following this example '{user1: {Games: (List of names of games), Game Genres: (List of names of genres)}, ...}'"

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
  return chat_completion.choices[0].message.content

# Print the response
#print("Answer:", summarize_gaming_activity(example_profile))
