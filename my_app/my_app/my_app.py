from pcconfig import config
import random

import pynecone as pc
 
class State(pc.State): 
    count = 0
    def handleIncrease(self):
        self.count += 1

    def handleDecrese(self):
        self.count -= 1

    def handleRandom(self):
        self.count = random.randint(0, 100)


def index():
    return pc.center(
        pc.vstack(
            pc.heading(State.count),
            pc.hstack(
                pc.button(
                    "Decrement",
                    on_click=State.handleDecrese,
                    background_color="#F04438",
                    color="#FFFFFF",
                ),
                pc.button(
                    "Randomize",
                    on_click=State.handleRandom,
                    background_color="#5C55F7",
                    color="#FFFFFF",
                ),
                pc.button("Increment",
                    on_click=State.handleIncrease, 
                    background_color="#00C896",
                    color="#FFFFFF",
                ),
            ),
            padding="100px",
            bg="#D3D3D3",
            border_radius="10px",
            box_shadow="lg",
        ),
        padding_y="200px",
        font_size="30px",
        text_align="center",
    )


app = pc.App(state=State)
app.add_page(index,title="counter")
app.compile()
