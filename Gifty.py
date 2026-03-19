from telethon import TelegramClient
from telethon.tl.functions.payments import GetPaymentFormRequest, SendStarsFormRequest
from telethon.tl.types import InputInvoiceStarGift, InputPeerUser, TextWithEntities
######################################################################################

apid = "1234" # ur api id
apihash = "1234fff" # ur api hash
gift_id = 1234 # gift id (check gifts id.txt in repo)
username = "cheatprovider" # WITHOUT @!!! just username u need to send gifts to (it can be u btw)
msgtext = "" # type something or comment this line

######################################################################################
async def giftsender():
    client = TelegramClient("session", apid, apihash, device_model="iPhone 21 Pro Max Mini Ultra", system_version="18.1", app_version="8.4", lang_code="en", system_lang_code="en-US")
    await client.start()
    
    try:
        entity = await client.get_entity(username)
        peer = InputPeerUser(user_id=entity.id, access_hash=entity.access_hash)
        message = TextWithEntities(text=msgtext, entities=[]) if msgtext else None
        
        invoice = InputInvoiceStarGift(
            peer=peer,
            gift_id=gift_id,
            hide_name=False,
            include_upgrade=False,
            message=message
        )
        
        payment_form = await client(GetPaymentFormRequest(
            invoice=invoice,
            theme_params=None
        ))
        
        result = await client(SendStarsFormRequest(
            form_id=payment_form.form_id,
            invoice=invoice
        ))
        
        print("success")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await client.disconnect()

if __name__ == "__main__":
    import asyncio
    import os
    
    asyncio.run(giftsender())
    os.system("pause")
