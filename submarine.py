from http import client
import seamoth

def main():
    camera = seamoth.Camera()
    conn = seamoth.DataConnection()

    conn.clientStart("192.168.86.42", 1951)

    while True:
        conn.send(camera.readCameraData())

if __name__ == "__main__":
    main()