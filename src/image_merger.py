import base64
import io

from PIL import Image


class Character:
    def __init__(self, head_str, torso_str, arm_str, leg_str) -> None:
        self.head = Image.open(io.BytesIO(base64.decodebytes(bytes(head_str, "utf-8"))))
        self.body = Image.open(io.BytesIO(base64.decodebytes(bytes(head_str, "utf-8"))))
        self.arm = Image.open(io.BytesIO(base64.decodebytes(bytes(head_str, "utf-8"))))
        self.leg = Image.open(io.BytesIO(base64.decodebytes(bytes(head_str, "utf-8"))))
        self._merge()

    def _merge(self):
        height = self.head.height + self.body.height + self.leg.height
        width = (self.arm.width * 2) + self.body.width
        self.character = Image.new("RGBA", (width, height))

        self.character.paste(self.head, ((height - self.head.width) // 2, 0))
        self.character.paste(self.body, (self.arm.width, self.head.height))
        self.character.paste(self.arm, (0, self.head.height))
        self.character.paste(
            self.arm, (self.arm.width + self.body.width, self.head.height)
        )
        self.character.paste(
            self.leg,
            ((width - self.leg.width) // 2, self.head.height + self.body.height),
        )
        self.character.paste(
            self.leg,
            ((width // 2) - self.leg.width, self.head.height + self.body.height),
        )

    def save(self):
        character_png = io.BytesIO()
        self.character.save(character_png, format="PNG", optimize=True)
        character_bytes = character_png.getvalue()
        base64_character_bytes = base64.b64encode(character_bytes)
        base64_character_str = base64_character_bytes.decode("ascii")
        return base64_character_str
