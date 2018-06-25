from plotly.basedatatypes import BaseTraceType


class Splom(BaseTraceType):

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        *scatter* traces also appends customdata items in the markers
        DOM elements
    
        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['customdata']

    @customdata.setter
    def customdata(self, val):
        self['customdata'] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on plot.ly for  customdata .
    
        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['customdatasrc']

    @customdatasrc.setter
    def customdatasrc(self, val):
        self['customdatasrc'] = val

    # diagonal
    # --------
    @property
    def diagonal(self):
        """
        The 'diagonal' property is an instance of Diagonal
        that may be specified as:
          - An instance of plotly.graph_objs.splom.Diagonal
          - A dict of string/value properties that will be passed
            to the Diagonal constructor
    
            Supported dict properties:
                
                visible
                    Determines whether or not subplots on the
                    diagonal are displayed.

        Returns
        -------
        plotly.graph_objs.splom.Diagonal
        """
        return self['diagonal']

    @diagonal.setter
    def diagonal(self, val):
        self['diagonal'] = val

    # dimensions
    # ----------
    @property
    def dimensions(self):
        """
        The 'dimensions' property is a tuple of instances of
        Dimension that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.splom.Dimension
          - A list or tuple of dicts of string/value properties that
            will be passed to the Dimension constructor
    
            Supported dict properties:
                
                label
                    Sets the label corresponding to this splom
                    dimension.
                values
                    Sets the dimension values to be plotted.
                valuessrc
                    Sets the source reference on plot.ly for
                    values .
                visible
                    Determines whether or not this dimension is
                    shown on the graph. Note that even visible
                    false dimension contribute to the default grid
                    generate by this splom trace.

        Returns
        -------
        tuple[plotly.graph_objs.splom.Dimension]
        """
        return self['dimensions']

    @dimensions.setter
    def dimensions(self, val):
        self['dimensions'] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.
    
        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on plot.ly for  hoverinfo .
    
        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hoverinfosrc']

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self['hoverinfosrc'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.splom.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on plot.ly for
                    bgcolor .
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on plot.ly for
                    bordercolor .
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the length (in number of characters) of
                    the trace name in the hover labels for this
                    trace. -1 shows the whole name regardless of
                    length. 0-3 shows the first 0-3 characters, and
                    an integer >3 will show the whole name if it is
                    less than that many characters, but if it is
                    longer, will truncate to `namelength - 3`
                    characters and add an ellipsis.
                namelengthsrc
                    Sets the source reference on plot.ly for
                    namelength .

        Returns
        -------
        plotly.graph_objs.splom.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.
    
        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ids']

    @ids.setter
    def ids(self, val):
        self['ids'] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on plot.ly for  ids .
    
        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['idssrc']

    @idssrc.setter
    def idssrc(self, val):
        self['idssrc'] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.
    
        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['legendgroup']

    @legendgroup.setter
    def legendgroup(self, val):
        self['legendgroup'] = val

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.splom.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                autocolorscale
                    Has an effect only if `marker.color` is set to
                    a numerical array. Determines whether the
                    colorscale is a default palette
                    (`autocolorscale: true`) or the palette
                    determined by `marker.colorscale`. In case
                    `colorscale` is unspecified or `autocolorscale`
                    is true, the default  palette will be chosen
                    according to whether numbers in the `color`
                    array are all positive, all negative or mixed.
                cauto
                    Has an effect only if `marker.color` is set to
                    a numerical array and `cmin`, `cmax` are set by
                    the user. In this case, it controls whether the
                    range of colors in `colorscale` is mapped to
                    the range of values in the `color` array
                    (`cauto: true`), or the `cmin`/`cmax` values
                    (`cauto: false`). Defaults to `false` when
                    `cmin`, `cmax` are set by the user.
                cmax
                    Has an effect only if `marker.color` is set to
                    a numerical array. Sets the upper bound of the
                    color domain. Value should be associated to the
                    `marker.color` array index, and if set,
                    `marker.cmin` must be set as well.
                cmin
                    Has an effect only if `marker.color` is set to
                    a numerical array. Sets the lower bound of the
                    color domain. Value should be associated to the
                    `marker.color` array index, and if set,
                    `marker.cmax` must be set as well.
                color
                    Sets the marker color. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `cmin` and `cmax` if set.
                colorbar
                    plotly.graph_objs.splom.marker.ColorBar
                    instance or dict with compatible properties
                colorscale
                    Sets the colorscale and only has an effect if
                    `marker.color` is set to a numerical array. The
                    colorscale must be an array containing arrays
                    mapping a normalized value to an rgb, rgba,
                    hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                    control the bounds of the colorscale in color
                    space, use `marker.cmin` and `marker.cmax`.
                    Alternatively, `colorscale` may be a palette
                    name string of the following list: Greys,
                    YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds,
                    Blues, Picnic, Rainbow, Portland, Jet, Hot,
                    Blackbody, Earth, Electric, Viridis, Cividis
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                line
                    plotly.graph_objs.splom.marker.Line instance or
                    dict with compatible properties
                opacity
                    Sets the marker opacity.
                opacitysrc
                    Sets the source reference on plot.ly for
                    opacity .
                reversescale
                    Has an effect only if `marker.color` is set to
                    a numerical array. Reverses the color mapping
                    if true (`cmin` will correspond to the last
                    color in the array and `cmax` will correspond
                    to the first color).
                showscale
                    Has an effect only if `marker.color` is set to
                    a numerical array. Determines whether or not a
                    colorbar is displayed.
                size
                    Sets the marker size (in px).
                sizemin
                    Has an effect only if `marker.size` is set to a
                    numerical array. Sets the minimum size (in px)
                    of the rendered marker points.
                sizemode
                    Has an effect only if `marker.size` is set to a
                    numerical array. Sets the rule for which the
                    data in `size` is converted to pixels.
                sizeref
                    Has an effect only if `marker.size` is set to a
                    numerical array. Sets the scale factor used to
                    determine the rendered size of marker points.
                    Use with `sizemin` and `sizemode`.
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .
                symbol
                    Sets the marker symbol type. Adding 100 is
                    equivalent to appending *-open* to a symbol
                    name. Adding 200 is equivalent to appending
                    *-dot* to a symbol name. Adding 300 is
                    equivalent to appending *-open-dot* or *dot-
                    open* to a symbol name.
                symbolsrc
                    Sets the source reference on plot.ly for
                    symbol .

        Returns
        -------
        plotly.graph_objs.splom.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the trace.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # selected
    # --------
    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of plotly.graph_objs.splom.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.splom.selected.Marker
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.splom.Selected
        """
        return self['selected']

    @selected.setter
    def selected(self, val):
        self['selected'] = val

    # selectedpoints
    # --------------
    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.
    
        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['selectedpoints']

    @selectedpoints.setter
    def selectedpoints(self, val):
        self['selectedpoints'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # showlowerhalf
    # -------------
    @property
    def showlowerhalf(self):
        """
        Determines whether or not subplots on the lower half from the
        diagonal are displayed.
    
        The 'showlowerhalf' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlowerhalf']

    @showlowerhalf.setter
    def showlowerhalf(self, val):
        self['showlowerhalf'] = val

    # showupperhalf
    # -------------
    @property
    def showupperhalf(self):
        """
        Determines whether or not subplots on the upper half from the
        diagonal are displayed.
    
        The 'showupperhalf' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showupperhalf']

    @showupperhalf.setter
    def showupperhalf(self, val):
        self['showupperhalf'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.splom.Stream
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to *50*, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See
                    https://plot.ly/settings for more details.

        Returns
        -------
        plotly.graph_objs.splom.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets text elements associated with each (x,y) pair to appear on
        hover. If a single string, the same string appears over all the
        data points. If an array of string, the items are mapped in
        order to the this trace's (x,y) coordinates.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on plot.ly for  text .
    
        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['textsrc']

    @textsrc.setter
    def textsrc(self, val):
        self['textsrc'] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['uid']

    @uid.setter
    def uid(self, val):
        self['uid'] = val

    # unselected
    # ----------
    @property
    def unselected(self):
        """
        The 'unselected' property is an instance of Unselected
        that may be specified as:
          - An instance of plotly.graph_objs.splom.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.splom.unselected.Marker
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.splom.Unselected
        """
        return self['unselected']

    @unselected.setter
    def unselected(self, val):
        self['unselected'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        *legendonly*, the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).
    
        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # xaxes
    # -----
    @property
    def xaxes(self):
        """
        Sets the list of x axes corresponding to this splom trace. By
        default, a splom will match the first N xaxes where N is the
        number of input dimensions.
    
        The 'xaxes' property is an info array that may be specified as a
        list or tuple of up to 1 elements where:
    
    (0) The 'xaxes[0]' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        list
        """
        return self['xaxes']

    @xaxes.setter
    def xaxes(self, val):
        self['xaxes'] = val

    # yaxes
    # -----
    @property
    def yaxes(self):
        """
        Sets the list of y axes corresponding to this splom trace. By
        default, a splom will match the first N yaxes where N is the
        number of input dimensions.
    
        The 'yaxes' property is an info array that may be specified as a
        list or tuple of up to 1 elements where:
    
    (0) The 'yaxes[0]' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        list
        """
        return self['yaxes']

    @yaxes.setter
    def yaxes(self, val):
        self['yaxes'] = val

    # type
    # ----
    @property
    def type(self):
        return self._props['type']

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return ''

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, *scatter* traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        diagonal
            plotly.graph_objs.splom.Diagonal instance or dict with
            compatible properties
        dimensions
            plotly.graph_objs.splom.Dimension instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.splom.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.splom.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.splom.Selected instance or dict with
            compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showlowerhalf
            Determines whether or not subplots on the lower half
            from the diagonal are displayed.
        showupperhalf
            Determines whether or not subplots on the upper half
            from the diagonal are displayed.
        stream
            plotly.graph_objs.splom.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each (x,y) pair to
            appear on hover. If a single string, the same string
            appears over all the data points. If an array of
            string, the items are mapped in order to the this
            trace's (x,y) coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        unselected
            plotly.graph_objs.splom.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            *legendonly*, the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxes
            Sets the list of x axes corresponding to this splom
            trace. By default, a splom will match the first N xaxes
            where N is the number of input dimensions.
        yaxes
            Sets the list of y axes corresponding to this splom
            trace. By default, a splom will match the first N yaxes
            where N is the number of input dimensions.
        """

    def __init__(
        self,
        arg=None,
        customdata=None,
        customdatasrc=None,
        diagonal=None,
        dimensions=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showlowerhalf=None,
        showupperhalf=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        unselected=None,
        visible=None,
        xaxes=None,
        yaxes=None,
        **kwargs
    ):
        """
        Construct a new Splom object
        
        Splom traces generate scatter plot matrix visualizations. Each
        splom `dimensions` items correspond to a generated axis. Values
        for each of those dimensions are set in `dimensions[i].values`.
        Splom traces support all `scattergl` marker style attributes.
        Specify `layout.grid` attributes and/or layout x-axis and
        y-axis attributes for more control over the axis positioning
        and style.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Splom
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, *scatter* traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        diagonal
            plotly.graph_objs.splom.Diagonal instance or dict with
            compatible properties
        dimensions
            plotly.graph_objs.splom.Dimension instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.splom.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.splom.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            plotly.graph_objs.splom.Selected instance or dict with
            compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showlowerhalf
            Determines whether or not subplots on the lower half
            from the diagonal are displayed.
        showupperhalf
            Determines whether or not subplots on the upper half
            from the diagonal are displayed.
        stream
            plotly.graph_objs.splom.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each (x,y) pair to
            appear on hover. If a single string, the same string
            appears over all the data points. If an array of
            string, the items are mapped in order to the this
            trace's (x,y) coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        unselected
            plotly.graph_objs.splom.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            *legendonly*, the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxes
            Sets the list of x axes corresponding to this splom
            trace. By default, a splom will match the first N xaxes
            where N is the number of input dimensions.
        yaxes
            Sets the list of y axes corresponding to this splom
            trace. By default, a splom will match the first N yaxes
            where N is the number of input dimensions.

        Returns
        -------
        Splom
        """
        super(Splom, self).__init__('splom')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Splom 
constructor must be a dict or 
an instance of plotly.graph_objs.Splom"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (splom as v_splom)

        # Initialize validators
        # ---------------------
        self._validators['customdata'] = v_splom.CustomdataValidator()
        self._validators['customdatasrc'] = v_splom.CustomdatasrcValidator()
        self._validators['diagonal'] = v_splom.DiagonalValidator()
        self._validators['dimensions'] = v_splom.DimensionsValidator()
        self._validators['hoverinfo'] = v_splom.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_splom.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_splom.HoverlabelValidator()
        self._validators['ids'] = v_splom.IdsValidator()
        self._validators['idssrc'] = v_splom.IdssrcValidator()
        self._validators['legendgroup'] = v_splom.LegendgroupValidator()
        self._validators['marker'] = v_splom.MarkerValidator()
        self._validators['name'] = v_splom.NameValidator()
        self._validators['opacity'] = v_splom.OpacityValidator()
        self._validators['selected'] = v_splom.SelectedValidator()
        self._validators['selectedpoints'] = v_splom.SelectedpointsValidator()
        self._validators['showlegend'] = v_splom.ShowlegendValidator()
        self._validators['showlowerhalf'] = v_splom.ShowlowerhalfValidator()
        self._validators['showupperhalf'] = v_splom.ShowupperhalfValidator()
        self._validators['stream'] = v_splom.StreamValidator()
        self._validators['text'] = v_splom.TextValidator()
        self._validators['textsrc'] = v_splom.TextsrcValidator()
        self._validators['uid'] = v_splom.UidValidator()
        self._validators['unselected'] = v_splom.UnselectedValidator()
        self._validators['visible'] = v_splom.VisibleValidator()
        self._validators['xaxes'] = v_splom.XaxesValidator()
        self._validators['yaxes'] = v_splom.YaxesValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('customdata', None)
        self.customdata = customdata or v
        v = arg.pop('customdatasrc', None)
        self.customdatasrc = customdatasrc or v
        v = arg.pop('diagonal', None)
        self.diagonal = diagonal or v
        v = arg.pop('dimensions', None)
        self.dimensions = dimensions or v
        v = arg.pop('hoverinfo', None)
        self.hoverinfo = hoverinfo or v
        v = arg.pop('hoverinfosrc', None)
        self.hoverinfosrc = hoverinfosrc or v
        v = arg.pop('hoverlabel', None)
        self.hoverlabel = hoverlabel or v
        v = arg.pop('ids', None)
        self.ids = ids or v
        v = arg.pop('idssrc', None)
        self.idssrc = idssrc or v
        v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup or v
        v = arg.pop('marker', None)
        self.marker = marker or v
        v = arg.pop('name', None)
        self.name = name or v
        v = arg.pop('opacity', None)
        self.opacity = opacity or v
        v = arg.pop('selected', None)
        self.selected = selected or v
        v = arg.pop('selectedpoints', None)
        self.selectedpoints = selectedpoints or v
        v = arg.pop('showlegend', None)
        self.showlegend = showlegend or v
        v = arg.pop('showlowerhalf', None)
        self.showlowerhalf = showlowerhalf or v
        v = arg.pop('showupperhalf', None)
        self.showupperhalf = showupperhalf or v
        v = arg.pop('stream', None)
        self.stream = stream or v
        v = arg.pop('text', None)
        self.text = text or v
        v = arg.pop('textsrc', None)
        self.textsrc = textsrc or v
        v = arg.pop('uid', None)
        self.uid = uid or v
        v = arg.pop('unselected', None)
        self.unselected = unselected or v
        v = arg.pop('visible', None)
        self.visible = visible or v
        v = arg.pop('xaxes', None)
        self.xaxes = xaxes or v
        v = arg.pop('yaxes', None)
        self.yaxes = yaxes or v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'splom'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='splom'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))