# get user input
filename = input("Enter File Name:").strip().lower()

#define filetypes acceptable in server directory
filetypes_image = (".jpg",".png", ".gif",".jpeg", ".bitmap")
filetypes_pdf = (".pdf")
filetypes_text = (".txt")
filetypes_zip = (".zip", ".rar", ".tgz")
filetype_audio = (".mp3", ".ogg", ".wav","aac",".weba")
filetype_video = (".mp4", ".mov",".ts",".ogg")

#insist on a valid entry
invalid = "Invalid Entry, please try again \U0001F641"
if filename == "":
    print(invalid)

# logic for valid entry
elif filename.endswith(filetypes_image):
    filename = filename.replace("jpg", "jpeg").split(".")[-1] # extract extension from filename
    print(f"image/{filename}")

elif filename.endswith(filetypes_pdf):
    filename = filename.split(".")[-1]
    print(f"application/{filename}")

elif filename.endswith(filetypes_text):
    filename = filename.split(".")[-1]
    print(f"text/plain")

elif filename.endswith(".zip"):
    filename = filename.split(".")[-1]
    print(f"application/{filename}")

elif filename.endswith(filetype_audio):
    filename = filename.split(".")[-1]
    print(f"audio/{filename}")

elif filename.endswith(filetype_video):
    filename = filename.split(".")[-1]
    print(f"video/{filename}")

else:
    print("application/octet-stream")

