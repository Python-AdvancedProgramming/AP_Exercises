from nicegui import ui
from googletrans import Translator

translator = Translator()

state = {
    "english_text": "",
    "german_text": "The translation will appear here.",
}


@ui.refreshable
def show_translation():
    ui.label("German translation:")
    ui.label(state["german_text"])


async def translate_text():
    english_text = state["english_text"]

    if english_text.strip() == "":
        state["german_text"] = "Please enter an English text first."
        ui.notify("No input provided", type="warning")
    else:
        try:
            translation = await translator.translate(
                english_text,
                src="en",
                dest="de",
            )
            state["german_text"] = translation.text

        except Exception as error:
            state["german_text"] = "Translation failed."
            ui.notify(f"Error: {error}", type="negative")

    show_translation.refresh()


def clear_text():
    state["english_text"] = ""
    state["german_text"] = "The translation will appear here."
    show_translation.refresh()


with ui.row().style("align-items: center; margin-bottom: 20px;"):
    ui.label("English to German Translator").style(
        "font-size: 32px; font-weight: bold;"
    )

with ui.card().style("width: 700px; padding: 24px;"):
    ui.label("Enter English text:")

    input_text = ui.textarea(
        label="English text",
        placeholder="Write something in English...",
    ).style("width: 100%; height: 220px;")

    input_text.bind_value(state, "english_text")

    with ui.row():
        ui.button("Translate to German", on_click=translate_text)
        ui.button("Clear text / Text löschen", on_click=clear_text)

    ui.separator()

    show_translation()


ui.run()
