"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park.', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽', 'they']
# once 0 upon 2 a 7 time 9 a 7 boy 1 who 11 had 16 a 7 dog 3 and 14 a 7 girl 13 who 11 had 16 a 7 cat 12 met 5 and 14 went 15 to 10 play 17 with 6 a 7 ball 15.


story = [(words[0])]
story.append(words[2])
story.append(words[7])
story.append(words[9])
story.append(words[7])
story.append(words[1])
story.append(words[11])
story.append(words[16])
story.append(words[7])
story.append(words[3])
story.append(words[14])
story.append(words[7])
story.append(words[13])
story.append(words[11])
story.append(words[16])
story.append(words[7])
story.append(words[12])
story.append(words[5])
story.append(words[14])
story.append(words[15])
story.append(words[10])
story.append(words[17])
story.append(words[6])
story.append(words[7])
story.append(words[18])
story.append('at')
story.append(words[8])
story.append(words[4])
# Create a story using the words in the list


# Display the story to the user
print(' '.join(story))