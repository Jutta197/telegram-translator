# telegram-translator
Use [MTProto API](https://core.telegram.org/api#tdlib--build-your-own-telegram) to log in to Telegram and display both the original text and its translation.


## Python Environment Setup

Code execution requires a [Python](https://www.python.org/downloads/windows/) environment:

```sh
python --version
```

## Clone the Repository

```sh
git clone git@github.com:Jutta197/telegram-translator.git
```

## Navigate to the Project Directory

```sh
cd telegram-translator
```

## Install Dependencies

```sh
pip install -r packages.txt
```

## Configure API Credentials

Visit [this](https://my.telegram.org/apps), log in, create an application, and then obtain **your API ID and API hash**. Replace these values in the **transdot3.py** file.
```python
api_id = 'api_id'
api_hash = 'api_hash'
```

### Launch the Script

```sh
py transdot3.py
```
