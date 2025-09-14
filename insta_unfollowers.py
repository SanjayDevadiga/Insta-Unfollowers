import instaloader
import json

class InstagramSession:
    def __init__(self, username: str, cookies_file: str = "cookies.json"):
        """
        Initialize Instagram session using cookies exported from browser.
        """
        self.username = username
        self.cookies_file = cookies_file
        self.loader = instaloader.Instaloader()
        self._load_cookies()

    def _load_cookies(self):
        """Load cookies from JSON file and inject into Instaloader session."""
        try:
            with open(self.cookies_file, "r") as f:
                cookies = json.load(f)

            for cookie in cookies:
                self.loader.context._session.cookies.set(cookie["name"], cookie["value"])

            # Tell Instaloader that we are logged in
            self.loader.context.username = self.username

        except FileNotFoundError:
            raise RuntimeError(f"Cookie file '{self.cookies_file}' not found.")
        except json.JSONDecodeError:
            raise RuntimeError("Invalid cookie file format.")

    def get_profile(self):
        """Return the Instaloader profile object for the current user."""
        return instaloader.Profile.from_username(self.loader.context, self.username)

    def get_followers(self):
        """Fetch followers as a list of usernames."""
        profile = self.get_profile()
        return [f.username for f in profile.get_followers()]

    def get_following(self):
        """Fetch following as a list of usernames."""
        profile = self.get_profile()
        return [f.username for f in profile.get_followees()]

    def compare_relationships(self):
        """Compute unfollowers and not-following-back users."""
        followers = set(self.get_followers())
        following = set(self.get_following())

        unfollowers = following - followers  # I follow them, they don’t follow me
        not_following_back = followers - following  # They follow me, I don’t follow back

        return followers, following, unfollowers, not_following_back

    def save_results(self):
        """Save followers, followees, unfollowers, and not-following-back to text files."""
        followers, following, unfollowers, not_following_back = self.compare_relationships()

        files = {
            "followers.txt": followers,
            "followees.txt": following,
            "unfollowers.txt": unfollowers,
            "not_following_back.txt": not_following_back,
        }

        for filename, data in files.items():
            with open(filename, "w", encoding="utf-8") as f:
                for user in sorted(data):
                    f.write(user + "\n")
            print(f"[✔] Saved {len(data)} entries to {filename}")


if __name__ == "__main__":
    username = "your username"  # your IG username
    cookies_file = "cookies.example.json"  # path to your cookies file
    session = InstagramSession(username, cookies_file)
    session.save_results()