import sys
import time
from tqdm import tqdm

sys.path.append("..")  # Adds higher directory to python modules path

from google.cloud import translate_v2 as translate
from definitions import CURRENT_DIR


# Set source and target languages
source = "en"  # English
target = "id"  # Indonesia
translate_client = translate.Client()


def translate_caption(text):
    result = translate_client.translate(
        text, target_language=target, source_language=source
    )

    return result["translatedText"]


if __name__ == "__main__":
    start_time = time.time()  # Get current time
    translated_dataset = []
    amount = 0

    with (
        open(
            f"{CURRENT_DIR}/Flicker8k_text/Flickr8k.token.indo.txt", "a"
        ) as translated_file,
        open(f"{CURRENT_DIR}/Flicker8k_text/Flickr8k.token.txt", "r") as original_file,
    ):
        try:
            for line in tqdm(original_file.read().split("\n")):
                # Split each line at the tab, dividing file and actual caption
                line = line.split("\t")

                # Take only the caption
                caption = line[-1]
                translated_caption = translate_caption(caption)

                # Switch original caption with translated caption and combine at the tab
                line[-1] = translated_caption
                data = "\t".join(line)

                # Append data to list and increment amount of captions
                translated_dataset.append(data)
                amount += 1
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt on program!\n")
        finally:
            # Append all captions from list to file
            for caption in translated_dataset:
                translated_file.write(caption + "\n")

            # Display total captions translated and time taken
            end_time = time.time()
            print(f"Translated captions in: {end_time - start_time} seconds")
            print(f"Translated {amount} captions")
