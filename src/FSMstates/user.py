from maxapi.context.state_machine import State, StatesGroup

class user_Form(StatesGroup):
    max_id = State()
    first_name = State()
    last_name = State()
    