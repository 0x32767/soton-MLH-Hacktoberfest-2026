import base64
import io
from pathlib import Path

from PIL import Image


class Character:
    def __init__(self) -> None:
        self.torso = None
        self.arm = None
        self.leg = None
        self.head = None

    def add_torso(self, torso_str):
        self.torso = Image.open(
            io.BytesIO(base64.decodebytes(bytes(torso_str, "utf-8")))
        )

    def add_arm(self, arm_str):
        self.arm = Image.open(io.BytesIO(base64.decodebytes(bytes(arm_str, "utf-8"))))

    def add_leg(self, leg_str):
        self.leg = Image.open(io.BytesIO(base64.decodebytes(bytes(leg_str, "utf-8"))))

    def add_head(self, head_str):
        self.head = Image.open(io.BytesIO(base64.decodebytes(bytes(head_str, "utf-8"))))

    def get_preview_for_torso(self):
        return self.save(
            self.head.crop(
                (0, self.head.height - 50, self.head.width, self.head.height)
            )
        )

    def get_preview_for_arm(self):
        return self.save(self.torso.crop((0, 0, 50, self.torso.height)))

    def get_preview_for_leg(self):
        return self.save(
            self.torso.crop(
                (0, self.torso.height - 50, self.torso.width, self.torso.height)
            )
        )

    def _merge(self):
        height = self.head.height + self.torso.height + self.leg.height
        width = (self.arm.width * 2) + self.torso.width
        self.character = Image.new("RGBA", (width, height))

        self.character.paste(self.head, ((height - self.head.width) // 2, 0))
        self.character.paste(self.torso, (self.arm.width, self.head.height))
        self.character.paste(self.arm, (0, self.head.height))
        self.character.paste(
            self.arm.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT),
            (self.arm.width + self.torso.width, self.head.height),
        )
        self.character.paste(
            self.leg,
            ((width - (self.leg.width * 2)) // 2, self.head.height + self.torso.height),
        )
        self.character.paste(
            self.leg.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT),
            (
                ((width - (self.leg.width * 2)) // 2) + self.leg.width,
                self.head.height + self.torso.height,
            ),
        )

    def _apply_background(self):
        self.image = Image.open(f"{Path(__file__).parent}/static/spooky/background.png")
        char_pad = (self.image.width - self.character.width) // 2
        self.image.paste(self.character, (char_pad, 0))

    def save(self, image_to_save=None):
        if image_to_save is None:
            self._merge()
            self._apply_background()
            image_to_save = self.character
        image_png = io.BytesIO()
        image_to_save.save(image_png, format="PNG")
        image_bytes = image_png.getvalue()
        base64_image_bytes = base64.b64encode(image_bytes)
        base64_image_str = base64_image_bytes.decode("ascii")
        return base64_image_str
