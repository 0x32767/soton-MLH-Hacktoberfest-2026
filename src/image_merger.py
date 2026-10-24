import base64
import io

from PIL import Image


class Character:
    def __init__(self, game_folder_path, head_str, torso_str, arm_str, leg_str) -> None:
        self.path = game_folder_path
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
        output_path = f"{self.path}/character.png"
        self.character.save(output_path, optimize=True)
