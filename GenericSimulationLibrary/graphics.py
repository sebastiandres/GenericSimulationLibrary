def general_plot(configuration, inputs, plot_options, outputs, 
                filename="", display=True, my_line_coeffs=[]):
    """If possible, plots the experimental data given
    in plot_options, the simulation data, and interactive line.
    
    :param filename: Filename to save the graph. If not provided, figure is not saved. Defaults to ''.
    :type filename: str, optional
    :param display: Boolean to show (True) or not show (False) the graph. Defaults to False
    :type display: bool, optional
    """
    if configuration["matplotlib_version"]:
        from matplotlib import pyplot as plt
    else:
        print("Cannot plot - ipywidget library not installed.")
        return
    # Fix empty plot_options
    if "sim_kwargs" not in outputs:
        outputs["sim_kwargs"] = {'label':'sim', 'color':'black'}#, 'marker':'o', 'markersize':6, 'linestyle':'dashed','linewidth':2}
    if "data_kwargs" not in outputs:
        outputs["data_kwargs"] = {'label':'exp', 'color':'red'}#, 'marker':'s', 'markersize':6, 'linestyle':'none','linewidth':2}
    # Create the figure
    my_fig = plt.figure(figsize=(16,8))
    has_content = False
    # Add the simulation, if possible
    if "x" in outputs and "y" in outputs:
        x = outputs["x"]
        y = outputs["y"]
        plt.plot(x, y, **plot_options["sim_kwargs"])
        has_content=True
    # Add the (experimental) plot_options, if possible
    if "data_x" in plot_options and "data_y" in plot_options:
        data_x = plot_options["data_x"]
        data_y = plot_options["data_y"]
        plt.plot(data_x, data_y, **plot_options["data_kwargs"])
        has_content=True
        # Add the line
        if len(my_line_coeffs)==2:
            m, b = my_line_coeffs
            line_x = [min(data_x), max(data_x)]
            line_y = [m*xi+b for xi in line_x]
            plt.plot(line_x, line_y, **plot_options["sim_kwargs"])
    plt.legend()
    # Add the properties
    if "xlabel" in plot_options:
        plt.xlabel(plot_options["xlabel"])
    if "ylabel" in plot_options:
        plt.ylabel(plot_options["ylabel"])
    if "title" in plot_options:
        plt.title(plot_options["title"])
    # Save figure, if filename provided
    if filename:
        my_fig.savefig(filename)
    # Show figure, if asked for
    if display:
        if has_content:
            plt.show()
        else:
            print("No content to plot.")
    else:
        plt.close()
    return

def delegated_plot(configuration, inputs, plot_options, outputs, filename="", display=True):
    general_plot(configuration, inputs, plot_options, outputs, filename, display, my_line_coeffs=[])
    return

def delegated_interactive_plot(configuration, inputs, plot_options, outputs, filename, display):
    """[summary]
    """
    if configuration["ipywidget_version"]:
        from ipywidgets import interactive
    else:
        print("Cannot plot - ipywidget library not installed.")
        return

    def f(m,b):
        my_line_coeffs = [m, b]
        general_plot(configuration, inputs, plot_options, outputs, filename, display, my_line_coeffs)

    interactive_plot = interactive(f, m=(0.0, 6.0), b=(-10, 10, 0.5))
    return interactive_plot