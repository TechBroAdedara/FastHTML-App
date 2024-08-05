from fasthtml.common import *
from ToDoTitle import ToDoTitle
from starlette.staticfiles import StaticFiles

# Include htmx library
htmx_script = Script(src="https://unpkg.com/htmx.org@1.5.0")

# Tailwind CSS and custom styles
css = Link(rel="stylesheet", href="/src/output.css")
tailwind_css = Link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
)
style = Style(
    """
            body{
                min-height: 100vh;
                margin:0;
                background-color: White;
                display:grid;
            }"""
)

app, rt = fast_app(
    pico=False,
    hdrs=(css, htmx_script, style),
    routes=[Mount("/src", StaticFiles(directory="src"), name="src")],
    live=True,
)

activity_list = []
count = 0


@app.post("/")
def test(activity: str):
    global count
    count += 1
    if activity:
        item = Div(
            activity,
            # A("Delete",
            #     hx_delete="/",
            #     hx_swap="outerHTML",
            #     cls="mx-3 text-red-500 hover:text-red-300"
            # ),
            cls="hover:text-white text-purple-500 font-semibold hover:border-2 hover:border-red-500 hover:shadow-none transition duration-300 my-5 border-2 rounded shadow-md hover:bg-red-500 p-4",
            id=f"{count}",
            hx_delete="/",
            hx_swap="outerHTML",
        )

        activity_list.append(item) if activity else None
        return item


@app.delete("/")
def delete_function():
    return ""


@app.get("/")
def get():
    return (
        Title("ToDo App"),
        Div(
            ToDoTitle("TODO APP!"),
            Div(
                Form(
                    Group(
                        Input(
                            id="new-todo-input",
                            placeholder="Enter Task",
                            name="activity",
                            cls="transition duration-300 my-3 px-3 py-2 bg-white border-2 shadow-sm hover:shadow-md border-slate-300 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1 placeholder:italic placeholder:text-slate-400",
                        ),
                        Button(
                            "Add",
                            cls="""
                                transition
                                duration-300 
                                rounded-md
                                w-24 h-8
                                font-semibold
                                bg-purple-500 
                                text-white
                                hover:bg-white
                                hover:text-purple-500
                                hover:border-purple-500
                                hover: border-2
                                """,
                        ),
                    ),
                    hx_post="/",
                    hx_target="#activity-list-container",
                    hx_swap="beforeend",
                ),
                cls="",
            ),
            Div(
                H2(
                    "Tasks",
                    cls="text-xl font-bold text-purple-400 my-5",
                ),
                Div(id="activity-list-container"),
                cls="list-container",
            ),
            cls="justify-self-center w-3/4 mt-10 ",
        ),
    )


serve()
