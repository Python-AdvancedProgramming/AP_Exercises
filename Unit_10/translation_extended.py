from dataclasses import dataclass
from googletrans import Translator
from nicegui import ui


@dataclass
class TranslationModel:
    english_text: str = ""
    german_text: str = "The translation will appear here."
    status: str = "Ready"


class TranslationApp:
    def __init__(self):
        self.model = TranslationModel()
        self.translator = Translator()

    async def translate(self):
        if self.model.english_text.strip() == "":
            self.model.german_text = "Please enter an English text first."
            self.model.status = "No input"
            ui.notify("No input provided", type="warning")
        else:
            try:
                result = await self.translator.translate(
                    self.model.english_text,
                    src="en",
                    dest="de",
                )
                self.model.german_text = result.text
                self.model.status = "Translated"
            except Exception as error:
                self.model.german_text = "Translation failed."
                self.model.status = "Error"
                ui.notify(f"Error: {error}", type="negative")

        self.translation_area.refresh()

    def clear_text(self):
        self.model.english_text = ""
        self.model.german_text = "The translation will appear here."
        self.model.status = "Ready"
        self.translation_area.refresh()

    def build(self):
        with ui.column().classes(
            "w-full min-h-screen items-center justify-center bg-gray-100 p-8"
        ):
            with ui.card().classes("w-full max-w-4xl p-8 shadow-lg rounded-lg"):
                with ui.column().classes("w-full gap-5"):

                    ui.label("English to German Translator").classes(
                        "text-4xl font-bold"
                    )

                    ui.label("Enter English text:")
                    textarea = ui.textarea(
                        label="English text",
                        placeholder="Write something in English...",
                    ).classes("w-full h-56")

                    textarea.bind_value(self.model, "english_text")

                    with ui.row().classes("w-full justify-between items-center"):
                        with ui.row().classes("gap-3"):
                            ui.button("Translate to German", on_click=self.translate)
                            ui.button(
                                "Clear text / Text löschen",
                                on_click=self.clear_text,
                            )

                        ui.label().bind_text_from(self.model, "status")

                    ui.separator()

                    self.translation_area()

    @ui.refreshable
    def translation_area(self):
        with ui.card().classes("w-full bg-blue-50 p-6"):
            ui.label("German translation").classes("text-lg font-semibold")
            ui.label(self.model.german_text).classes("text-base")


app = TranslationApp()
app.build()

ui.run()
