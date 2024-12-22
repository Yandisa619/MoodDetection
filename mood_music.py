import openai 

openai.api_key = "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"


music_suggestions = {
    "sad": "Relaxing Playlist: https://open.spotify.com/album/2N1ab00YnjAe9TBxtg7YGx?si=3a1b241bd9b34431",
    "anxious": "Calm Piano: https://open.spotify.com/playlist/0eU3ubPAnqeSMi9K3YKVpC?si=KeedOZPdT8KdmQrh6fM5Dg",
    "tired": "Lo-Fi Beats: https://open.spotify.com/album/3LPtPgP1veXoKEuPzHjtOY?si=4K5521AhT_WjDfUz0gmiDQ",
    "happy": "Feel-Good Hits: https://open.spotify.com/playlist/37i9dQZF1E4wSqZ5Zcfoee?si=W76VWaF0So6rKmahxES0QA",
}

 

youtube_video_suggestions = {
    "sad": "5 Minute Meditation for Relaxation: https://youtu.be/b4pP6HyXRMI?si=1eb-sqrDPhhKAUvX",
    "anxious": "How to Calm Anxiety: https://youtu.be/mKW4ZFP8bGY?si=IOUqV4q0v4Kyh5Ay",
    "tired": "Energy Boosting Techniques: https://youtu.be/w5XCvxI0Tjk?si=2xHvOfY8pu_labrF",
    "happy": "How to Stay Happy: https://youtu.be/r4ZdyS6v3qA?si=dVtPcZfKV6-E_Xll",
}
def suggest_music(mood):
    """Suggests music based on the identified mood."""
    return music_suggestions.get(mood.lower(), "Here's a general calming playlist: https://open.spotify.com/playlist/37i9dQZF1DX6sHwck3IBzT?si=xVTZQu6gSkeN8wbVloOCmQ")

def suggest_video(mood):
    """Suggests YouTube video based on the identified mood. """
    return youtube_video_suggestions.get(mood.lower(), "Here's a general relaxation video: https://youtu.be/tbnzAVRZ9Xc?si=q929XxieZ4rxxeyi")

def main():
    print("Welcome to the Mood-Centered Music and Video Suggestion App!")
    user_input = input("How are you feeling today? ")

    
    mood_keywords = {
        "sad": "sad",
        "anxious": "anxious",
        "tired": "tired",
        "happy": "happy",
    }

    detected_mood = "general"  
    for keyword, mood in mood_keywords.items():
        if keyword in user_input.lower():
            detected_mood = mood
            break

    print(f"Detected Mood: {detected_mood}")

    music_suggestion = suggest_music(detected_mood)
    video_suggestion = suggest_video(detected_mood)

    print(f"Music Suggestion: {music_suggestion}")
    print(f"YouTube Video Suggestion: {video_suggestion}")
if __name__ == "__main__":
    main()
