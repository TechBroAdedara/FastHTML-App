from fasthtml.common import *

def ToDoTitle(child: str|None = None,**kwargs):
    return Div(
                H1(f"{child if child is not None else ""}"),
                cls="text-4xl font-bold mb-5 ",
            *kwargs
            )