import plotly.graph_objs as go
from plotly.offline import init_notebook_mode

colours = ["green", "red", "blue", "yellow", "grey", "orange", "brown", "dodgerblue", "aqua", "#ea15ed", "#44fc4d", "#4d005e"]*5


def init_fig(title, xlabel, ylabel, template="plotly_dark"):
    return go.Figure(layout={
        "title": title,
        "xaxis_title": xlabel,
        "yaxis_title": ylabel,
        "template": template,
        "legend": {"itemsizing": "constant"},
        "hovermode": "x",
    })


def add_trace_to_plot(figure: go.Figure, xvals: list, yvals: list, linecolour: str, name: str, **kwargs):

    opacity = kwargs.get("opacity", 1)
    mode = kwargs.get("mode", "lines+markers")
    markersize = kwargs.get("markersize", 5)
    hovertext = kwargs.get("hovertext", "")

    figure.add_trace(
        go.Scatter(x=xvals,
                   y=yvals,
                   opacity=opacity,
                   line={"color": linecolour},
                   mode=mode,
                   hovertext=hovertext,
                   marker={"symbol": "circle", "size": [markersize if c != 0 else 0 for c in yvals],
                           "opacity": opacity},
                   name=name,
                   showlegend=True)
    )
    return figure


def plot_df(data_frame, col_name_list: list, day_col_name="day", hover_col="", **kwargs):

    title = kwargs.get("title", "")
    ylabel = kwargs.get("ylabel", "count")
    xlabel = kwargs.get("xlabel", "day")
    template = kwargs.get("template", "plotly_dark")

    fig = init_fig(title=title, xlabel=xlabel, ylabel=ylabel, template=template)
    hover_values = ""
    if hover_col:
        hover_values = data_frame[hover_col]

    for ii, col_name in enumerate(col_name_list):
        try:
            counts = data_frame[col_name].values
        except KeyError:
            print(f"Column {col_name} not in dataframe :(")
            continue

        fig = add_trace_to_plot(
            fig,
            data_frame[day_col_name],
            counts,
            linecolour=colours[ii],
            name=col_name,
            hovertext=hover_values,
            **kwargs
        )

    fig.show()
