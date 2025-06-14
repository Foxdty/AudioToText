import whisper
import gradio as gr
import yt_dlp
import os
import uuid


model = whisper.load_model("small")

def download_youtube_audio(youtube_url):
    output_filename = f"{uuid.uuid4()}"
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_filename,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
    }
    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    print("output: ",output_filename)
    return output_filename

def transcribe_audio(file_upload, youtube_link):
    audio_path = None


    if file_upload:
        audio_path = file_upload
    elif youtube_link:
        audio_path = f"{download_youtube_audio(youtube_link)}.mp3"
    else:
        return "Vui lòng tải file hoặc nhập link YouTube."

    try:
        print("done")
        result = model.transcribe(audio_path)
       
        return result["text"]
    except Exception as e:
        print("audio_path: ",audio_path)
        return f"Lỗi: {str(e)}"
    finally:
     
        if youtube_link and audio_path and os.path.exists(audio_path):
            os.remove(audio_path)
        



interface = gr.Interface(
    fn=transcribe_audio,
    inputs=[
        gr.Audio(type="filepath", label="Tải file MP3 (tùy chọn)"),
        gr.Textbox(label="Hoặc dán link YouTube (tùy chọn)")
    ],
    outputs=gr.Textbox(label="Văn bản chuyển đổi"),
    title="Chuyển giọng nói thành văn bản (MP3 hoặc YouTube)",
    description="Tải file MP3 hoặc dán link YouTube để chuyển âm thanh sang văn bản"
)

interface.launch()
