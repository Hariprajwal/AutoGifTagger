import pyautogui
import pyperclip
import time

# Your tag list
TAGS = [
    "#Meditation",
    "#Mindfulness",
    "#Spirituality",
    "#YogiLife",
    "#Tapas",
    "#HinduWisdom",
    "#SanatanaDharma",
    "#VedicTradition",
    "#Bhakti",
    "#Dhyan",
    "#EasternPhilosophy",
    "#AncientWisdom",
    "#SpiritualJourney",
    "#HigherConsciousness",
    "#Brahma",
    "#LordVishnu",
    "#BhaktaPrahaladha",
    "#MahaavatarNarasimha",
    "#Upanishads",
    "#Puranas",
    "#SacredMantras"
]

print("You have 5 seconds to switch to your chat/text area...")
time.sleep(5)

for tag in TAGS:
    pyperclip.copy(tag)           # Copy tag to clipboard
    pyautogui.hotkey("ctrl", "v") # Paste
    pyautogui.press("enter")      # Press Enter after each tag
    time.sleep(0.5)               # Small delay to look natural

print("✅ Completed: All tags pasted.")
