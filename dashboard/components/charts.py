import plotly.express as px


def line_chart(

        data,

        x,

        y,

        title

):

    fig = px.line(

        data,

        x=x,

        y=y,

        markers=True,

        title=title

    )

    return fig


def bar_chart(

        data,

        x,

        y,

        title

):

    fig = px.bar(

        data,

        x=x,

        y=y,

        title=title

    )

    return fig
import plotly.express as px


def line_chart(df, x, y, color=None, title=""):

    fig = px.line(

        df,

        x=x,

        y=y,

        color=color,

        markers=True,

        title=title

    )

    return fig


def bar_chart(df, x, y, color=None, title=""):

    fig = px.bar(

        df,

        x=x,

        y=y,

        color=color,

        title=title

    )

    return fig


def histogram(df, x, color=None, title=""):

    fig = px.histogram(

        df,

        x=x,

        color=color,

        title=title

    )

    return fig