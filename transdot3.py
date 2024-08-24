from telethon.sync import TelegramClient, events
from translatepy import Translator, exceptions

# https://my.telegram.org/apps
api_id = 'api_id'
api_hash = 'api_hash'


# Create an instance of TelegramClient
client = TelegramClient('transdot3', api_id, api_hash)
client.start()

# Initialize the translator
translator = Translator()

@client.on(events.NewMessage(outgoing=True))
async def main(event):
# Check for the `.tr` prefix to implement specific command handling functionality.
#   if not event.message.message.startswith(".tr") and event.message.message.strip():  
    if event.message.message.strip():
        try:
            # Translation
            translated_text_ja = translator.translate(event.message.message, "ja").result
            translated_text_de = translator.translate(event.message.message, "de").result

            # Output the original text and the translations
            # Or use the entities parameter https://core.telegram.org/api/entities
            # f-string
            combined_message = (
                f"{event.message.message}\n\n"
#                f"```"
                f"「{translated_text_ja}」"
                f"{translated_text_de}"
#                f"```"

            )

            # Update the message content
            await event.edit(combined_message)
        except (exceptions.NoResult, exceptions.UnknownLanguage) as error:
            await event.delete()
            
        except Exception as e:
            pass
            

# Run the client
client.run_until_disconnected()
