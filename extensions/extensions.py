txt = input("File name: ").lower().strip()
#if txt[-4:] in ['.gif',".jpg",".png",".txt",".zip"]:
if txt.endswith(".gif") :
    print("image/gif")
elif txt.endswith(".png") :
    print("image/png")
elif txt.endswith(".jpg") or txt.endswith(".jpeg"):
    print("image/jpeg")
elif txt.endswith(".pdf"):
    print("application/pdf")
elif txt.endswith(".txt"):
    print("text/plain")
elif txt.endswith(".zip"):
   print("application/zip")
else:
    print("application/octet-stream")