import instaloader
from instaloader.exceptions import InstaloaderException, BadResponseException

def download_instagram_video(url):
    try:
        # Create an instance of Instaloader class
        loader = instaloader.Instaloader()

        # Retrieve post information
        post = instaloader.Post.from_shortcode(loader.context, url.rsplit('/', 1)[-1])

        # Download the video
        loader.download_post(post, target='.')
        print("Video downloaded successfully!")
    except BadResponseException as e:
        print(f"Bad response from Instagram: {e}")
    except InstaloaderException as e:
        print(f"Instaloader error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the URL of the Instagram video: ")
    download_instagram_video(video_url)
