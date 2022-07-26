import pyshark

capture = pyshark.LiveCapture(interface="イーサネット")
for raw_socket in capture.sniff_continuously():
    try:
        print(raw_socket)
    except Exception as e:
        print(e)