# Starlette Alice :purple_heart:

Template app for [Yandex Alice](https://yandex.ru/alice) made on [Starlette](https://www.starlette.io/) with ready from the box [Now](https://zeit.co/) deployment

### Running on your PC without Now (only for debug!)

```sh
$ pip3 install -r requirements.txt
$ python3 app.py
```
Then in another console run [ngrok](https://ngrok.com/) to make your server open for the world.
```sh
$ ngrok http 8000
```
Then copy your public link and paste it into your skill settings in [Alice developer dashboard](https://dialogs.yandex.ru/developer)

### Deployment
Install Now, then run inside project directory
```sh
$ now
```
If you run firstly, you will have to login via the email confirmation and create a project. Repeat the same steps with public link and your skill settings as with ngrok.
