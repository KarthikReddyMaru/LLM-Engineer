import modal
from modal import App, Image

app = App(name = 'Location')
image = Image.debian_slim().pip_install(["requests"])

@app.cls(image = image)
class Location:
    
    @modal.enter()
    def setup(self):
        print("Starting container...")
        
    @modal.method()
    def getLocation(self) -> list[str, str, str]:
        
        from requests import get

        response = get("https://ipinfo.io/json").json()
        return response['city'], response['region'], response['country']

    @modal.exit()
    def exit(self):
        print("Stopping container...")