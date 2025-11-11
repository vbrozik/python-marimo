# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas>=2.3.3",
#     "plotly>=6.4.0",
# ]
#
# [tool.marimo.display]
# theme = "system"
# # ///

"""Marimo notebook illustrating i^x in the complex plane."""

import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    """Import required libraries."""
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    return go, mo, np


@app.cell
def _(mo):
    """Create interactive slider for the exponent."""
    mo.md(
        r"""
        # Exponentiating the Imaginary Unit: $i^x$

        This notebook explores the behavior of $i^x$ where $i$ is the imaginary unit ($\sqrt{-1}$) 
        and $x$ is a real number.

        ## Mathematical Background

        Using Euler's formula, we can express $i$ as:
    
        $$
        i = e^{iπ/2}
        $$

        Therefore:
    
        $$
        i^x = (e^{iπ/2})^x = e^{iπx/2}
        $$

        Using Euler's formula again: $e^{iθ} = cos(θ) + i·sin(θ)$, we get:
    
        $$
        i^x = cos(πx/2) + i·sin(πx/2)
        $$

        This means $i^x$ traces a path on the unit circle in the complex plane.

        ## Interactive graph
        """
    )
    return


@app.cell
def _(mo):
    """Create slider for setting the step size of the exponent slider."""
    x_slider_step = mo.ui.slider(
        start=0.01,
        stop=1.0,
        step=0.01,
        value=0.1,
        label="Slider Step Size:",
        show_value=True,
    )
    x_slider_step
    return (x_slider_step,)


@app.cell
def _(mo, x_slider_step):
    """Create slider for $x$ value."""
    x_slider = mo.ui.slider(
        start=-4.0,
        stop=4.0,
        # step=0.1,
        step=x_slider_step.value,
        value=0.0,
        label="Exponent $x$:",
        show_value=True,
        full_width=True,
    )
    x_slider
    return (x_slider,)


@app.cell
def _(go, mo, np, x_slider):
    """Compute and visualize $i^x$ in the complex plane."""
    # Get current x value
    x_current = x_slider.value

    # Compute i^x for the current value
    # i^x = e^(i*pi*x/2) = cos(pi*x/2) + i*sin(pi*x/2)
    angle = np.pi * x_current / 2
    result_real = np.cos(angle)
    result_imag = np.sin(angle)

    # Detect notebook theme and set Plotly template
    theme = mo.app_meta().theme
    # Note: The value probably fails when the notebook is set to use the system theme.
    # See: https://gemini.google.com/share/9c6b606ebdeb
    theme = 'dark'
    plotly_template = 'plotly_dark' if theme == 'dark' else 'plotly'

    # Create the plot
    fig = go.Figure()

    # Add the unit circle
    circle_theta = np.linspace(0, 2*np.pi, 100)
    fig.add_trace(go.Scatter(
        x=np.cos(circle_theta),
        y=np.sin(circle_theta),
        mode='lines',
        line=dict(color='lightgray', dash='dash', width=1),
        name='Unit Circle',
        showlegend=True
    ))

    # # Create array of x values for the path
    # x_values = np.linspace(-4, 4, 200)
    # angles = np.pi * x_values / 2
    # path_real = np.cos(angles)
    # path_imag = np.sin(angles)
    # # Add the path of i^x as x varies
    # fig.add_trace(go.Scatter(
    #     x=path_real,
    #     y=path_imag,
    #     mode='lines',
    #     line=dict(color='blue', width=2),
    #     name='Path of i^x',
    #     showlegend=True
    # ))

    # Add the current point i^x
    fig.add_trace(go.Scatter(
        x=[result_real],
        y=[result_imag],
        mode='markers+text',
        marker=dict(size=12, color='red'),
        text=[f'i^{x_current:.2f}'],
        textposition='top center',
        name=f'i^{x_current:.2f}',
        showlegend=True
    ))

    # Add vector from origin to current point
    fig.add_trace(go.Scatter(
        x=[0, result_real],
        y=[0, result_imag],
        mode='lines',
        line=dict(color='red', width=2),
        name='Vector',
        showlegend=False
    ))

    # # Add axes
    # fig.add_trace(go.Scatter(
    #     x=[-1.5, 1.5],
    #     y=[0, 0],
    #     mode='lines',
    #     line=dict(color='black', width=1),
    #     showlegend=False
    # ))
    # fig.add_trace(go.Scatter(
    #     x=[0, 0],
    #     y=[-1.5, 1.5],
    #     mode='lines',
    #     line=dict(color='black', width=1),
    #     showlegend=False
    # ))

    # Update layout
    fig.update_layout(
        title=f'i^x in the Complex Plane (x = {x_current:.2f})',
        xaxis_title='Real Part',
        yaxis_title='Imaginary Part',
        width=500,
        height=500,
        xaxis=dict(range=[-1.2, 1.2], scaleanchor='y', scaleratio=1),
        yaxis=dict(range=[-1.2, 1.2]),
        hovermode='closest',
        showlegend=True,
        template=plotly_template,
    )

    # Display result information
    result_text = mo.md(
        f"""
        ## Current Result

        **$x = {x_current:.2f}$**

        **$i^{{ {x_current:.2f} }} = {result_real:.4f} + {result_imag:.4f}i$**

        - Magnitude: $|i^x| = {np.sqrt(result_real**2 + result_imag**2):.4f}$
        - Angle: $arg(i^x) = {angle:.4f} radians = {np.degrees(angle):.2f}°$

        ### Special Values:
        - $i^0 = 1$
        - $i^1 = i$
        - $i^2 = -1$
        - $i^3 = -i$
        - $i^4 = 1$ (the cycle repeats)
        """
    )

    mo.vstack([fig, result_text])
    return


@app.cell
def _(mo):
    """Additional explanation."""
    mo.md(
        """
        ## Observations

        1. **Periodicity**: Since i^x traces the unit circle, it has a period of 4.
           That is, i^(x+4) = i^x for all real x.

        2. **Unit Circle**: The magnitude of i^x is always 1, so all values lie on the unit circle.

        3. **Rotation**: As x increases by 1, i^x rotates by π/2 radians (90°) counterclockwise.

        4. **Integer Powers**:
           - When x is an even integer: i^x = ±1 (real values)
           - When x is an odd integer: i^x = ±i (purely imaginary values)

        5. **Continuous Path**: As x varies continuously, i^x traces a continuous path on the unit circle.
        """
    )
    return


if __name__ == "__main__":
    app.run()
