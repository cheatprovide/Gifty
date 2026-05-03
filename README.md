39 lines script that allow u to buy expired telegram gifts

## setup

install telethon:
```bash
pip install telethon
```

## config

open `cfg.txt` and set:

- `APID` - ur telegram api id (get from https://my.telegram.org)
- `APIHASH` - ur telegram api hash (get from https://my.telegram.org)
- `GIFTID` - gift id u want to send (check gifts id.txt)
- `USERNAME` - recipient telegram username (WITHOUT @)
- `MSGTEXT` - optional message with the gift
- `HIDENAME` - show sender name (False) or hide (True)

## run

```bash
python Gifty.py
```

first run - login via phone number

session saves to `your.session`

success = gift sent

## notes

- this method works for gifts that are no longer available in telegram
- keep ur api credentials safe
- actual for May 2026

feedback: t.me/cheatprovider
