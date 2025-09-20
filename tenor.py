import pyautogui
import pyperclip
import time

# Your tag list
TAGS = [
    "#Meditation",
    "#Spirituality",
    "#YogiLife",
    "#Tapas",
    "#HinduWisdom",
    "#SanatanaDharma",
    "#VedicTradition",
    "#Bhakti",
    "#Dhyan",
    "#AncientWisdom",
    "#SpiritualJourney",
    "#HigherConsciousness",
    "#Brahma",
    "#LordVishnu",
    "#BhaktaPrahaladha",
    "#MahaavatarNarasimha",
    "#Upanishads",
    "#Puranas",
    "#SacredMantras",
    "#mahavatar_narsimha",
    "#mahavatar narsimha"
]

print("You have 5 seconds to switch to your chat/text area...")
time.sleep(5)

while True:  # Infinite loop
    for tag in TAGS:
        pyperclip.copy(tag)            # Copy tag to clipboard
        pyautogui.hotkey("ctrl", "v")  # Paste
        pyautogui.press("enter")       # Press Enter after each tag
        time.sleep(0.5)                # Small delay between tags
    
    print("✅ Completed one round of tags.")
    time.sleep(3)  # Wait 3 seconds before repeating
