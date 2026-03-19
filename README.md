50 lines script that allow u to buy expired telegram gifts

## setup

install telethon:
```bash
pip install telethon
```

## config

open `Gifty.py` and set:

- `apid` - ur telegram api id (get from https://my.telegram.org)
- `apihash` - ur telegram api hash (get from https://my.telegram.org)
- `gift_id` - gift id u want to send (check gifts id.txt)
- `username` - recipient telegram username
- `msgtext` - optional message with the gift

## run

```bash
python Gifty.py
```

first run - login via phone number

session saves to `session.session`

success = gift sent

## notes

- this method works for gifts that are no longer available in telegram
- keep ur api credentials safe
- actual for 2026

feedback: t.me/cheatprovider
