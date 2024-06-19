# from pytube import YouTube

# def download_video(url, download_path):
#     try:
#         yt = YouTube(url)
#         video = yt.streams.get_highest_resolution()
#         print("Downloading video...")
#         video.download(output_path=download_path, filename=yt.title)
#         print("Video downloaded successfully!")
#     except Exception as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     video_url = input("Enter the YouTube video URL: ")
#     download_path = r"C:\Users\Gowtham\Videos"  # Update this with your desired download path
#     download_video(video_url, download_path)

# from pytube import YouTube
# import os

# def download_4k_video(url, download_path):
#     try:
#         # Create a YouTube object
#         yt = YouTube(url)

#         # Filter streams to get the highest resolution (4K in this case)
#         video_stream = yt.streams.filter(res="2160p", file_extension='mp4').first()

#         # Check if 4K video is available
#         if video_stream is None:
#             print("4K video is not available for this video.")
#             return

#         # Displaying video title
#         print(f"Title: {yt.title}")

#         # Displaying download status
#         print("Starting download...")

#         # Download the video
#         video_stream.download(output_path=download_path)

#         # Displaying completion status
#         print(f"Download completed! Video saved to: {os.path.join(download_path, video_stream.default_filename)}")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# url = "https://www.youtube.com/watch?v=ijBxe70sd8M"  # Replace with the actual YouTube video URL
# download_path = r"C:\Users\Gowtham\Videos"  # Replace with your desired download path

# download_4k_video(url, download_path)



from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def download_4k_video(url, download_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Filter streams to get the highest resolution (4K video) and audio streams
        video_stream = yt.streams.filter(res="2160p", mime_type="video/webm").first()
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/webm").first()

        # Check if 4K video is available
        if video_stream is None:
            print("4K video is not available for this video.")
            return

        # Ensure download path exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Download the video and audio streams
        print("Starting download...")
        video_file = video_stream.download(output_path=download_path, filename="video_4k.webm")
        audio_file = audio_stream.download(output_path=download_path, filename="audio.webm")
        print("Download completed!")

        # Merge video and audio using moviepy
        print("Merging video and audio...")
        video_clip = VideoFileClip(video_file)
        audio_clip = AudioFileClip(audio_file)
        final_clip = video_clip.set_audio(audio_clip)
        final_output_path = os.path.join(download_path, yt.title + ".mp4")
        final_clip.write_videofile(final_output_path, codec='libx264', audio_codec='aac')

        # Cleanup temporary files
        os.remove(video_file)
        os.remove(audio_file)

        print(f"Download and merge completed! Video saved to: {final_output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://youtu.be/ijBxe70sd8M?si=Z8lkjdEi2DumMX6Q"  # Replace with the actual YouTube video URL
download_path =  r"C:\Users\Gowtham\Videos"  # Replace with your desired download path

download_4k_video(url, download_path)
