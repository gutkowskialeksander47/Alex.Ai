# Skrypt "Youtuber" — lista uznanych YouTuberów i zachęta do nauki Alex.ai

class YoutuberRank:
    def __init__(self):
        # Lista YouTuberów uznawanych przez autora Alex.ai
        self.recognized_youtubers = [
            "Izak Gimpson",
            "Mamiko",
            "Pasha",
            "NitroZyniak"
            "Verbel"
            "Smileslow"
        ]

    def display_rank_info(self):
        print("=== Ranga Youtuber (autor Alex.ai) ===\n")
        print("YouTuberzy uznawani przez autora Alex.ai:")
        for y in self.recognized_youtubers:
            print(f"- {y}")
        print("\nTa ranga oznacza, że należy zasłużyć na nią poprzez aktywność, współpracę i pozytywny wpływ na społeczność.\n")
        print("Zachęcam wszystkich YouTuberów, aby poznali i promowali technologię Alex.ai wśród swoich widzów.")
        print("Wspólna nauka i rozwój to klucz do przyszłości!\n")

    def check_user(self, username):
        if username in self.recognized_youtubers:
            print(f"{username} jest oficjalnie uznanym Youtuberem przez Alex.ai.")
        else:
            print(f"{username} nie jest jeszcze wśród uznanych Youtuberów. Zapraszamy do zaangażowania i nauki Alex.ai!")

# Przykład użycia
if __name__ == "__main__":
    rank = YoutuberRank()
    rank.display_rank_info()
    
    # Sprawdzenie konkretnego użytkownika
    user_to_check = "Isamu"
    rank.check_user(user_to_check)