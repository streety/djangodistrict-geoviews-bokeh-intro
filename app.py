from flask import Flask, render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE

app = Flask(__name__)



@app.route("/")
def polynomial():
    """ Very simple embedding of a polynomial chart

    """

    # Create a polynomial line graph with those arguments
    x = range(0, 10)
    fig = figure(title="Polynomial")
    fig.line(x, [i ** 2 for i in x], color='red', line_width=2)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    html = render_template(
        'embed.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html

if __name__ == "__main__":
    app.run(debug=True)
