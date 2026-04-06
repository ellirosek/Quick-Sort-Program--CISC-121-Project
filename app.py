import gradio as gr

# Global state
state = {
    "array": [],
    "pivot": None,
    "left": [],
    "right": [],
    "remaining": [],
    "steps": []
}

# Create bar visualization using HTML
def draw_bars(arr, pivot=None):
    if not arr:
        return ""

    max_val = max(arr)
    bars_html = "<div style='display:flex; align-items:flex-end; height:200px;'>"

    for num in arr:
        height = (num / max_val) * 180
        color = "red" if num == pivot else "steelblue"

        bars_html += f"""
        <div style='margin:5px; text-align:center;'>
            <div style='background:{color}; width:40px; height:{height}px;'></div>
            <div>{num}</div>
        </div>
        """

    bars_html += "</div>"
    return bars_html


# Start sorting
def start_sort(input_text):
    try:
        arr = list(map(int, input_text.split(",")))
        state["array"] = arr
        state["pivot"] = arr[0]
        state["remaining"] = arr[1:]
        state["left"] = []
        state["right"] = []
        state["steps"] = [f"Starting array: {arr}", f"Pivot chosen: {state['pivot']}"]

        return draw_bars(arr, state["pivot"]), "Is the next number smaller or bigger than the pivot?"
    except:
        return "", "Enter numbers like: 5,3,8,4,2"


# Choose left
def choose_left():
    if not state["remaining"]:
        return finish_partition()

    num = state["remaining"].pop(0)
    state["left"].append(num)
    state["steps"].append(f"{num} → LEFT")

    return update_display()


# Choose right
def choose_right():
    if not state["remaining"]:
        return finish_partition()

    num = state["remaining"].pop(0)
    state["right"].append(num)
    state["steps"].append(f"{num} → RIGHT")

    return update_display()


# Update display
def update_display():
    arr_display = state["left"] + [state["pivot"]] + state["right"] + state["remaining"]
    return draw_bars(arr_display, state["pivot"]), "\n".join(state["steps"])


# Finish partition
def finish_partition():
    state["steps"].append(f"Partition done: LEFT={state['left']} | RIGHT={state['right']}")
    sorted_arr = sorted(state["array"])

    return draw_bars(sorted_arr), f"FINAL SORTED: {sorted_arr}\n\nSteps:\n" + "\n".join(state["steps"])


# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# Quick Sort Interactive Visualizer")

    input_box = gr.Textbox(label="Enter numbers (comma separated)")
    start_btn = gr.Button("Start Sorting")

    bars_output = gr.HTML()
    text_output = gr.Textbox(label="Steps", lines=15)

    left_btn = gr.Button("Smaller than Pivot (LEFT)")
    right_btn = gr.Button("Bigger than Pivot (RIGHT)")

    start_btn.click(start_sort, inputs=input_box, outputs=[bars_output, text_output])
    left_btn.click(choose_left, outputs=[bars_output, text_output])
    right_btn.click(choose_right, outputs=[bars_output, text_output])

app.launch()
