from maxapi.context.state_machine import State, StatesGroup

class user_Form(StatesGroup):
    name = State()
    link = State()