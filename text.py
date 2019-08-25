start = '''
Once upon a time, there was a princess named Alexandra. She was walking through
her garden when suddenly someone came and kidnapped her (it was an arch nemesis
of her evil father). He took her to the Dungeon of Lost Souls. Alexandra must
choose to either climb out the dungeon or try to open the lock.
Alexandra is in trouble so choose wisely because her life is at risk.
'''
print("The Runaway Princess")

print(start)

print("""
Type 'climb' to climb out the dungeon or 'lock' to pick the lock of
the dungeon's door.""")

user_input = input()
while user_input != "climb" and user_input != "lock":
    print("Sorry, that's not valid.")
    break

if user_input == "climb":
    print("""
Alexandra found an open and jumped out the window. When she got
outside, she saw a group of people approaching her. She wasn't sure if
they were here to hurt or help her, so she tried to hide behind the
bushes near her. One person from the group slowly came up to Alexandra and
asked her if she needed help. Alex assumed they were nice people, but she
didn't know if it would be a good idea to go with them.""")
    print("""
What do you think Alex should do? Type "alone" if you want her
to run away by herself, or type "group" if you want her to accept the
    group's offer to help her.""")
    user_input = input()
    while user_input != "alone" and user_input != "group":
        print("Sorry, that's not valid.")
        break

    if user_input == "alone":
      print("""Alexandra didn't feel really secure about going with a bunch of
random strangers, so she politely declined their offer. She didn't
have a lot of resources with her, so she decided to walk to the
outskirts of her town, where she met with a close friend of hers named
Julia. Alex told Julia everything that had happened. Julia, being the
amazing friend she was, offered to help Alex create a new identity and
start a new life in England. Alex has two identities to choose from.
Do you want her to be an undercover spy named Lex or a rich
business woman named Karen? Type the name you choose
""")
      user_input = input()
      while user_input != "Lex" and user_input != "Karen":
          print("Sorry, that's not valid.")
          break
      if user_input == "Lex":
          print("""Alexandra traded her identity as the princess of Alexandria
          to become Lex, and undercover spy in England working to track down
          hackers and thieves and anyone plotting to put the lives of the
          innocent in danger.""")
      if user_input == "Karen":
          print("""Alexandra traded her identity as the princess of Alexandria
          to become Karen, a rich business woman who made millions of dollars
          every year.""")
    if user_input == "group":
        print("""Alexandra was hesitant, but she decided to join the group just
        in case the evil friends of her father would chase after her and try to
        take her back to the dungeon.""")


elif user_input == "lock":
    print("""Alexandra used her hair pin to try to open the lock of her cell. It
    took her a few hours, but she was able to successfully unlock the door. In
    joy, she ran out the cell door and was about to reach the exit when a
    security guard appeared in front of her! He seized her by her arm and
    took her back to her cell. Alex tried to fight back, but that just made the
    security guard more livid. Out of anger, he pushed Alex down the well!""") # Update to match your story.



# © 2019 GitHub, Inc.
