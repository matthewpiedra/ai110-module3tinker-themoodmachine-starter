"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "I had a hella dope coffee this morning, lowkey feeling great",
    "😂 Something terrible happened today. Can't wait to reveal later",
    "I absolutely love getting stuck in traffic, it's the best part of my day",
    "Well, that exam went great",
    "That professor can do a better job at explaining the subject",
    "I'm scared to fail the final exam",
    "no cap this final literally ruined my whole week 💀",
    "highkey obsessed with this playlist rn, on repeat all day",
    "lol love how my wifi dies every single time I have a deadline",
    "kinda nervous about the interview but also weirdly hyped 🙃",
    "Excited to come back home now. I was stressed the whole day.",
    "I hate to walk to school"
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "I had a hella dope coffee this morning, lowkey feeling great",
    "positive",     # "😂 Something terrible happened today. Can't wait to reveal later"
    "negative",     # "I absolutely love getting stuck in traffic, it's the best part of my day"
    "negative" ,     # "Well, that exam went great"
    "negative",     # "That professor can do a better job at explaining the subject"
    "negative",     # "I'm scared to fail the final exam"
    "negative",     # "no cap this final literally ruined my whole week 💀"
    "positive",    # "highkey obsessed with this playlist rn, on repeat all day
    "negative",     # "lol love how my wifi dies every single time I have a deadline"
    "mixed",     # "kinda nervous about the interview but also weirdly hyped
    "positive",     # "Excited to come back home now. I was stressed the whole day.
    "negative"      # "I hate to walk to school"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
