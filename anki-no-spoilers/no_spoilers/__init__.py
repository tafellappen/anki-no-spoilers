# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
import re

def beforeShowCard(html, card, context):
    makeBlueScript = """
<script>
document.body.style.background = "blue";
</script>"""
    # answer = card.answer()
    # if answer in html

    return html + makeBlueScript


#########################
def testModCards():
    ids = mw.col.findCards("deck:プログラミング")
    testingCap = 20
    cardNumber = 0

    #https://www.reddit.com/r/Anki/comments/5b1p7v/cant_edit_note_field_in_python/
    for id in ids:
        if (cardNumber >= testingCap):
            break
        card = mw.col.getCard(id)
        note = card.note()
        for (name, value) in note.items():

            # if (name == "Spanish Word"):
            note[name] = value + "something new"


            # showInfo(value)

        note.flush()
        cardNumber += 1

def removeSpoilers():
    ids = mw.col.find_notes("deck:プログラミング")
    for id in ids:
        note = mw.col.getNote(id)
        for (name, value) in note.items():
            # showInfo(name)
            if (name == "furigana-plain(expression)"):
                wordToScreenFor = note[name]

                fieldNameToScan = "Front of Card Sentence"
                fieldToScan = note[fieldNameToScan]

                # #remove furigana from the word, the sentence will not have it
                furi = re.search("(\[.*\])", wordToScreenFor)
                wordWithoutFuri = furi.group(1)

                note[fieldNameToScan] = fieldToScan.replace(wordToScreenFor, "[|||no peeking|||]")




        note.flush()
    showInfo("Done")

# create a new menu item, "test"
action = QAction("remove spoilers", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, removeSpoilers)
# and add it to the tools menu
mw.form.menuTools.addAction(action)


gui_hooks.card_will_show.append(beforeShowCard)


