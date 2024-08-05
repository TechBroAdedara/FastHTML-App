from fasthtml.common import *

def ToDoTitle(child: str|None = None,**kwargs):
    return Div(
                H1(f"{child if child is not None else ""}"),
                cls="text-4xl font-bold font-sans mb-5 text-purple-500  ",
            *kwargs
            )
