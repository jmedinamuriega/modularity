import random
def mood_response(mood):
    moods_bad = ['sad', 'angry', 'frustrated', 'anxious', 'stressed', 'tired', 'bored', 'lonely', 'disappointed', 'overwhelmed']
    moods_good = ['happy', 'excited', 'relaxed', 'content', 'energetic', 'focused', 'proud', 'grateful', 'inspired', 'peaceful']
    if mood in moods_bad:
        return "I hope your day gets better!"
    elif mood in moods_good:
        return "I am happy to hear that!"
    else:
        return "I don't understand that feeling, I am a robot"