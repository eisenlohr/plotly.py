from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Lonaxis(BaseLayoutHierarchyType):

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the graticule's longitude/latitude tick step.
    
        The 'dtick' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dtick']

    @dtick.setter
    def dtick(self, val):
        self['dtick'] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the graticule's stroke color.
    
        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['gridcolor']

    @gridcolor.setter
    def gridcolor(self, val):
        self['gridcolor'] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the graticule's stroke width (in px).
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['gridwidth']

    @gridwidth.setter
    def gridwidth(self, val):
        self['gridwidth'] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis (in degrees), sets the map's
        clipped coordinates.
    
        The 'range' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Sets whether or not graticule are shown on the map.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showgrid']

    @showgrid.setter
    def showgrid(self, val):
        self['showgrid'] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the graticule's starting tick longitude/latitude.
    
        The 'tick0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['tick0']

    @tick0.setter
    def tick0(self, val):
        self['tick0'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.geo'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dtick
            Sets the graticule's longitude/latitude tick step.
        gridcolor
            Sets the graticule's stroke color.
        gridwidth
            Sets the graticule's stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map's clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule's starting tick longitude/latitude.
        """

    def __init__(
        self,
        arg=None,
        dtick=None,
        gridcolor=None,
        gridwidth=None,
        range=None,
        showgrid=None,
        tick0=None,
        **kwargs
    ):
        """
        Construct a new Lonaxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.geo.Lonaxis
        dtick
            Sets the graticule's longitude/latitude tick step.
        gridcolor
            Sets the graticule's stroke color.
        gridwidth
            Sets the graticule's stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map's clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule's starting tick longitude/latitude.

        Returns
        -------
        Lonaxis
        """
        super(Lonaxis, self).__init__('lonaxis')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.geo.Lonaxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.geo.Lonaxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import (lonaxis as v_lonaxis)

        # Initialize validators
        # ---------------------
        self._validators['dtick'] = v_lonaxis.DtickValidator()
        self._validators['gridcolor'] = v_lonaxis.GridcolorValidator()
        self._validators['gridwidth'] = v_lonaxis.GridwidthValidator()
        self._validators['range'] = v_lonaxis.RangeValidator()
        self._validators['showgrid'] = v_lonaxis.ShowgridValidator()
        self._validators['tick0'] = v_lonaxis.Tick0Validator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('dtick', None)
        self['dtick'] = dtick if dtick is not None else _v
        _v = arg.pop('gridcolor', None)
        self['gridcolor'] = gridcolor if gridcolor is not None else _v
        _v = arg.pop('gridwidth', None)
        self['gridwidth'] = gridwidth if gridwidth is not None else _v
        _v = arg.pop('range', None)
        self['range'] = range if range is not None else _v
        _v = arg.pop('showgrid', None)
        self['showgrid'] = showgrid if showgrid is not None else _v
        _v = arg.pop('tick0', None)
        self['tick0'] = tick0 if tick0 is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False