# SipadSurvey

A small automation script that fills in the course/instructor evaluation
surveys on the TUMS Sipad portal (<https://sipad.tums.ac.ir>) for you, using
Selenium and Google Chrome.

You log in with your own credentials, pick one answer (e.g. "very good"), and
the script applies it to every item of every pending survey.

## Requirements

- Google Chrome installed
- Python 3.9+ (only if you run from source)

## Option 1: Windows executable

Download `survey.exe` from the
[Releases](https://github.com/shlheidari/SipadSurvey/releases) page and run it.
No Python installation is needed.

## Option 2: Run from source

```bash
pip install -r requirements.txt
python survey.py
```

## Usage

1. Enter your Sipad username and password (the password is not echoed).
2. Choose the answer to apply to all questions:

   | Number | Answer     |
   | ------ | ---------- |
   | 0      | very good  |
   | 1      | good       |
   | 2      | average    |
   | 3      | weak       |
   | 4      | very weak  |
   | 5      | undecided  |

   Any invalid input falls back to `0`.
3. Wait. The first start can take a while (ChromeDriver is downloaded
   automatically). You can minimize the window and keep using your computer.

## Notes

- Your credentials are only typed into the Sipad login page; nothing is stored
  or sent anywhere else.
- The script relies on the current layout of the Sipad website. If the site
  changes, it may stop working.
- If a step keeps failing, the script gives up after a few attempts instead of
  looping forever.
- Use at your own risk and in accordance with your university's rules.

## Support

Telegram: <https://t.me/Shlheidari>

## License

[MIT](LICENSE)
