from telethon import TelegramClient
from telethon.tl.functions.payments import GetPaymentFormRequest, SendStarsFormRequest
from telethon.tl.types import InputInvoiceStarGift, InputPeerUser, TextWithEntities

with open("cfg.txt") as f:
    exec(f.read())
async def giftsender():
    client = TelegramClient("your.session", APID, APIHASH, device_model="iPhone 21 Pro Max Mini Ultra", system_version="18.1", app_version="8.4", lang_code="en", system_lang_code="en-US")
    await client.start()
    
    try:
        entity = await client.get_entity(USERNAME)
        peer = InputPeerUser(user_id=entity.id, access_hash=entity.access_hash)
        message = TextWithEntities(text=MSGTEXT, entities=[]) if MSGTEXT else None
        
        invoice = InputInvoiceStarGift(
            peer=peer,
            gift_id=GIFTID,
            hide_name=HIDENAME,
            include_upgrade=False,
            message=message
        )
        
        pform = await client(GetPaymentFormRequest(invoice=invoice))
        
        await client(SendStarsFormRequest(
            form_id=pform.form_id,
            invoice=invoice
        ))
        
        print("success")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(giftsender())      # no 40 lines script(9(99((