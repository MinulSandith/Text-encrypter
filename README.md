# Text Encrypter

A tiny [Streamlit](https://streamlit.io/) web app for scrambling and unscrambling text using a simple, custom, reversible text transformation combined with Base64 encoding. It's a fun obfuscation tool, not a real cryptographic cipher — don't use it to protect sensitive data.

## Live app

<https://minulsandith-text-encrypter-frontend-c6u1q8.streamlitapp.com/>

> Note: this link uses Streamlit's older `*.streamlitapp.com` domain. If it doesn't load, the app may need to be redeployed on [Streamlit Community Cloud](https://streamlit.io/cloud) to get a current `*.streamlit.app` URL.

## How it works

1. **Reverse** the input string.
2. **Interleave** it into three groups by splitting characters round-robin (indices `0, 3, 6…` / `1, 4, 7…` / `2, 5, 8…`), then concatenate the groups back together.
3. **Base64-encode** the result (UTF-8) to produce the final "encoded" text.

Decoding runs the same steps in reverse: Base64-decode, un-interleave the three groups back into original order, then reverse the string again.

Newline characters in the input are replaced with `" * "` before encoding, since the scrambling step doesn't preserve line breaks.

## Project structure

| File | Purpose |
| --- | --- |
| `frontend.py` | Streamlit UI — text input, encode/decode buttons, error handling |
| `backend.py` | Core `encode()` / `decode()` logic |
| `style.css` | Custom styling (animated gradient background) injected into the app |
| `requirements.txt` | Python dependencies |
| `logo.jpg` | Project logo |

## Running locally

Requires Python 3.9+.

```bash
git clone https://github.com/MinulSandith/Text-encrypter.git
cd Text-encrypter
pip install -r requirements.txt
streamlit run frontend.py
```

The app will open at `http://localhost:8501`.

## Usage

1. Open the app.
2. Type or paste text into the input box.
3. Click **encode** to scramble it, or **decode** to reverse a previously encoded string.
   - When decoding, paste the exact text shown by **encode** (it will look like `b'...'`) — the app strips the surrounding `b'` and `'` automatically.
4. Copy the result from the output box.

## Development notes / known limitations

- This is a reversible obfuscation scheme, **not encryption** — anyone can decode the output without a key.
- Pasting malformed or non-Base64 text into **decode** shows a friendly warning instead of crashing.
- Round-trips correctly for ASCII, Unicode (accented characters, emoji), backslashes, tabs, and empty input.

## Contributing

Bug reports and pull requests are welcome — see the [issues](https://github.com/MinulSandith/Text-encrypter/issues) page.

Check out my other projects: <https://github.com/MinulSandith?tab=repositories>
