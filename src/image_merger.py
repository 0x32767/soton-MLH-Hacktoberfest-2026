import os
import sys

from PIL import Image


class Character:
    def __init__(self, game_id) -> None:
        self.path = f"../images/{game_id}"
        self.head = Image.open(f"{self.path}/head.png")
        self.body = Image.open(f"{self.path}/torso.png")
        self.arm = Image.open(f"{self.path}/arm.png")
        self.leg = Image.open(f"{self.path}/leg.png")
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
