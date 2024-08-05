from fasthtml.common import *
from ToDoTitle import ToDoTitle
from starlette.staticfiles import StaticFiles

# Include htmx library
htmx_script = Script(src="https://unpkg.com/htmx.org@1.5.0")

# Tailwind CSS and custom styles
css = Link(rel="stylesheet", href="/static/css/styles.css")
tailwind_css = Link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
)

app, rt = fast_app(
    hdrs=(css, tailwind_css, htmx_script),
    routes=[Mount("/static", StaticFiles(directory="static"), name="static")],
    live=True,
)

activity_list = []
count  = 0


@app.post("/")
def test(activity: str):
    global count
    count += 1
    if activity:
        item = Li(
                    P(
                        activity,
                        cls="hover:text-red-500 font-semibold",
                    ),
                    # A("Delete",
                    #     hx_delete="/",
                    #     hx_swap="outerHTML",
                    #     cls="mx-3 text-red-500 hover:text-red-300"
                    # ),
                    cls="mx-8 my-5 font-semibold",
                    id=f"{count}",
                    hx_delete="/",  
                    hx_swap="outerHTML"
                )
        
        activity_list.append(item) if activity else None
        return item

@app.delete("/")
def delete_function():
    return ""

@app.get("/")
def get():
    return( 
        Title("ToDo App"), 
        Main(
            Div(
                ToDoTitle("TODO APP!"),
                Div(
                    Card(
                        Form(
                            Group(
                                Input(
                                    id="new-todo-input",
                                    placeholder="Enter Task",
                                    name="activity",
                                    cls="w-24"
                                ),
                                Button(
                                    "Add",
                                    cls="""
                                        font-semibold
                                        bg-purple-500 
                                        hover:bg-white 
                                        hover:text-purple-500 
                                        focus:border-purple-500 
                                        border-transparent
                                        """,
                                ),
                            ),
                            hx_post="/",
                            hx_target="#activity-list-container",
                            hx_swap="beforeend",
                        ),
                    ),
                ),
                Div(
                    H2(
                        "TODOs",
                        cls="font-bold"
                    ),
                    Ul(id="activity-list-container"), 
                    cls="list-container"
                ),
                cls="container",
            ),
        )
    )


serve()
