from os import getlogin, rename, path, makedirs


class Program:
    def __init__(self):
        self.files: tuple = (
            {"payload": r"RainEffect.scr", "dest": r"C:\Windows\System32"}, 
            {"payload": r"image.png",      "dest": rf"C:\Users\{getlogin()}\AppData\Local"}
        )


    def run(self):
        
        payload: str = self.files[0]["payload"]
        dest:    str = self.files[0]["dest"]
        rename(payload, fr"{dest}\{payload}")

        payload: str = self.files[1]["payload"]
        dest:    str = self.files[1]["dest"]
        new_dir: str = path.join(dest, "Rain Effect ScreenSaver")
        makedirs(new_dir)
        rename(payload, fr"{new_dir}\{payload}")



if __name__ == "__main__":
    Program().run()