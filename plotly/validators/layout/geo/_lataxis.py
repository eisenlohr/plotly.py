import _plotly_utils.basevalidators


class LataxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='lataxis', parent_name='layout.geo', **kwargs
    ):
        super(LataxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Lataxis',
            data_docs="""
            dtick
                Sets the graticule's longitude/latitude tick
                step.
            gridcolor
                Sets the graticule's stroke color.
            gridwidth
                Sets the graticule's stroke width (in px).
            range
                Sets the range of this axis (in degrees), sets
                the map's clipped coordinates.
            showgrid
                Sets whether or not graticule are shown on the
                map.
            tick0
                Sets the graticule's starting tick
                longitude/latitude.
""",
            **kwargs
        )