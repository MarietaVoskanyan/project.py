import random
x=random.randint(1,3)
inp=input('Choose the template by typing 1, 2 or 3: ')
print('Now please input the words')
try:
    if x==1:    
        number=int(input('Input the number: '))
        m_of_time=input('Input the measure of time: ')
        m_of_transportation=input('Input the mode of transportation: ')
        adjective=input('Input the adjective: ')
        adjective2=input('Input the adjective: ')
        noun=input('Input the noun: ')
        color=input('Input the color: ')
        p_of_the_b=input('Input the part of the body: ')
        verb=input('Input the verb: ')
        number2=int(input('Input the number: '))
        noun2=input('Input the noun: ')
        noun3=input('Input the noun: ')
        p_of_the_b2=input('Input the part of the body: ')
        noun4=input('Input the noun: ')
        adjective3=input('Input the adjective: ')
        silly_word=input('Input the silly word: ')
        print('It was about %d %s ago when I arrived at the hospital in a %s. The hospital is a/an %s place, there are a lot of %s %s here. There are nurses here who have %s %s. If someone wants to come into my room I told them that they have to %s first. I’ve decorated my room with %d %s. Today I talked to a doctor and they were wearing a %s on their %s. I heard that all doctors %s %s every day for breakfast. The most %s thing about being in the hospital is the %s %s !' % (number, m_of_time, m_of_transportation, adjective, adjective2, noun, color, p_of_the_b, verb, number2, noun2, noun3, p_of_the_b2, verb, noun4, adjective3, silly_word, noun))


    if x==2:    
        proper_noun=input('Input the proper noun (person’s name): ')
        noun=input('Input the noun: ')
        adjective=input('Input the adjective(feeling): ')
        verb=input('Input the verb: ')
        adjective2=input('Input the adjective(feeling): ')
        animal=input('Input the animal: ')
        verb2=input('Input the verb: ')
        color=input('Input the color: ')
        verb3=input('Input the verb(ending in ing): ')
        adverb=(input('Input the adverb (ending in ly): '))
        number=int(input('Input the number: '))
        m_of_time=input('Input the measure of time: ')
        silly_word=input('Input the silly word: ')
        noun2=input('Input the noun: ')
        print('This weekend I am going camping with %s. I packed my lantern, sleeping bag, and %s. I am so %s to %s in a tent. I am %s we might see a(n) %s, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and %s. I have heard that the %s lake is great for %s. Then we will %s hike through the forest for %d %s. If I see a %s %s while hiking, I am going to bring it home as a pet! At night we will tell %d %s stories and roast %s around the campfire!!' % (proper_noun, noun, adjective, verb, adjective2, animal, verb2, color, verb3, adverb, number, m_of_time, color, animal, number, silly_word, noun2))


    if x==3:
        proper_noun=input('Input theProper Noun (Person’s Name): ')
        adjective=input('Input the adjective: ')
        color=input('Input the color: ')
        animal=input('Input the animal: ')
        place=input('Input the place: ')
        adjective2=input('Input the adjective: ')
        magical_creature=input('Input the magical creature (plural): ')        
        adjective3=input('Input the adjective: ')
        magical_creature2=input('Input the magical creature (plural): ')        
        room_in_a_house=input('Input the room in a house: ')
        noun=input('Input the noun: ')
        noun2=input('Input the noun: ')
        noun3=input('Input the noun(plural): ')
        adjective4=input('Input the adjective: ')
        noun4=input('Input the noun(plural): ')
        number=int(input('Input the number: '))
        m_of_time=input('Input the measure of time: ')
        verb=input('Input the verb(ending in ing): ')
        adjective5=input('Input the adjective: ')
        noun5=input('Input the noun(plural): ')
        print('Dear %s, I am writing to you from a %s castle in an enchanted forest. I found myself here one day after going for a ride on a %s %s in %s. There are %s %s and %s %s here! In the %s there is a pool full of %s. I fall asleep each night on a %s of %s and dream of %s %s. It feels as though I have lived here for %d %s. I hope one day you can visit, although the only way to get here now is %s on a %s %s!!' % (proper_noun, adjective, color, animal, place, adjective2, magical_creature, adjective3, magical_creature2, room_in_a_house, noun, noun2, noun3, adjective4, noun4, number, m_of_time, verb, adjective5, noun5))
except:
    print("Enter the number")




    
 
    
